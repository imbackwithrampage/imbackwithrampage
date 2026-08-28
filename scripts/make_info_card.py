#!/usr/bin/env python3
"""
Generate a sleek Neofetch-style terminal info card SVG for Sunil Sachindar S A.
Features:
- Title bar with macOS / terminal control dots
- Host info: sunil@imbackwithrampage
- OS / Terminal / Uptime / Roles / Stack / Highlights
- Staggered line-by-line slide/fade in animations
- Matches the exact dimensions and dark GitHub color scheme
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "info-card.svg")

CANVAS_W = 1000
CANVAS_H = 1040
PAD = 36
TITLEBAR_H = 46

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
    ("Shell", "zsh 5.9 (x86_64-apple-darwin)", MUTED),
    ("Role", "Full Stack Developer · AI Engineer · Builder", ACCENT_YELLOW),
    ("Languages", "Python, TypeScript, JavaScript, Go, C++, Rust", ACCENT_CYAN),
    ("Frameworks", "React, Next.js, FastAPI, Node.js, PyTorch, Tailwind", ACCENT_BLUE),
    ("Cloud / Ops", "Docker, Kubernetes, AWS, GCP, GitHub Actions, CI/CD", ACCENT_ORANGE),
    ("Interests", "LLMs, Computer Vision, Autonomous Agents, Scalable Systems", ACCENT_GREEN),
    ("Current Focus", "High-performance Agentic Systems & Real-time AI", ACCENT_YELLOW),
]

STATIC = bool(os.environ.get("STATIC"))

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" '
    f'viewBox="0 0 {CANVAS_W} {CANVAS_H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    f'<defs>',
    f'<linearGradient id="cbg" x1="0" y1="0" x2="0" y2="1">',
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>',
    f'</linearGradient>',
    f'<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
    f'</defs>',
    f'<style>',
    """
    @keyframes lineFade {
        0% { opacity: 0; transform: translateY(6px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .line { animation: lineFade 0.45s cubic-bezier(0.16, 1, 0.3, 1) both; }
    """,
    f'</style>',
    f'<rect width="{CANVAS_W}" height="{CANVAS_H}" rx="14" fill="url(#cbg)"/>',
    f'<rect x="0.5" y="0.5" width="{CANVAS_W-1}" height="{CANVAS_H-1}" rx="14" fill="none" stroke="{FRAME}" stroke-width="1.2"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{CANVAS_W}" y2="{TITLEBAR_H}" stroke="{FRAME}" stroke-width="1.2"/>',
]

# Control dots
for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*22}" cy="{TITLEBAR_H/2}" r="6.5" fill="{dotcol}"/>')

parts.append(f'<text x="{CANVAS_W/2}" y="{TITLEBAR_H/2 + 5}" fill="{TITLE_TEXT}" font-size="14" font-weight="600" text-anchor="middle">sunil@rampage: ~$ neofetch</text>')

start_y = TITLEBAR_H + 45
line_h = 38
delay_step = 0.08
current_delay = 0.1

# Header banner
header_txt = '<text class="line" x="{x}" y="{y}" style="animation-delay:{d:.2f}s">' \
             '<tspan fill="{u_col}" font-weight="700" font-size="20">sunil</tspan>' \
             '<tspan fill="{at_col}" font-size="18">@</tspan>' \
             '<tspan fill="{h_col}" font-weight="700" font-size="20">imbackwithrampage</tspan>' \
             '</text>'.format(x=PAD+10, y=start_y, d=current_delay, u_col=ACCENT_CYAN, at_col=MUTED, h_col=ACCENT_PURPLE)
parts.append(header_txt)

# Separator
current_delay += delay_step
sep_y = start_y + 14
parts.append(f'<line class="line" x1="{PAD+10}" y1="{sep_y}" x2="{CANVAS_W - PAD - 10}" y2="{sep_y}" stroke="{FRAME}" stroke-width="1.5" style="animation-delay:{current_delay:.2f}s"/>')

cur_y = sep_y + 34
for label, val, color in info_items:
    current_delay += delay_step
    line_svg = (
        f'<g class="line" style="animation-delay:{current_delay:.2f}s">'
        f'<text x="{PAD+10}" y="{cur_y}" font-size="16" font-weight="700" fill="{color}">{label:<14}</text>'
        f'<text x="{PAD+180}" y="{cur_y}" font-size="15" fill="{MUTED}">~ </text>'
        f'<text x="{PAD+205}" y="{cur_y}" font-size="15" fill="{TEXT}">{val}</text>'
        f'</g>'
    )
    parts.append(line_svg)
    cur_y += line_h

# Color Palette block (classic neofetch color bar)
current_delay += delay_step
palette_y = cur_y + 16
parts.append(f'<g class="line" style="animation-delay:{current_delay:.2f}s">')
colors_row1 = ["#1f242c", "#f85149", "#3fb950", "#d29922", "#58a6ff", "#bc8cff", "#22d3ee", "#e6edf3"]
colors_row2 = ["#484f58", "#ff7b72", "#56d364", "#e3b341", "#79c0ff", "#d2a8ff", "#56e3f5", "#ffffff"]

box_w = 42
box_h = 20
box_gap = 10

for i, col in enumerate(colors_row1):
    bx = PAD + 10 + i * (box_w + box_gap)
    parts.append(f'<rect x="{bx}" y="{palette_y}" width="{box_w}" height="{box_h}" rx="4" fill="{col}"/>')

for i, col in enumerate(colors_row2):
    bx = PAD + 10 + i * (box_w + box_gap)
    parts.append(f'<rect x="{bx}" y="{palette_y + box_h + 6}" width="{box_w}" height="{box_h}" rx="4" fill="{col}"/>')
parts.append('</g>')

# Prompt line at the bottom
current_delay += delay_step
bot_y = palette_y + box_h * 2 + 50
parts.append(f'<line class="line" x1="{PAD+10}" y1="{bot_y-25}" x2="{CANVAS_W-PAD-10}" y2="{bot_y-25}" stroke="{FRAME}" stroke-width="1.2" style="animation-delay:{current_delay:.2f}s"/>')
parts.append(f'<g class="line" style="animation-delay:{current_delay:.2f}s">')
parts.append(f'<text x="{PAD+10}" y="{bot_y}" fill="{ACCENT_CYAN}" font-size="15" font-weight="700">sunil@rampage</text>')
parts.append(f'<text x="{PAD+155}" y="{bot_y}" fill="{MUTED}" font-size="15">:</text>')
parts.append(f'<text x="{PAD+170}" y="{bot_y}" fill="{ACCENT_YELLOW}" font-size="15">~</text>')
parts.append(f'<text x="{PAD+185}" y="{bot_y}" fill="{TEXT}" font-size="15">$</text>')
parts.append(f'<text x="{PAD+205}" y="{bot_y}" fill="{MUTED}" font-size="15">echo &quot;Ready to build the future.&quot;</text>')
parts.append(f'<rect x="{PAD+545}" y="{bot_y-14}" width="9" height="17" fill="{ACCENT_CYAN}">'
             f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite"/></rect>')
parts.append('</g>')

parts.append("</svg>")
svg = "".join(parts)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"wrote {OUT} ({len(svg)} bytes; {CANVAS_W}x{CANVAS_H})")
