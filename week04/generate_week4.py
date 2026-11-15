#!/usr/bin/env python3
"""Generate Fire EV Week 4 SKY130A circuit netlists and report diagrams."""
from pathlib import Path
import re, subprocess, shutil, html, sys

BASE = Path.home() / "fire-ev-internship" / "week04"
CIR = BASE / "circuits"
DOC = BASE / "documentation"
DIAG = DOC / "circuit_diagrams"
RES = BASE / "results"
LOG = BASE / "logs"
for d in (CIR, DOC, DIAG, RES, LOG):
    d.mkdir(parents=True, exist_ok=True)

try:
    PDK = Path.home() / ".volare/volare/sky130/versions/c6d73a35f524070e85faff4a6a9eef49553ebc2b/sky130A"
except Exception as e:
    raise SystemExit(f"Cannot read active PDK from 'volare output': {e}")
MODEL_LIB = PDK / "libs.tech" / "ngspice" / "sky130.lib.spice"
if not MODEL_LIB.is_file():
    raise SystemExit(f"SKY130 model library missing: {MODEL_LIB}")

# Find actual model identifiers in the installed SKY130 transistor model files.
def find_model(kind):
    pattern = re.compile(r"^\s*\.model\s+(\S+)\s+(nmos|pmos)\b", re.I)
    want = "nmos" if kind == "nfet" else "pmos"
    roots = [PDK / "libs.ref" / "sky130_fd_pr" / "spice",
             PDK / "libs.tech" / "ngspice"]
    matches = []
    for root in roots:
        if not root.exists():
            continue
        for f in root.rglob("*.spice"):
            try:
                for line in f.read_text(errors="ignore").splitlines():
                    m = pattern.match(line)
                    if m and want == m.group(2).lower() and "01v8" in m.group(1) and "hvt" not in m.group(1) and "lvt" not in m.group(1):
                        matches.append(m.group(1))
            except OSError:
                pass
    if matches:
        # Prefer the plain standard-threshold core 1.8-V model if present.
        matches.sort(key=lambda x: ("nfet_01v8" not in x if kind == "nfet" else "pfet_01v8" not in x,
                                    "model.0" not in x, len(x)))
        return matches[0]
    # Common SKY130 model names; simulation log will show if this version differs.
    return "sky130_fd_pr__nfet_01v8__model.0" if kind == "nfet" else "sky130_fd_pr__pfet_01v8__model.0"

NMODEL = find_model("nfet")
PMODEL = find_model("pfet")
HEAD = f'''* Fire EV Internship - Week 4: Combinational CMOS Logic
* SKY130A PDK: {PDK}
* Typical process corner; educational circuit sizing, not sign-off design.
.lib "{MODEL_LIB}" tt
.param VDD=1.8
.param LCH=0.15u
.param WN=1u
.param WP=2u
* Model identifiers discovered from installed PDK:
* NMOS: {NMODEL}
* PMOS: {PMODEL}
'''
NAND_SUBCKT = f'''
.subckt NAND2 A B Y VP VN
MPA Y A VP VP {PMODEL} W={{WP}} L={{LCH}}
MPB Y B VP VP {PMODEL} W={{WP}} L={{LCH}}
MNA Y A N1 VN {NMODEL} W={{WN}} L={{LCH}}
MNB N1 B VN VN {NMODEL} W={{WN}} L={{LCH}}
.ends NAND2
'''
XOR_SUBCKT = '''
.subckt XOR2 A B Y VP VN
X1 A B N1 VP VN NAND2
X2 A N1 N2 VP VN NAND2
X3 B N1 N3 VP VN NAND2
X4 N2 N3 Y VP VN NAND2
.ends XOR2
'''

def emit(name, body, signals, note, stop="80n"):
    vectors = " ".join(f"v({s})" for s in signals)
    text = HEAD + f"* {note}\n" + body + f'''\n.control
set noaskquit
tran 100p {stop}
wrdata results/{name}_transient.dat {vectors}
.endc
.end
'''
    (CIR / f"{name}.cir").write_text(text)

# Day 20: NAND2 and NOR2 transistor-level circuits.
common_inputs = '''VDD vp 0 1.8
VA a 0 PULSE(0 1.8 0 100p 100p 10n 20n)
VB b 0 PULSE(0 1.8 0 100p 100p 20n 40n)
CLOAD y 0 10f
'''
emit("nand2", common_inputs + '''X1 a b y vp 0 NAND2
''' + NAND_SUBCKT, ["a", "b", "y"], "NAND2: PMOS parallel; NMOS series.")
emit("nor2", common_inputs + f'''MPA n1 a vp vp {PMODEL} W={{WP}} L={{LCH}}
MPB y b n1 vp {PMODEL} W={{WP}} L={{LCH}}
MNA y a 0 0 {NMODEL} W={{WN}} L={{LCH}}
MNB y b 0 0 {NMODEL} W={{WN}} L={{LCH}}
''', ["a", "b", "y"], "NOR2: PMOS series; NMOS parallel.")

# Day 21: complex CMOS gates; pull-up and pull-down are dual networks.
abc = '''VDD vp 0 1.8
VA a 0 PULSE(0 1.8 0 100p 100p 10n 20n)
VB b 0 PULSE(0 1.8 0 100p 100p 20n 40n)
VC c 0 PULSE(0 1.8 0 100p 100p 40n 80n)
CLOAD y 0 10f
'''
emit("aoi21", abc + f'''* Y = NOT((A AND B) OR C)
* PUN: (PMOS A parallel PMOS B) in series with PMOS C
MPA p1 a vp vp {PMODEL} W={{WP}} L={{LCH}}
MPB p1 b vp vp {PMODEL} W={{WP}} L={{LCH}}
MPC y c p1 vp {PMODEL} W={{WP}} L={{LCH}}
* PDN: (NMOS A series NMOS B) in parallel with NMOS C
MNA y a n1 0 {NMODEL} W={{WN}} L={{LCH}}
MNB n1 b 0 0 {NMODEL} W={{WN}} L={{LCH}}
MNC y c 0 0 {NMODEL} W={{WN}} L={{LCH}}
''', ["a", "b", "c", "y"], "AOI21: Y = NOT((A AND B) OR C).")
emit("oai21", abc + f'''* Y = NOT((A OR B) AND C)
* PUN: (PMOS A series PMOS B) in parallel with PMOS C
MPA p1 a vp vp {PMODEL} W={{WP}} L={{LCH}}
MPB y b p1 vp {PMODEL} W={{WP}} L={{LCH}}
MPC y c vp vp {PMODEL} W={{WP}} L={{LCH}}
* PDN: (NMOS A parallel NMOS B) in series with NMOS C
MNA y a n1 0 {NMODEL} W={{WN}} L={{LCH}}
MNB y b n1 0 {NMODEL} W={{WN}} L={{LCH}}
MNC n1 c 0 0 {NMODEL} W={{WN}} L={{LCH}}
''', ["a", "b", "c", "y"], "OAI21: Y = NOT((A OR B) AND C).")

# Day 22: transmission gate and mux. Complementary controls generated ideally.
emit("transmission_gate", f'''VDD vp 0 1.8
VIN din 0 PULSE(0 1.8 0 100p 100p 20n 40n)
VS s 0 PULSE(0 1.8 0 100p 100p 40n 80n)
Bsb sb 0 V=1.8-V(s)
MN out s din 0 {NMODEL} W={{WN}} L={{LCH}}
MP out sb din vp {PMODEL} W={{WP}} L={{LCH}}
CLOAD out 0 10f
''', ["din", "s", "out"], "Transmission gate: parallel NMOS/PMOS with complementary control.")
emit("mux2to1", f'''VDD vp 0 1.8
VA a 0 PULSE(0 1.8 0 100p 100p 10n 20n)
VB b 0 PULSE(1.8 0 0 100p 100p 10n 20n)
VS s 0 PULSE(0 1.8 0 100p 100p 40n 80n)
Bsb sb 0 V=1.8-V(s)
* A path enabled when S=0; B path enabled when S=1
MNA y sb a 0 {NMODEL} W={{WN}} L={{LCH}}
MPA y s a vp {PMODEL} W={{WP}} L={{LCH}}
MNB y s b 0 {NMODEL} W={{WN}} L={{LCH}}
MPB y sb b vp {PMODEL} W={{WP}} L={{LCH}}
CLOAD y 0 10f
''', ["a", "b", "s", "y"], "2:1 MUX: Y = (NOT S AND A) OR (S AND B).")

# Day 24: NAND-based full adder. Two XOR2s and NAND carry network.
emit("full_adder_1bit", f'''VDD vp 0 1.8
VA a 0 PULSE(0 1.8 0 100p 100p 10n 20n)
VB b 0 PULSE(0 1.8 0 100p 100p 20n 40n)
VC cin 0 PULSE(0 1.8 0 100p 100p 40n 80n)
XORAB a b x1 vp 0 XOR2
XORSUM x1 cin sum vp 0 XOR2
XAND1 a b nab vp 0 NAND2
XAND2 x1 cin nxc vp 0 NAND2
XCARRY nab nxc cout vp 0 NAND2
CLOADS sum 0 10f
CLOADC cout 0 10f
''' + NAND_SUBCKT + XOR_SUBCKT, ["a", "b", "cin", "sum", "cout"], "1-bit full adder: SUM=A XOR B XOR CIN; COUT=AB+CIN(A XOR B).")

# Truth tables for report.
truth = '''# Week 4 Truth Tables

## NAND2 and NOR2
| A | B | NAND2 | NOR2 |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

## AOI21 and OAI21
AOI21: Y = NOT((A AND B) OR C)  
OAI21: Y = NOT((A OR B) AND C)

## 2:1 MUX
Y = (NOT S AND A) OR (S AND B). S=0 selects A; S=1 selects B.

## 1-bit Full Adder
SUM = A XOR B XOR CIN  
COUT = A*B + CIN*(A XOR B)

| A | B | CIN | SUM | COUT |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |
'''
(DOC / "week4_truth_tables.md").write_text(truth)

# Report-ready vector topology diagrams. These are explanatory diagrams, not Xschem exports.
diagrams = {
    "nand2": ("CMOS NAND2", "Y = NOT(A · B)", ["PUN: PMOS A and PMOS B in parallel", "PDN: NMOS A and NMOS B in series"]),
    "nor2": ("CMOS NOR2", "Y = NOT(A + B)", ["PUN: PMOS A and PMOS B in series", "PDN: NMOS A and NMOS B in parallel"]),
    "aoi21": ("CMOS AOI21", "Y = NOT((A · B) + C)", ["PUN: (PMOS A || PMOS B) in series with PMOS C", "PDN: (NMOS A — NMOS B) in parallel with NMOS C"]),
    "oai21": ("CMOS OAI21", "Y = NOT((A + B) · C)", ["PUN: (PMOS A — PMOS B) in parallel with PMOS C", "PDN: (NMOS A || NMOS B) in series with NMOS C"]),
    "transmission_gate": ("CMOS Transmission Gate", "Parallel NMOS and PMOS pass devices", ["NMOS gate = S; passes strong LOW", "PMOS gate = NOT(S); passes strong HIGH"]),
    "mux2to1": ("2:1 Multiplexer", "Y = (NOT S · A) + (S · B)", ["TG-A enabled when S=0; connects A to Y", "TG-B enabled when S=1; connects B to Y"]),
    "full_adder_1bit": ("1-bit Full Adder", "SUM = A XOR B XOR CIN", ["COUT = A·B + CIN·(A XOR B)", "Three inputs: A, B, CIN; outputs: SUM, COUT"]),
}
for key, (title, eq, rows) in diagrams.items():
    row_svg = ""
    for idx, row in enumerate(rows):
        y = 270 + idx * 125
        row_svg += f'<rect x="100" y="{y}" width="1000" height="78" rx="12" fill="#eef2ff" stroke="#334155" stroke-width="2"/>'
        row_svg += f'<text x="600" y="{y+48}" text-anchor="middle" font-family="DejaVu Sans,Arial" font-size="23" fill="#172033">{html.escape(row)}</text>'
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="650" viewBox="0 0 1200 650">
<rect width="1200" height="650" fill="#ffffff"/>
<text x="60" y="72" font-family="DejaVu Sans,Arial" font-size="36" font-weight="bold" fill="#172033">{html.escape(title)}</text>
<text x="60" y="135" font-family="DejaVu Sans,Arial" font-size="27" fill="#2563eb">{html.escape(eq)}</text>
{row_svg}
<text x="60" y="610" font-family="DejaVu Sans,Arial" font-size="17" fill="#64748b">Fire EV Internship | Week 4 | Conceptual CMOS topology diagram</text>
</svg>'''
    (DIAG / f"{key}.svg").write_text(svg)

# Export PNG variants where a converter is installed.
for svg in DIAG.glob("*.svg"):
    png = svg.with_suffix(".png")
    if shutil.which("inkscape"):
        subprocess.run(["inkscape", str(svg), "--export-type=png", f"--export-filename={png}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    elif shutil.which("rsvg-convert"):
        with png.open("wb") as out:
            subprocess.run(["rsvg-convert", str(svg)], stdout=out, check=False)

readme = f'''# Fire EV Week 4 - Combinational CMOS Logic

PDK directory: `{PDK}`  
Model library: `{MODEL_LIB}`  
MOS model names found: NMOS `{NMODEL}`, PMOS `{PMODEL}`

## Files
- `circuits/`: seven transistor-level SPICE netlists.
- `documentation/circuit_diagrams/`: report-ready SVG topology diagrams (PNG copies created if a converter is installed).
- `documentation/week4_truth_tables.md`: equations and truth tables.
- `results/`: ngspice transient data, when simulations complete.

## Simulate
Run from `~/fire-ev-internship/week04`:
```bash
ngspice -b circuits/nand2.cir
ngspice -b circuits/nor2.cir
ngspice -b circuits/aoi21.cir
ngspice -b circuits/oai21.cir
ngspice -b circuits/transmission_gate.cir
ngspice -b circuits/mux2to1.cir
ngspice -b circuits/full_adder_1bit.cir
```
Inspect each ngspice log and result file. A generated netlist is not proof of successful simulation.

**Diagram note:** SVGs are explanatory CMOS topology diagrams for the report; they are not screenshots or Xschem-generated `.sch` files. Add actual Xschem schematic captures when they have been opened and checked.
'''
(BASE / "README.md").write_text(readme)

print("Week 4 generator completed.")
print(f"Active SKY130A directory: {PDK}")
print(f"Model library: {MODEL_LIB}")
print(f"Discovered models: NMOS={NMODEL}, PMOS={PMODEL}")
print("Netlists:")
for f in sorted(CIR.glob("*.cir")):
    print("  ", f.name)
print("Report diagrams:")
for f in sorted(DIAG.glob("*.svg")):
    print("  ", f.name)
print(f"Truth tables: {DOC / 'week4_truth_tables.md'}")
