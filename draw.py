"""Draw the 26 November 2026 world-news front page (entry.png).

A flat, newspaper-style infographic drawn with Pillow: six verified
stories from Thursday 26 November 2026, each with its own small
illustration, headline and caption, plus a footer strip of three more
stories. Every fact was checked against BBC / Reuters / AP reporting
dated 26 November 2026 (see SOURCES in README.md). Run:

    python3 draw.py            # writes entry.png (1024x1024, < 1 MiB)
"""

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (17, 17, 17)
RED = (178, 34, 34)
NAVY = (30, 58, 95)
TEAL = (14, 116, 110)
GOLD = (176, 124, 18)
SLATE = (71, 85, 105)

FDIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(f"{FDIR}/{name}", size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def panel(draw, x, y, w, h, tag, tag_color, headline, body, art):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill=(255, 255, 255), outline=(203, 196, 178), width=2)
    # tag chip
    draw.rounded_rectangle([x + 14, y + 12, x + 14 + draw.textlength(tag, font=SANS_B(15)) + 16, y + 36],
                           radius=5, fill=tag_color)
    draw.text((x + 22, y + 15), tag, font=SANS_B(15), fill=(255, 255, 255))
    # illustration on the right
    art(draw, x + w - 158, y + 48, 144, 120)
    # headline + body on the left
    tx, tw = x + 14, w - 186
    lines = wrap(draw, headline, SANS_B(23), tw)
    yy = y + 48
    for ln in lines[:3]:
        draw.text((tx, yy), ln, font=SANS_B(23), fill=INK)
        yy += 27
    yy += 4
    for ln in wrap(draw, body, SANS(16), tw)[:5]:
        draw.text((tx, yy), ln, font=SANS(16), fill=(38, 38, 38))
        yy += 20


# --- small flat illustrations (each fits a 144x120 box) ---
def art_parade(d, x, y, w, h):
    d.ellipse([x + 8, y + 6, x + 52, y + 52], fill=(217, 119, 6), outline=INK, width=2)
    d.ellipse([x + 56, y + 16, x + 96, y + 58], fill=RED, outline=INK, width=2)
    d.ellipse([x + 100, y + 4, x + 138, y + 46], fill=NAVY, outline=INK, width=2)
    for cx in (30, 76, 119):
        d.line([x + cx, y + 52, x + cx, y + 78], fill=INK, width=2)
    d.ellipse([x + 18, y + 78, x + 126, y + 104], fill=(148, 163, 184))
    d.text((x + 44, y + 82), "100th", font=SANS_B(17), fill=(255, 255, 255))


def art_store(d, x, y, w, h):
    d.rectangle([x + 10, y + 30, x + 134, y + 108], fill=(226, 232, 240), outline=INK, width=2)
    d.rectangle([x + 10, y + 30, x + 134, y + 52], fill=TEAL)
    d.text((x + 28, y + 33), "SUPERMARKET", font=SANS_B(13), fill=(255, 255, 255))
    d.rectangle([x + 58, y + 66, x + 86, y + 108], fill=NAVY)
    d.text((x + 90, y + 84), "17 h", font=SANS_B(18), fill=RED)


def art_chart(d, x, y, w, h):
    d.line([x + 14, y + 104, x + 134, y + 104], fill=INK, width=2)
    d.line([x + 14, y + 104, x + 14, y + 34], fill=INK, width=2)
    for i, bh in enumerate((26, 44, 62)):
        bx = x + 28 + i * 38
        d.rectangle([bx, y + 104 - bh, bx + 26, y + 104], fill=RED if i == 2 else (148, 163, 184))
    d.text((x + 20, y + 6), "~500,000", font=SANS_B(18), fill=RED)


def art_rocket(d, x, y, w, h):
    d.ellipse([x + 78, y + 62, x + 138, y + 92], outline=GOLD, width=3)
    d.ellipse([x + 92, y + 68, x + 124, y + 86], fill=(253, 224, 71))
    d.polygon([(x + 40, y + 20), (x + 58, y + 20), (x + 58, y + 78), (x + 40, y + 78)], fill=(226, 232, 240), outline=INK)
    d.polygon([(x + 40, y + 20), (x + 49, y + 2), (x + 58, y + 20)], fill=RED)
    d.ellipse([x + 43, y + 34, x + 55, y + 46], fill=NAVY)
    d.polygon([(x + 40, y + 78), (x + 30, y + 96), (x + 40, y + 88)], fill=(249, 115, 22))
    d.polygon([(x + 58, y + 78), (x + 68, y + 96), (x + 58, y + 88)], fill=(249, 115, 22))
    d.text((x + 8, y + 100), "TIANGONG", font=SANS_B(13), fill=NAVY)


def art_dome(d, x, y, w, h):
    d.rectangle([x + 16, y + 88, x + 128, y + 106], fill=(203, 196, 178))
    for i in range(5):
        d.rectangle([x + 22 + i * 22, y + 62, x + 36 + i * 22, y + 88], fill=NAVY, outline=INK, width=1)
    d.pieslice([x + 34, y + 18, x + 110, y + 66], 180, 360, fill=NAVY)
    d.rectangle([x + 68, y + 6, x + 76, y + 20], fill=GOLD)
    d.text((x + 52, y + 88), "77", font=SANS_B(15), fill=INK)


def art_factory(d, x, y, w, h):
    d.rectangle([x + 10, y + 48, x + 134, y + 106], fill=(226, 232, 240), outline=INK, width=2)
    d.polygon([(x + 10, y + 48), (x + 34, y + 30), (x + 58, y + 48)], fill=TEAL)
    d.polygon([(x + 58, y + 48), (x + 82, y + 30), (x + 106, y + 48)], fill=TEAL)
    d.rectangle([x + 112, y + 18, x + 126, y + 48], fill=SLATE)
    d.line([x + 24, y + 62, x + 62, y + 24], fill=RED, width=4)
    d.polygon([(x + 62, y + 24), (x + 46, y + 26), (x + 60, y + 40)], fill=RED)
    d.text((x + 66, y + 66), "+36%", font=SANS_B(22), fill=RED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.line([24, 18, 1000, 18], fill=INK, width=4)
    title = "THE WORLD IN ONE DAY"
    d.text(((W - d.textlength(title, font=SERIF_B(52))) / 2, 30),
           title, font=SERIF_B(52), fill=INK)
    date = "THURSDAY, 26 NOVEMBER 2026"
    d.text(((W - d.textlength(date, font=SANS_B(30))) / 2, 96),
           date, font=SANS_B(30), fill=RED)
    sub = "Six stories that defined the day  •  the Americas  •  Europe  •  Asia  •  Space"
    d.text(((W - d.textlength(sub, font=SANS(18))) / 2, 134),
           sub, font=SANS(18), fill=SLATE)
    d.line([24, 160, 1000, 160], fill=INK, width=2)

    panels = [
        ("USA", RED, "THANKSGIVING IN A STORM",
         "The 100th Macy's parade — 100 inflatables — marches in New York as a coastal storm brings 40–45 mph gusts and 1–2 in of rain. 81.5m Americans travel for the holiday.",
         art_parade),
        ("COLOMBIA", TEAL, "HOSTAGES FREED AFTER 17 HOURS",
         "Police storm an Éxito supermarket in Cartagena, freeing about 20 shoppers and staff. One gunman is killed in the raid.",
         art_store),
        ("UKRAINE WAR", NAVY, "RUSSIA'S WAR DEAD: ≈500,000",
         "Moscow's own figures show almost half a million Russians lost in Ukraine, the BBC reports — the war's toll laid bare in leaked data.",
         art_chart),
        ("SPACE", GOLD, "PAKISTAN'S FIRST ASTRONAUT",
         "Shenzhou-24 lifts off with Muhammad Zeeshan Ali, the first foreigner aboard China's Tiangong station. Crew of 3; launch 08:18 Beijing time.",
         art_rocket),
        ("INDIA", (120, 53, 15), "77 YEARS OF THE CONSTITUTION",
         "India marks Constitution Day — adopted 26 Nov 1949. Delhi also pledges a ₹15,000-crore package for Nepal after Modi–Shah talks.",
         art_dome),
        ("BANGLADESH", (21, 101, 52), "GARMENT PAY RISES 36%",
         "Bangladesh raises the minimum wage for garment workers by 36% after weeks of protests shut factories across the industry.",
         art_factory),
    ]
    px, py, pw, ph, gap = 24, 176, 476, 228, 16
    for i, (tag, color, head, body, art) in enumerate(panels):
        x = px + (i % 2) * (pw + gap)
        y = py + (i // 2) * (ph + gap)
        panel(d, x, y, pw, ph, tag, color, head, body, art)

    # --- footer strip ---
    fy = 176 + 3 * ph + 2 * 16 + 14
    d.rounded_rectangle([24, fy, 1000, fy + 78], radius=8, fill=NAVY)
    d.text((40, fy + 10), "ALSO TODAY", font=SANS_B(16), fill=(253, 224, 71))
    foot = ("NATO sends AWACS jets to Poland after 3 Russian missiles land there  •  "
            "Nvidia brings back Jensen Huang as CEO  •  6 killed, incl. 2 children, "
            "in a plane crash off Mississippi")
    for j, ln in enumerate(wrap(d, foot, SANS(16), 944)):
        d.text((40, fy + 32 + j * 20), ln, font=SANS(16), fill=(255, 255, 255))
    src = "Sources: BBC · Reuters · AP — as reported on 26 November 2026"
    d.text(((W - d.textlength(src, font=SANS(14))) / 2, fy + 82),
           src, font=SANS(14), fill=SLATE)

    out = Path(__file__).resolve().parent / "entry.png"
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} {out.stat().st_size} bytes")


if __name__ == "__main__":
    main()
