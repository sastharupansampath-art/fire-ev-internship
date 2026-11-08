# Day 18 — CMOS Inverter Sizing

The sizing experiment keeps NMOS width fixed at 1 µm and changes PMOS width.

Test PMOS widths: 1 µm, 2 µm, 3 µm and 4 µm.

Keep the following constant:
- VDD = 1.8 V
- NMOS width = 1 µm
- Both channel lengths = 0.15 µm
- Load capacitance = 10 fF
- Input pulse and simulation time

Compare:
- VTC / switching threshold
- Output rise time
- Output fall time
- Propagation delays

A wider PMOS strengthens the pull-up network. Do not assume a width is optimal without comparing measured rise and fall times.
