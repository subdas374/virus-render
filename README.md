<div align="center">

```
██╗   ██╗██╗██████╗ ██╗   ██╗███████╗    ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗
██║   ██║██║██╔══██╗██║   ██║██╔════╝    ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║   ██║██║██████╔╝██║   ██║███████╗    ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚██╗ ██╔╝██║██╔══██╗██║   ██║╚════██║    ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
 ╚████╔╝ ██║██║  ██║╚██████╔╝███████║    ██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
  ╚═══╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```

### *A biologically accurate, animated SARS-CoV-2 visualisation built entirely with Python Turtle*

<br>

![Python](https://img.shields.io/badge/Python-3.7%2B-39ff6a?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a0f)
![Turtle](https://img.shields.io/badge/Turtle-stdlib-00cc66?style=for-the-badge&logoColor=white&labelColor=0a0a0f)
![License](https://img.shields.io/badge/License-MIT-17d468?style=for-the-badge&labelColor=0a0a0f)
![Status](https://img.shields.io/badge/Status-Active-39ff6a?style=for-the-badge&labelColor=0a0a0f)

<br>

```
         ·  ✦  ·          ·  ✦  ·          ·  ✦  ·
    ╔══════════════════════════════════════════════╗
    ║   No third-party libraries. No frameworks.  ║
    ║      Just Python, math, and curiosity.      ║
    ╚══════════════════════════════════════════════╝
         ·  ✦  ·          ·  ✦  ·          ·  ✦  ·
```

</div>

---

## ◈ What Is This?

**Virus Render** is an educational visualisation that draws a structurally accurate model of a **SARS-CoV-2 (coronavirus)** particle — layer by layer, in real time — using nothing but Python's built-in `turtle` graphics library and `math`.

Every layer corresponds to a real biological structure. Every radius is proportionally scaled. The animation draws from the **outside inward**, mirroring how electron microscopy reveals viral anatomy.

---

## ◈ Preview

```
                         ↑  ↑  ↑  ↑
                    ↗  spike proteins  ↖
                 ○──────────────────────○
               ○  · · matrix proteins · · ○
             ○  ╱╲  ╱╲  capsid shell  ╱╲  ╱╲  ○
            ○  ●●●●●●●●●●●●●●●●●●●●●●●●●●  ○
           ○  ●  ╰──────────────╯  RNA  ●  ○
            ○  ●●●●●●●●●●●●●●●●●●●●●●●●●●  ○
             ○  ╲╱  ╲╱  ╲╱  ╲╱  ╲╱  ╲╱  ○
               ○  · · · · · · · · · · ○
                 ○──────────────────○
                    ↘               ↙
```

> **Run it yourself** — the animation is best experienced live. Each structure builds on screen as you watch.

---

## ◈ Biological Accuracy

The render depicts **six distinct anatomical layers** of a real coronavirus, drawn in order from outermost to innermost:

| Layer | Structure | Biological Role |
|:-----:|-----------|-----------------|
| `1` | **Lipid Bilayer Envelope** | Outer membrane derived from the host cell |
| `2` | **Spike Proteins (S)** | 28 trimeric spikes — the "crown" that gives coronaviruses their name; primary vaccine target |
| `3` | **Matrix Proteins (M)** | Most abundant structural protein; anchors the envelope |
| `4` | **Capsid Shell** | Icosahedral protein coat protecting the genome |
| `5` | **Nucleocapsid Core** | Dense protein-RNA complex |
| `6` | **RNA Genome** | Single-stranded +RNA; drawn as a golden-angle spiral (~30 kb genome) |

---

## ◈ Features

- 🧬 &nbsp; **Biologically layered** — six distinct structures, each anatomically distinct
- 🎬 &nbsp; **Animated drawing** — `tracer(1, 18)` renders each line stroke visibly in real time
- 🔬 &nbsp; **Proportionally scaled** — radii are relative to each other, not arbitrary
- 🌀 &nbsp; **Golden-angle RNA spiral** — 37° rotation per step approximates natural nucleic acid packing
- 📐 &nbsp; **Icosahedral capsid** — alternating inner/outer vertices simulate triangulated facets
- 🖤 &nbsp; **Neon-on-black aesthetic** — high-contrast palette inspired by bio-imaging software
- 📦 &nbsp; **Zero dependencies** — only Python stdlib (`turtle`, `math`)

---

## ◈ Getting Started

### Prerequisites

```bash
python --version   # Python 3.7 or higher
```

Turtle is part of the Python standard library — **no pip install needed.**

> ⚠️ On some Linux systems you may need: `sudo apt install python3-tk`

---

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/virus-render.git

# Navigate into it
cd virus-render
```

### Run

```bash
python virus_render.py
```

The window will open and begin drawing automatically. **Click the window to close it** when done.

---

## ◈ Code Architecture

```
virus_render.py
│
├── Window Setup         — screen size, background, animation tracer
├── make_pen()           — factory function for turtle instances
│
├── Layer 1: Envelope    — two concentric circles (outer + inner membrane)
├── Layer 2: Spikes      — 28 stalks + filled bulbous heads (S-protein)
├── Layer 3: Capsid      — 18 triangulated facets (icosahedral shell)
├── Layer 4: Core        — filled dark circle (nucleocapsid)
├── Layer 5: RNA         — 400-step golden-angle outward spiral
├── Layer 6: Matrix      — 60 evenly-spaced protein dots
│
└── Labels               — title + colour-coded legend
```

---

## ◈ Animation Speed Tuning

Speed is controlled per-pen. Change the `speed=` argument in each `make_pen()` call:

| `speed` value | Effect |
|:---:|---|
| `1` | Very slow — meditative, good for demonstrations |
| `4–5` | Slow and deliberate — default for envelope & spikes |
| `6–8` | Medium — capsid facets, core |
| `10` | Fast — used for RNA (400 steps) |
| `0` | **Instant** — bypasses animation entirely |

Global step delay is set via:
```python
screen.tracer(1, 18)   # (steps_per_update, delay_in_ms)
```
Increase `18` → slower. Decrease → faster.

---

## ◈ Project Structure

```
virus-render/
├── virus_render.py     ← main script
├── README.md           ← you are here
└── LICENSE
```

---

## ◈ Roadmap

- [ ] Rotation animation (spin the virus slowly)
- [ ] Multiple virus particles at different scales
- [ ] Export render as SVG or PNG
- [ ] Side-by-side comparison: Influenza vs Coronavirus vs HIV
- [ ] Interactive mode — click a layer to highlight and label it

---

## ◈ Contributing

Contributions are welcome! If you're a biology student, data visualiser, or Python enthusiast:

1. Fork the repo
2. Create your branch: `git checkout -b feature/my-addition`
3. Commit your changes: `git commit -m 'Add HIV envelope render'`
4. Push to the branch: `git push origin feature/my-addition`
5. Open a Pull Request

---

## ◈ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## ◈ Acknowledgements

- Viral structure reference: [ViralZone — SARS-CoV-2](https://viralzone.expasy.org/9056)
- Python Turtle documentation: [docs.python.org/3/library/turtle](https://docs.python.org/3/library/turtle.html)
- Spike protein structure: [RCSB PDB 6VXX](https://www.rcsb.org/structure/6VXX)

---

<div align="center">

```
  ·  ·  ·  built with  ○  Python  ·  math  ·  curiosity  ○  ·  ·  ·
```

*"To understand a virus, first learn to draw one."*

<br>

![Made with Python](https://img.shields.io/badge/Made%20with-Python-39ff6a?style=flat-square&logo=python&logoColor=white&labelColor=0a0a0f)
![Bio + Code](https://img.shields.io/badge/Bio-%2B%20Code-00cc66?style=flat-square&labelColor=0a0a0f)

</div>
