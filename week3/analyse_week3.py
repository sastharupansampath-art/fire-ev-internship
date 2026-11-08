from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
PLOTS = ROOT / "plots"
PLOTS.mkdir(exist_ok=True)

def load_spice(path):
    arr = np.loadtxt(path, skiprows=1)
    if arr.ndim != 2 or arr.shape[1] < 3:
        raise ValueError(f"Unexpected data format in {path}: {arr.shape}")
    return arr

# Day 15: VTC
vtc = load_spice(DATA / "vtc.dat")
vin, vout = vtc[:, 1], vtc[:, 2]
plt.figure()
plt.plot(vin, vout)
plt.xlabel("Input voltage (V)")
plt.ylabel("Output voltage (V)")
plt.title("CMOS inverter voltage transfer characteristic")
plt.grid(True)
plt.tight_layout()
plt.savefig(PLOTS / "inverter_vtc.png", dpi=180)
plt.close()

idx = np.argmin(np.abs(vin - vout))
vm = (vin[idx] + vout[idx]) / 2

# Day 16: transient waveform
tr = load_spice(DATA / "transient.dat")
t, vi, vo = tr[:, 0], tr[:, 1], tr[:, 2]
plt.figure()
plt.plot(t * 1e9, vi, label="Input")
plt.plot(t * 1e9, vo, label="Output")
plt.xlabel("Time (ns)")
plt.ylabel("Voltage (V)")
plt.title("CMOS inverter transient response")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(PLOTS / "inverter_transient.png", dpi=180)
plt.close()

def crossing_time(t, y, level, rising, after=0.0):
    start = np.searchsorted(t, after)
    tt, yy = t[start:], y[start:]
    if rising:
        ix = np.where((yy[:-1] < level) & (yy[1:] >= level))[0]
    else:
        ix = np.where((yy[:-1] > level) & (yy[1:] <= level))[0]
    if not len(ix):
        return None
    i = ix[0] + start
    return t[i] + (level-y[i])*(t[i+1]-t[i])/(y[i+1]-y[i])

v10, v50, v90 = 0.18, 0.9, 1.62
# Output rise/fall crossings (first available transition)
t10r = crossing_time(t, vo, v10, True, after=1e-9)
t90r = crossing_time(t, vo, v90, True, after=1e-9)
t90f = crossing_time(t, vo, v90, False, after=6e-9)
t10f = crossing_time(t, vo, v10, False, after=6e-9)

# Input rising edge causes output falling; input falling causes output rising.
tir = crossing_time(t, vi, v50, True, after=0.5e-9)
tif = crossing_time(t, vi, v50, False, after=5e-9)
tof = crossing_time(t, vo, v50, False, after=0.5e-9)
tor = crossing_time(t, vo, v50, True, after=5e-9)

lines = [
    f"Approximate V_M (Vin = Vout): {vm:.5f} V",
    f"Rise time (10%-90%): {(t90r-t10r)*1e9:.5f} ns" if t10r is not None and t90r is not None else "Rise time: crossing not found",
    f"Fall time (90%-10%): {(t10f-t90f)*1e9:.5f} ns" if t90f is not None and t10f is not None else "Fall time: crossing not found",
    f"t_PHL (input rise to output fall): {(tof-tir)*1e9:.5f} ns" if tir is not None and tof is not None else "t_PHL: crossing not found",
    f"t_PLH (input fall to output rise): {(tor-tif)*1e9:.5f} ns" if tif is not None and tor is not None else "t_PLH: crossing not found",
]
(ROOT / "measurement_results.txt").write_text("\n".join(lines) + "\n")
print("\n".join(lines))

# Day 18: sizing waveform comparison
plt.figure()
for width in ["1u", "2u", "3u", "4u"]:
    d = load_spice(DATA / f"size_{width}.dat")
    plt.plot(d[:, 0] * 1e9, d[:, 2], label=f"PMOS W={width}")
plt.xlabel("Time (ns)")
plt.ylabel("Output voltage (V)")
plt.title("Effect of PMOS width on inverter output")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(PLOTS / "sizing_comparison.png", dpi=180)
plt.close()
print("Graphs saved in plots/")
