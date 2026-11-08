v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {VIN}
E {}
P 4 1 -80 0 {}
N 20 100 30 -30 {
lab=#net1}
N 60 70 70 0 {
lab=#net2}
N 60 130 90 130 {
lab=GND}
N 90 110 90 130 {
lab=GND}
N 60 100 90 110 {
lab=GND}
N 70 -60 120 -60 {
lab=VDD}
N 120 -60 120 -30 {
lab=VDD}
N 70 -30 120 -30 {
lab=VDD}
N 70 -70 70 -60 {
lab=VDD}
N 60 130 60 160 {
lab=GND}
N -70 50 30 50 {
lab=VIN}
N 170 40 170 50 {
lab=VOUT}
N 70 40 170 50 {
lab=VOUT}
N 60 40 70 40 {
lab=VOUT}
C {pmos4.sym} 50 -30 0 0 {name=M1 model=pmos w=5u l=0.18u del=0 m=1}
C {nmos4.sym} 40 100 0 0 {name=M2 model=nmos w=5u l=0.18u del=0 m=1}
C {vdd.sym} 70 -70 0 0 {name=l1 lab=VDD}
C {gnd.sym} 60 160 0 0 {name=l2 lab=GND}
C {lab_wire.sym} -70 50 0 0 {name=p1 sig_type=std_logic lab=VIN
}
C {lab_wire.sym} 170 40 0 0 {name=p2 sig_type=std_logic lab=VOUT
}
C {vsource.sym} -70 80 0 0 {name=V1 value="PULSE(0 3 0 1n 1n 5u 10u)" savecurrent=false}
C {gnd.sym} -70 110 0 0 {name=l3 lab=GND}
