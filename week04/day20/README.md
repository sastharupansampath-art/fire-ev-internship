# Day 20 — CMOS NAND2 and NOR2

## Files
- `nand2.cir` — two-input CMOS NAND transient simulation netlist.
- `nor2.cir` — two-input CMOS NOR transient simulation netlist.

## Run in Ubuntu
Open a terminal in this directory and run:

```bash
ngspice nand2.cir
ngspice nor2.cir
```

Each simulation applies input pulse patterns that exercise all four input
combinations over an 80 ns transient run. The plot displays `A`, `B`, and
output `Y`.

## Expected truth table

| A | B | NAND Y | NOR Y |
|---|---|---|---|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

## Circuit topology
- NAND2: PMOS parallel; NMOS series.
- NOR2: PMOS series; NMOS parallel.

## Model limitation
These are educational Level-1 MOSFET model netlists for learning functional
behaviour. They are not SKY130A model simulations, extracted-layout results,
or Xschem-generated netlists. Run and verify them before recording practical
completion. For the internship submission, add your own Xschem schematics,
actual simulation screenshots, observations, and any required PDK-based
results.
