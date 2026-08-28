#!/usr/bin/env python3
"""
Generate a rich, Neofetch-style terminal info card SVG for Sunil Sachindar S A.
Uses GitHub-proven SMIL wipe & opacity animations.
"""
import html
import os
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "sunil-info-card.svg")

CANVAS_W = 840
CANVAS_H = 875
PAD = 24
TITLEBAR_H = 32
ART_W = CANVAS_W - PAD * 2

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
ACCENT_PINK = "#f778ba"

info_items = [
    ("Host", "imbackwithrampage (Neural Core / x86_64)", ACCENT_PURPLE),
    ("Now", "AI Automation Developer @ Google DeepMind", ACCENT_CYAN),
    ("Role", "AI Engineer · Robotics & Autonomous Agent Builder", ACCENT_YELLOW),
    ("Research", "Agentic AI & SLMs (NIT Trichy) · Humanoid Robotics (PSGCET)", ACCENT_GREEN),
    ("Languages", "Python, Kotlin, Java, C++, TypeScript, Go, SQL", ACCENT_BLUE),
    ("AI / Robotics", "PyTorch, TensorFlow, ROS, MediaPipe, OpenCV, Jetson Nano", ACCENT_PINK),
    ("Cloud & Ops", "GCP, Docker, Kubernetes, Apache Spark, Airflow, CI/CD", ACCENT_ORANGE),
    ("Publications", "IEEE Embedded Systems Conf '24 · Robotics & Autonomous Systems", ACCENT_PURPLE),
    ("Honors", "NASA Space Apps Global Nominee · GCP Codeathon (Top 3)", ACCENT_YELLOW),
    ("Leadership", "GDG Cloud Computing Lead (7k+ devs) · Robotics Club President", ACCENT_CYAN),
]

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_W}" height="{CANVAS_H}" '
    f'viewBox="0 0 {CANVAS_W} {CANVAS_H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<defs>',
    f'<linearGradient id="ibg" x1="0" y1="0" x2="0" y2="1">',
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>',
    '</linearGradient>',
    '</defs>',
    f'<rect width="{CANVAS_W}" height="{CANVAS_H}" rx="12" fill="url(#ibg)"/>',
    f'<rect x="0.5" y="0.5" width="{CANVAS_W-1}" height="{CANVAS_H-1}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{CANVAS_W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]

# Control dots
for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')

parts.append(f'<text x="{CANVAS_W/2}" y="{TITLEBAR_H/2 + 4}" fill="{TITLE_TEXT}" font-size="12" font-weight="600" text-anchor="middle">sunil@rampage: ~$ neofetch --profile</text>')

start_y = TITLEBAR_H + 36
line_h = 42
delay_step = 0.08
current_delay = 0.10

# Header banner
parts.append(
    f'<clipPath id="chdr"><rect x="{PAD}" y="{start_y-20}" width="0" height="30">'
    f'<animate attributeName="width" from="0" to="{ART_W}" begin="{current_delay:.2f}s" dur="0.25s" fill="freeze"/></rect></clipPath>'
    f'<g clip-path="url(#chdr)">'
    f'<text x="{PAD+6}" y="{start_y}" font-size="17" font-weight="700">'
    f'<tspan fill="{ACCENT_CYAN}">sunil</tspan>'
    f'<tspan fill="{MUTED}">@</tspan>'
    f'<tspan fill="{ACCENT_PURPLE}">imbackwithrampage</tspan>'
    f'<tspan fill="{MUTED}" font-size="13" font-weight="400"> (Sunil Sachindar S A)</tspan>'
    f'</text>'
    f'</g>'
)

current_delay += delay_step
sep_y = start_y + 14
parts.append(
    f'<clipPath id="csep"><rect x="{PAD}" y="{sep_y-2}" width="0" height="6">'
    f'<animate attributeName="width" from="0" to="{ART_W}" begin="{current_delay:.2f}s" dur="0.25s" fill="freeze"/></rect></clipPath>'
    f'<g clip-path="url(#csep)">'
    f'<line x1="{PAD+6}" y1="{sep_y}" x2="{CANVAS_W - PAD - 6}" y2="{sep_y}" stroke="{FRAME}" stroke-width="1.2"/>'
    f'</g>'
)

cur_y = sep_y + 36
for idx, (label, val, color) in enumerate(info_items):
    current_delay += delay_step
    safe_label = html.escape(label)
    safe_val = html.escape(val)
    cid = f"ci{idx}"
    parts.append(
        f'<clipPath id="{cid}"><rect x="{PAD}" y="{cur_y-18}" width="0" height="26">'
        f'<animate attributeName="width" from="0" to="{ART_W}" begin="{current_delay:.2f}s" dur="0.25s" fill="freeze"/></rect></clipPath>'
        f'<g clip-path="url(#{cid})">'
        f'<text x="{PAD+6}" y="{cur_y}" font-size="13.5" font-weight="700" fill="{color}">{safe_label}</text>'
        f'<text x="{PAD+145}" y="{cur_y}" font-size="13.5" fill="{MUTED}">~ </text>'
        f'<text x="{PAD+168}" y="{cur_y}" font-size="13.5" fill="{TEXT}">{safe_val}</text>'
        f'</g>'
    )
    cur_y += line_h

# Color Palette block
current_delay += delay_step
palette_y = cur_y + 12
colors_row1 = ["#1f242c", "#f85149", "#3fb950", "#d29922", "#58a6ff", "#bc8cff", "#22d3ee", "#e6edf3"]
colors_row2 = ["#484f58", "#ff7b72", "#56d364", "#e3b341", "#79c0ff", "#d2a8ff", "#56e3f5", "#ffffff"]

box_w = 34
box_h = 16
box_gap = 8

parts.append(
    f'<clipPath id="cpal"><rect x="{PAD}" y="{palette_y-4}" width="0" height="50">'
    f'<animate attributeName="width" from="0" to="{ART_W}" begin="{current_delay:.2f}s" dur="0.3s" fill="freeze"/></rect></clipPath>'
    f'<g clip-path="url(#cpal)">'
)
for i, col in enumerate(colors_row1):
    bx = PAD + 6 + i * (box_w + box_gap)
    parts.append(f'<rect x="{bx}" y="{palette_y}" width="{box_w}" height="{box_h}" rx="3" fill="{col}"/>')

for i, col in enumerate(colors_row2):
    bx = PAD + 6 + i * (box_w + box_gap)
    parts.append(f'<rect x="{bx}" y="{palette_y + box_h + 5}" width="{box_w}" height="{box_h}" rx="3" fill="{col}"/>')
parts.append('</g>')

# Bottom terminal prompt line
current_delay += delay_step
bot_sep_y = palette_y + box_h * 2 + 28
bot_y = bot_sep_y + 28
parts.append(
    f'<clipPath id="cbot"><rect x="{PAD}" y="{bot_sep_y-2}" width="0" height="50">'
    f'<animate attributeName="width" from="0" to="{ART_W}" begin="{current_delay:.2f}s" dur="0.3s" fill="freeze"/></rect></clipPath>'
    f'<g clip-path="url(#cbot)">'
    f'<line x1="{PAD+6}" y1="{bot_sep_y}" x2="{CANVAS_W-PAD-6}" y2="{bot_sep_y}" stroke="{FRAME}" stroke-width="1"/>'
    f'<text x="{PAD+6}" y="{bot_y}" fill="{ACCENT_CYAN}" font-size="13.5" font-weight="700">sunil@rampage</text>'
    f'<text x="{PAD+132}" y="{bot_y}" fill="{MUTED}" font-size="13.5">:</text>'
    f'<text x="{PAD+144}" y="{bot_y}" fill="{ACCENT_YELLOW}" font-size="13.5">~</text>'
    f'<text x="{PAD+156}" y="{bot_y}" fill="{TEXT}" font-size="13.5">$</text>'
    f'<text x="{PAD+174}" y="{bot_y}" fill="{MUTED}" font-size="13.5">echo &quot;Building autonomous agents &amp; AI automation @ Google DeepMind.&quot;</text>'
    f'</g>'
    f'<rect x="{PAD+735}" y="{bot_y-12}" width="8" height="15" fill="{ACCENT_CYAN}">'
    f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite"/></rect>'
)

parts.append("</svg>")
svg = "".join(parts)

# Strict XML Validation
try:
    ET.fromstring(svg)
    print("XML Validation PASSED")
except Exception as e:
    print("XML Validation FAILED:", e)
    sys.exit(1)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"wrote {OUT} ({len(svg)} bytes; {CANVAS_W}x{CANVAS_H})")
