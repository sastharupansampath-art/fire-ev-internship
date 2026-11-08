CMOS INVERTER OUTPUT FILES

1) Open a terminal in this folder.
2) Run transient switching simulation:
   ngspice cmos_inverter_transient.cir
3) Run DC voltage-transfer characteristic (VTC):
   ngspice cmos_inverter_vtc.cir

The transient file uses a 0-to-3 V pulse input. The DC file sweeps VIN from 0 to 3 V.
These are generic Level-1 MOSFET learning models, NOT SKY130A PDK simulations.
The Xschem drawing shown in the companion diagram is a reference circuit; the .cir files
are directly runnable in ngspice. The MOS terminal order is Drain, Gate, Source, Bulk.
