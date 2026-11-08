# Day 17 — CMOS Inverter Power

## Static power
In a stable logic state, ideal CMOS has negligible direct DC current from VDD to ground. Real circuits still consume leakage power.

`P_static = VDD × I_leakage`

## Dynamic power
Charging and discharging load capacitance consumes dynamic power.

`P_dynamic = α × C_L × VDD² × f`

- α: switching activity factor
- C_L: load capacitance
- VDD: supply voltage
- f: switching frequency

## Short-circuit power
During an input transition, PMOS and NMOS can briefly conduct simultaneously, creating a temporary current path from VDD to ground.

## Reminder
The formula is a theoretical estimate. Actual power should be measured from the simulated supply current over a defined interval and with clearly stated switching activity and load.
