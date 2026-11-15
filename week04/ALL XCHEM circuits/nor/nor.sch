v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
N -80 80 -80 140 {lab=Y}
N -80 80 160 80 {lab=Y}
N 160 80 160 130 {lab=Y}
N 40 -120 40 -60 {lab=#net1}
N 40 0 40 80 {lab=Y}
N -80 200 -80 280 {lab=GND}
N -80 280 160 280 {lab=GND}
N 160 200 160 280 {lab=GND}
N 40 280 40 320 {lab=GND}
N -200 -150 -0 -150 {lab=A}
N -200 -150 -200 -30 {lab=A}
N 80 -30 240 -30 {lab=B}
N 240 -30 300 -30 {lab=B}
N -200 -30 -200 170 {lab=A}
N -200 170 -120 170 {lab=A}
N 40 40 180 40 {lab=Y}
N -340 -120 -340 -80 {lab=GND}
N -550 -120 -550 -80 {lab=GND}
N -550 20 -550 60 {lab=GND}
N 40 -210 40 -180 {lab=VDD}
N 160 130 160 140 {lab=Y}
N 200 170 300 170 {lab=B}
N 180 40 340 40 {lab=Y}
C {sky130_fd_pr/nfet3_01v8.sym} 180 170 0 1 {name=M1
W=1
L=0.15
body=GND
nf=1
mult=1
ad="expr('int((@nf + 1)/2) * @W / @nf * 0.29')"
pd="expr('2*int((@nf + 1)/2) * (@W / @nf + 0.29)')"
as="expr('int((@nf + 2)/2) * @W / @nf * 0.29')"
ps="expr('2*int((@nf + 2)/2) * (@W / @nf + 0.29)')"
nrd="expr('0.29 / @W ')" nrs="expr('0.29 / @W ')"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/nfet3_01v8.sym} -100 170 0 0 {name=M2
W=1
L=0.15
body=GND
nf=1
mult=1
ad="expr('int((@nf + 1)/2) * @W / @nf * 0.29')"
pd="expr('2*int((@nf + 1)/2) * (@W / @nf + 0.29)')"
as="expr('int((@nf + 2)/2) * @W / @nf * 0.29')"
ps="expr('2*int((@nf + 2)/2) * (@W / @nf + 0.29)')"
nrd="expr('0.29 / @W ')" nrs="expr('0.29 / @W ')"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {gnd.sym} 40 320 0 0 {name=l1 lab=GND}
C {lab_pin.sym} 40 -210 0 0 {name=p1 sig_type=std_logic lab=VDD}
C {ipin.sym} -200 -30 0 0 {name=p2 lab=A}
C {ipin.sym} 300 -30 0 1 {name=p3 lab=B}
C {opin.sym} 340 40 0 0 {name=p4 lab=Y}
C {lab_pin.sym} -340 -180 0 0 {name=p5 sig_type=std_logic lab=VDD}
C {lab_pin.sym} -550 -40 0 0 {name=p6 sig_type=std_logic lab=A}
C {lab_pin.sym} -550 -180 0 0 {name=p7 sig_type=std_logic lab=B}
C {vsource.sym} -340 -150 0 0 {name=VDD value=1.8 savecurrent=false}
C {vsource.sym} -550 -10 0 0 {name=VA value="PULSE(0 1.8 0n 100p 100p 10n 20n)" savecurrent=false}
C {vsource.sym} -550 -150 0 0 {name=VB value="PULSE(0 1.8 0n 100p 100p 20n 40n)" savecurrent=false}
C {gnd.sym} -340 -80 0 0 {name=l2 lab=GND}
C {gnd.sym} -550 60 0 0 {name=l3 lab=GND}
C {gnd.sym} -550 -80 0 0 {name=l4 lab=GND}
C {code_shown.sym} 110 -230 0 0 {name=s1 only_toplevel=false value=".lib /mnt/d/EDA/pdk/open_pdks/sky130/sky130A/libs.tech/ngspice/sky130.lib.spice tt
.control
save all
tran 100p 80n
run
plot v(A) v(B) v(Y)
.endc"}
C {sky130_fd_pr/pfet3_01v8.sym} 20 -150 0 0 {name=M3
W=1
L=0.15
body=VDD
nf=1
mult=1
ad="expr('int((@nf + 1)/2) * @W / @nf * 0.29')"
pd="expr('2*int((@nf + 1)/2) * (@W / @nf + 0.29)')"
as="expr('int((@nf + 2)/2) * @W / @nf * 0.29')"
ps="expr('2*int((@nf + 2)/2) * (@W / @nf + 0.29)')"
nrd="expr('0.29 / @W ')" nrs="expr('0.29 / @W ')"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet3_01v8.sym} 60 -30 0 1 {name=M4
W=1
L=0.15
body=VDD
nf=1
mult=1
ad="expr('int((@nf + 1)/2) * @W / @nf * 0.29')"
pd="expr('2*int((@nf + 1)/2) * (@W / @nf + 0.29)')"
as="expr('int((@nf + 2)/2) * @W / @nf * 0.29')"
ps="expr('2*int((@nf + 2)/2) * (@W / @nf + 0.29)')"
nrd="expr('0.29 / @W ')" nrs="expr('0.29 / @W ')"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {ipin.sym} 300 170 0 1 {name=p8 lab=B}
