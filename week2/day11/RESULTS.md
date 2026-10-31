# Week 2 - Day 11: SKY130A MOSFET Simulation

## Objective
Simulate NMOS and PMOS transistor characteristics using
ngspice and the SKY130A process design kit.

## Simulation Environment
- Operating system: Ubuntu 24.04 LTS
- Simulator: ngspice
- PDK: SKY130A
- Model corner: Typical (TT)
- Temperature: 27 C
- NMOS: sky130_fd_pr__nfet_01v8
- PMOS: sky130_fd_pr__pfet_01v8

## Transistor Dimensions

| Parameter | NMOS | PMOS |
|---|---:|---:|
| Channel length | 0.15 um | 0.15 um |
| Channel width | 1 um | 2 um |

## Threshold Voltage Extraction

Constant-current method:
Reference current = 1 uA per um of channel width.

| Parameter | NMOS | PMOS |
|---|---:|---:|
| Reference current | 1 uA | 2 uA |
| Threshold magnitude | 0.6169 V | 0.5897 V |
| Signed threshold estimate | +0.6169 V | -0.5897 V |

These are extracted constant-current estimates, not necessarily
the compact model's internal threshold parameters.

## Generated Characteristics

1. NMOS output characteristics (ID vs VDS)
2. NMOS transfer characteristics (ID vs VGS)
3. PMOS output characteristics (ID magnitude vs VSD)
4. PMOS transfer characteristics (ID magnitude vs VSG)

## Observations

- NMOS drain current increases with gate-source voltage.
- PMOS drain current magnitude increases with source-gate voltage.
- Both devices show linear and saturation behaviour.
- The saturation curves have a non-zero slope due to
  non-ideal transistor effects.

## Tools Used
- ngspice
- SKY130A PDK
- Python
- NumPy
- Matplotlib
