# makefun-news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/reyzn02/makefun-news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/reyzn02/makefun-news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Sum up 26 November's world news in one image: a newspaper front-page infographic for Thursday, 26 November 2026. Six stories, each with its own flat illustration, headline and caption: the 100th Macy's Thanksgiving Day Parade marching through a coastal storm in New York (100 inflatables, 40–45 mph gusts, 81.5m Americans travelling); police in Cartagena freeing about 20 hostages after a 17-hour supermarket siege; Russia's own figures showing almost 500,000 dead in the Ukraine war; China's Shenzhou-24 carrying Pakistan's Muhammad Zeeshan Ali, the first foreign astronaut aboard Tiangong; India marking 77 years of its Constitution and pledging a ₹15,000-crore package for Nepal; and Bangladesh raising garment workers' minimum wage by 36%. A footer strip adds NATO sending AWACS jets to Poland after three Russian missiles landed there, Nvidia bringing back Jensen Huang as CEO, and six killed (including two children) in a plane crash off Mississippi. The program (Python 3, standard library only, no network) copies the image to the output directory as `entry.png`; `draw.py` draws the image from scratch.

## Sources (all as reported on 26 November 2026)

- BBC: Russia's own figures show almost 500,000 lost in the Ukraine war; Colombian police storm supermarket to free ~20 held hostage for 17 hours; Shenzhou-24 carries Pakistan's first astronaut; two children among six dead in a plane crash off Mississippi.
- Reuters: NATO to send AWACS aircraft to Poland after three missiles land; Trump rewrites the lame-duck rules with his intervention on Nvidia CEO Jensen Huang; Bangladesh garment workers win a 36% minimum-wage rise.
- AP / TIME / People: 100th Macy's Thanksgiving Day Parade, 26 November, New York; high-wind watch, gusts 40–45 mph, 1–2 in of rain; AAA: 81.5m Americans travelling 24–30 November.
- India: Constitution Day, 26 November (Constitution adopted 26 Nov 1949, 77 years); ₹15,000-crore Nepal package announced by PM Modi after talks with PM Balendra Shah.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To redraw the image from scratch:

```sh
python3 draw.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
