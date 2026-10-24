import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 6))

for filename, label in [
    ("diode_25C.txt", "25°C"),
    ("diode_75C.txt", "75°C")
]:
    data = np.loadtxt(filename)

    diode_voltage = data[:, 1]
    diode_current = data[:, 0] / 1000

    plt.plot(diode_voltage, diode_current * 1000, label=label)

plt.xlabel("Diode Voltage (V)")
plt.ylabel("Diode Current (mA)")
plt.title("Diode I-V Characteristics at Two Temperatures")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("diode_iv_comparison.png", dpi=300)
plt.show()
