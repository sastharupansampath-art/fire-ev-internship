import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("rc_response.txt")

time = data[:, 0]
voltage = data[:, 1]

plt.plot(time * 1000, voltage)
plt.xlabel("Time (ms)")
plt.ylabel("Capacitor Voltage (V)")
plt.title("RC Circuit Transient Response")
plt.grid(True)
plt.tight_layout()
plt.savefig("rc_transient.png", dpi=300)
plt.show()
