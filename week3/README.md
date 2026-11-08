# Week 3 — Days 15–18: CMOS Inverter

This package contains starter files for the four tasks:
- Day 15: CMOS inverter DC sweep / VTC
- Day 16: transient response, rise/fall time and propagation delay
- Day 17: CMOS power concepts and a calculation helper
- Day 18: PMOS sizing comparison

## Important
The circuit netlists use simple Level-1 MOSFET models so they can run independently of a PDK installation. They are learning/testbench models, NOT SKY130A sign-off results. For the Fire EV deliverable, rerun using the approved SKY130A model files and the exact model/corner settings from your roadmap.

## Requirements on Ubuntu
```bash
sudo apt update
sudo apt install -y ngspice xschem python3-numpy python3-matplotlib
```

## Run all simulations
From this folder:
```bash
bash run_all.sh
```

Then open the graphs:
```bash
xdg-open plots/inverter_vtc.png
xdg-open plots/inverter_transient.png
xdg-open plots/sizing_comparison.png
```

## xschem
Open the provided `day15/cmos_inverter.sch` with:
```bash
xschem day15/cmos_inverter.sch
```
The schematic is a starting point for visual inspection/editing. The `.cir` files are the independent simulation netlists used by `run_all.sh`.

## What is not pre-completed
This environment did not have ngspice or xschem installed, so no SPICE run was claimed as completed and no fabricated simulation plots/results are included. Run `bash run_all.sh` on your Ubuntu laptop to generate the actual data and graphs.
