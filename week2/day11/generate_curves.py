import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt

PDK = os.path.expanduser("~/.volare/sky130A")
MODEL = os.path.join(PDK, "libs.tech/ngspice/sky130.lib.spice")

os.makedirs("data", exist_ok=True)
os.makedirs("plots", exist_ok=True)


def simulate(name, netlist_name, netlist_text, data_file):
    # Write the SPICE circuit
    with open(netlist_name, "w") as f:
        f.write(netlist_text)

    # Execute ngspice
    result = subprocess.run(
        ["ngspice", "-b", netlist_name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"\nFAILED: {name}")
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(1)

    # Check the actual data file
    if not os.path.isfile(data_file) or os.path.getsize(data_file) == 0:
        print(f"\nDATA FILE NOT GENERATED: {data_file}")
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(1)

    data = np.loadtxt(data_file)

    if data.ndim != 2 or data.shape[1] < 2:
        raise ValueError(f"Unexpected data format: {data_file}")

    print(f"Completed: {name} ({len(data)} points)")
    return data


# ==========================================
# 1. NMOS OUTPUT CHARACTERISTICS
# ==========================================

nmos_output = []

for vg in [0.6, 0.8, 1.0, 1.2, 1.5, 1.8]:

    tag = str(vg).replace(".", "p")
    dat = f"data/nmos_output_{tag}.dat"

    circuit = f"""
* SKY130A NMOS output characteristics
.lib "{MODEL}" tt
.option scale=1e-6

VDS d 0 0
VGS g 0 {vg}
XM1 d g 0 0 sky130_fd_pr__nfet_01v8 L=0.15 W=1

.control
set wr_singlescale
dc VDS 0 1.8 0.02
wrdata {dat} -i(VDS)
quit
.endc
.end
"""

    data = simulate(
        f"NMOS output VGS={vg}V",
        f"nmos_output_{tag}.cir",
        circuit,
        dat
    )

    voltage = data[:, 0]
    current = np.abs(data[:, -1])

    nmos_output.append((voltage, current, vg))

    np.savetxt(
        f"data/nmos_output_{tag}.csv",
        np.column_stack((voltage, current)),
        delimiter=",",
        header="VDS_V,ID_A",
        comments=""
    )


# ==========================================
# 2. NMOS TRANSFER CHARACTERISTICS
# ==========================================

dat = "data/nmos_transfer.dat"

circuit = f"""
* SKY130A NMOS transfer characteristics
.lib "{MODEL}" tt
.option scale=1e-6

VDS d 0 1.8
VGS g 0 0
XM1 d g 0 0 sky130_fd_pr__nfet_01v8 L=0.15 W=1

.control
set wr_singlescale
dc VGS 0 1.8 0.01
wrdata {dat} -i(VDS)
quit
.endc
.end
"""

data = simulate("NMOS transfer", "nmos_transfer.cir", circuit, dat)

nmos_vgs = data[:, 0]
nmos_id = np.abs(data[:, -1])

np.savetxt(
    "data/nmos_transfer.csv",
    np.column_stack((nmos_vgs, nmos_id)),
    delimiter=",",
    header="VGS_V,ID_A",
    comments=""
)


# ==========================================
# 3. PMOS OUTPUT CHARACTERISTICS
# ==========================================

pmos_output = []

for vsg in [0.6, 0.8, 1.0, 1.2, 1.5, 1.8]:

    tag = str(vsg).replace(".", "p")
    dat = f"data/pmos_output_{tag}.dat"

    circuit = f"""
* SKY130A PMOS output characteristics
.lib "{MODEL}" tt
.option scale=1e-6

VDD s 0 1.8
VSD s d 0
VSG s g {vsg}
XM1 d g s s sky130_fd_pr__pfet_01v8 L=0.15 W=2

.control
set wr_singlescale
dc VSD 0 1.8 0.02
wrdata {dat} -i(VSD)
quit
.endc
.end
"""

    data = simulate(
        f"PMOS output VSG={vsg}V",
        f"pmos_output_{tag}.cir",
        circuit,
        dat
    )

    voltage = data[:, 0]
    current = np.abs(data[:, -1])

    pmos_output.append((voltage, current, vsg))

    np.savetxt(
        f"data/pmos_output_{tag}.csv",
        np.column_stack((voltage, current)),
        delimiter=",",
        header="VSD_V,ID_A",
        comments=""
    )


# ==========================================
# 4. PMOS TRANSFER CHARACTERISTICS
# ==========================================

dat = "data/pmos_transfer.dat"

circuit = f"""
* SKY130A PMOS transfer characteristics
.lib "{MODEL}" tt
.option scale=1e-6

VDD s 0 1.8
VSD s d 1.8
VSG s g 0
XM1 d g s s sky130_fd_pr__pfet_01v8 L=0.15 W=2

.control
set wr_singlescale
dc VSG 0 1.8 0.01
wrdata {dat} -i(VSD)
quit
.endc
.end
"""

data = simulate("PMOS transfer", "pmos_transfer.cir", circuit, dat)

pmos_vsg = data[:, 0]
pmos_id = np.abs(data[:, -1])

np.savetxt(
    "data/pmos_transfer.csv",
    np.column_stack((pmos_vsg, pmos_id)),
    delimiter=",",
    header="VSG_V,ID_A",
    comments=""
)


# ==========================================
# 5. GENERATE FOUR GRAPHS
# ==========================================

# NMOS output
plt.figure(figsize=(9, 6))

for voltage, current, vg in nmos_output:
    plt.plot(voltage, current * 1e6, label=f"VGS = {vg} V")

plt.xlabel("VDS (V)")
plt.ylabel("Drain Current (µA)")
plt.title("SKY130A NMOS Output Characteristics")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots/nmos_output.png", dpi=300)
plt.close()


# NMOS transfer
plt.figure(figsize=(9, 6))
plt.plot(nmos_vgs, nmos_id * 1e6)

plt.xlabel("VGS (V)")
plt.ylabel("Drain Current (µA)")
plt.title("SKY130A NMOS Transfer Characteristics")
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/nmos_transfer.png", dpi=300)
plt.close()


# PMOS output
plt.figure(figsize=(9, 6))

for voltage, current, vsg in pmos_output:
    plt.plot(voltage, current * 1e6, label=f"VSG = {vsg} V")

plt.xlabel("VSD (V)")
plt.ylabel("Drain Current Magnitude (µA)")
plt.title("SKY130A PMOS Output Characteristics")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plots/pmos_output.png", dpi=300)
plt.close()


# PMOS transfer
plt.figure(figsize=(9, 6))
plt.plot(pmos_vsg, pmos_id * 1e6)

plt.xlabel("VSG (V)")
plt.ylabel("Drain Current Magnitude (µA)")
plt.title("SKY130A PMOS Transfer Characteristics")
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/pmos_transfer.png", dpi=300)
plt.close()


print("\n====================================")
print("ALL FOUR SIMULATIONS COMPLETED")
print("====================================")

for filename in sorted(os.listdir("plots")):
    print("Graph:", filename)

print("\nCSV data files:")
for filename in sorted(os.listdir("data")):
    if filename.endswith(".csv"):
        print(filename)
