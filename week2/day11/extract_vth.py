import numpy as np

# Reference current: 1 µA per µm of transistor width
IREF_PER_UM = 1e-6

devices = [
    ("NMOS", "data/nmos_transfer.csv", 1.0),
    ("PMOS", "data/pmos_transfer.csv", 2.0)
]

for name, filename, width_um in devices:
    data = np.loadtxt(filename, delimiter=",", skiprows=1)
    voltage = data[:, 0]
    current = data[:, 1]

    reference = IREF_PER_UM * width_um

    if not np.all(np.diff(voltage) > 0):
        raise ValueError(f"{name}: voltage values are not increasing")

    if reference < current.min() or reference > current.max():
        print(f"{name}: reference current outside measured range")
        continue

    crossing = np.where(current >= reference)[0][0]

    if crossing == 0:
        vth = voltage[0]
    else:
        vth = np.interp(
            reference,
            current[crossing-1:crossing+1],
            voltage[crossing-1:crossing+1]
        )

    print(f"\n{name}")
    print(f"Width: {width_um:.1f} µm")
    print(f"Reference current: {reference*1e6:.2f} µA")
    print(f"Extracted threshold magnitude: {vth:.4f} V")

    if name == "PMOS":
        print(f"Signed Vth estimate: {-vth:.4f} V")
