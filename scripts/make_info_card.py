#!/usr/bin/env python3
"""
Generate a GitHub-safe Neofetch-style terminal info card SVG for Sunil Sachindar S A.
Uses pure SMIL animations (native in GitHub <img> embedding, no unsafe CSS or filters).
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "info-card.svg")

CANVAS_W = 840
CANVAS_H = 875
PAD = 26
TITLEBAR_H = 36

BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
TITLE_TEXT = "#7d8590"
TEXT = "#e6edf3"
MUTED = "#8b949e"
ACCENT_BLUE = "#58a6ff"
ACCENT_CYAN = "#22d3ee"
ACCENT_GREEN = "#3fb950"
ACCENT_PURPLE = "#bc8cff"
ACCENT_YELLOW = "#e3b341"
ACCENT_ORANGE = "#f0883e"

info_items = [
    ("OS", "Arch Linux / macOS / Neural Core x86_64", ACCENT_CYAN),
    ("Host", "imbackwithrampage", ACCENT_PURPLE),
    ("Kernel", "6.12.0-sunil-prod #1 SMP PREEMPT", MUTED),
    ("Uptime", "24/7 Deep Learning & Fullstack Flow", ACCENT_GREEN),
    ("Role", "Full Stack Developer · AI Engineer · Builder", ACCENT_YELLOW),
    ("Languages", "Python, TypeScript, JavaScript, Go, C++, Rust", ACCENT_CYAN),
    ("Frameworks", "React, Next.js, FastAPI, Node.js, PyTorch", ACCENT_BLUE),
    ("Cloud / Ops", "Docker, Kubernetes, AWS, GCP, GitHub Actions", ACCENT_ORANGE),
    ("Interests", "LLMs, Computer Vision, Autonomous Agents", ACCENT_GREEN),
    ("Current Focus", "High-performance Agentic Systems & Real-time AI", ACCENT_YELLOW),
]

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" '
    f'viewBox="0 0 {CANVAS_W} {CANVAS_H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    f'<defs>',
    f'<linearGradient id="cbg" x1="0" y1="0" x2="0" y2="1">',
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>',
    f'</linearGradient>',
    f'</defs>',
    f'<rect width="{CANVAS_W}" height="{CANVAS_H}" rx="12" fill="url(#cbg)"/>',
    f'<rect x="0.5" y="0.5" width="{CANVAS_W-1}" height="{CANVAS_H-1}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{CANVAS_W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]

# Control dots
for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*18}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')

parts.append(f'<text x="{CANVAS_W/2}" y="{TITLEBAR_H/2 + 4}" fill="{TITLE_TEXT}" font-size="12" font-weight="600" text-anchor="middle">sunil@rampage: ~$ neofetch</text>')

start_y = TITLEBAR_H + 42
line_h = 42
delay_step = 0.08
current_delay = 0.12

# Header banner
parts.append(
    f'<g opacity="0">'
    f'<set attributeName="opacity" to="1" begin="{current_delay:.2f}s"/>'
    f'<text x="{PAD+8}" y="{start_y}" font-size="18" font-weight="700">'
    f'<tspan fill="{ACCENT_CYAN}">sunil</tspan>'
    f'<tspan fill="{MUTED}">@</tspan>'
    f'<tspan fill="{ACCENT_PURPLE}">imbackwithrampage</tspan>'
    f'</text>'
    f'</g>'
)

current_delay += delay_step
sep_y = start_y + 16
parts.append(
    f'<g opacity="0">'
    f'<set attributeName="opacity" to="1" begin="{current_delay:.2f}s"/>'
    f'<line x1="{PAD+8}" y1="{sep_y}" x2="{CANVAS_W - PAD - 8}" y2="{sep_y}" stroke="{FRAME}" stroke-width="1.2"/>'
    f'</g>'
)

cur_y = sep_y + 36
for label, val, color in info_items:
    current_delay += delay_step
    safe_val = html.escape(val)
    line_svg = (
        f'<g opacity="0">'
        f'<set attributeName="opacity" to="1" begin="{current_delay:.2f}s"/>'
        f'<text x="{PAD+8}" y="{cur_y}" font-size="14" font-weight="700" fill="{color}">{label:<14}</text>'
        f'<text x="{PAD+150}" y="{cur_y}" font-size="14" fill="{MUTED}">~ </text>'
        f'<text x="{PAD+172}" y="{cur_y}" font-size="14" fill="{TEXT}">{safe_val}</text>'
        f'</g>'
    )
    parts.append(line_svg)
    cur_y += line_h

# Color Palette block (classic neofetch color bar)
current_delay += delay_step
palette_y = cur_y + 14
colors_row1 = ["#1f242c", "#f85149", "#3fb950", "#d29922", "#58a6ff", "#bc8cff", "#22d3ee", "#e6edf3"]
colors_row2 = ["#484f58", "#ff7b72", "#56d364", "#e3b341", "#79c0ff", "#d2a8ff", "#56e3f5", "#ffffff"]

box_w = 34
box_h = 16
box_gap = 8

palette_parts = [f'<g opacity="0"><set attributeName="opacity" to="1" begin="{current_delay:.2f}s"/>']
for i, col in enumerate(colors_row1):
    bx = PAD + 8 + i * (box_w + box_gap)
    palette_parts.append(f'<rect x="{bx}" y="{palette_y}" width="{box_w}" height="{box_h}" rx="3" fill="{col}"/>')

for i, col in enumerate(colors_row2):
    bx = PAD + 8 + i * (box_w + box_gap)
    palette_parts.append(f'<rect x="{bx}" y="{palette_y + box_h + 5}" width="{box_w}" height="{box_h}" rx="3" fill="{col}"/>')
palette_parts.append('</g>')
parts.append("".join(palette_parts))

# Bottom terminal prompt line
current_delay += delay_step
bot_sep_y = palette_y + box_h * 2 + 28
bot_y = bot_sep_y + 30
parts.append(
    f'<g opacity="0">'
    f'<set attributeName="opacity" to="1" begin="{current_delay:.2f}s"/>'
    f'<line x1="{PAD+8}" y1="{bot_sep_y}" x2="{CANVAS_W-PAD-8}" y2="{bot_sep_y}" stroke="{FRAME}" stroke-width="1"/>'
    f'<text x="{PAD+8}" y="{bot_y}" fill="{ACCENT_CYAN}" font-size="14" font-weight="700">sunil@rampage</text>'
    f'<text x="{PAD+136}" y="{bot_y}" fill="{MUTED}" font-size="14">:</text>'
    f'<text x="{PAD+148}" y="{bot_y}" fill="{ACCENT_YELLOW}" font-size="14">~</text>'
    f'<text x="{PAD+160}" y="{bot_y}" fill="{TEXT}" font-size="14">$</text>'
    f'<text x="{PAD+178}" y="{bot_y}" fill="{MUTED}" font-size="14">echo &quot;Ready to build the future.&quot;</text>'
    f'<rect x="{PAD+486}" y="{bot_y-12}" width="8" height="15" fill="{ACCENT_CYAN}">'
    f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite"/></rect>'
    f'</g>'
)

parts.append("</svg>")
svg = "".join(parts)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"wrote {OUT} ({len(svg)} bytes; {CANVAS_W}x{CANVAS_H})")
