# Fire EV Week 4 - Combinational CMOS Logic

PDK directory: `/home/sastha-rupan-s/.volare/volare/sky130/versions/c6d73a35f524070e85faff4a6a9eef49553ebc2b/sky130A`  
Model library: `/home/sastha-rupan-s/.volare/volare/sky130/versions/c6d73a35f524070e85faff4a6a9eef49553ebc2b/sky130A/libs.tech/ngspice/sky130.lib.spice`  
MOS model names found: NMOS `sky130_fd_pr__nfet_01v8__model.0`, PMOS `sky130_fd_pr__pfet_01v8__model.0`

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
