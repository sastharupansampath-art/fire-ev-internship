v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
N 440 90 440 160 {lab=#net1}
N 280 -110 280 -40 {lab=Y}
N 280 -40 600 -40 {lab=Y}
N 600 -120 600 -40 {lab=Y}
N 440 -40 440 30 {lab=Y}
N 440 220 440 260 {lab=GND}
N 280 -240 280 -170 {lab=VDD}
N 280 -240 580 -240 {lab=VDD}
N 580 -240 600 -240 {lab=VDD}
N 600 -240 600 -180 {lab=VDD}
N 440 -300 440 -240 {lab=VDD}
N 160 60 400 60 {lab=A}
N 160 -140 160 60 {lab=A}
N 160 -140 240 -140 {lab=A}
N 640 -150 680 -150 {lab=B}
N 480 190 530 190 {lab=B}
N 60 -40 160 -40 {lab=A}
N 440 -10 680 -10 {lab=Y}
N -280 -140 -280 -70 {lab=GND}
N -180 -140 -180 -70 {lab=GND}
N -70 -140 -70 -70 {lab=GND}
C {sky130_fd_pr/nfet3_01v8.sym} 420 60 0 0 {name=M1
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
C {sky130_fd_pr/nfet3_01v8.sym} 460 190 0 1 {name=M2
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
C {sky130_fd_pr/pfet3_01v8.sym} 260 -140 0 0 {name=M3
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
C {sky130_fd_pr/pfet3_01v8.sym} 620 -150 0 1 {name=M4
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
C {gnd.sym} 440 260 0 0 {name=l1 lab=GND}
C {lab_pin.sym} 440 -300 0 0 {name=p3 sig_type=std_logic lab=VDD}
C {ipin.sym} 530 190 2 0 {name=p2 lab=B}
C {ipin.sym} 60 -40 2 1 {name=p1 lab=A}
C {ipin.sym} 680 -150 2 0 {name=p4 lab=B}
C {opin.sym} 680 -10 0 0 {name=p5 lab=Y}
C {vsource.sym} -70 -170 0 0 {name=VDD value=1.8 savecurrent=false}
C {lab_pin.sym} -70 -200 0 0 {name=p6 sig_type=std_logic lab=VDD}
C {vsource.sym} -180 -170 0 0 {name=VA value="PULSE(0 1.8 0n 100p 100p 10n 20n)" savecurrent=false}
C {vsource.sym} -280 -170 0 0 {name=VB value="PULSE(0 1.8 0n 100p 100p 20n 40n)" savecurrent=false}
C {lab_pin.sym} -180 -200 0 0 {name=p7 sig_type=std_logic lab=A}
C {gnd.sym} -70 -70 0 0 {name=l2 lab=GND}
C {gnd.sym} -180 -70 0 0 {name=l3 lab=GND}
C {gnd.sym} -280 -70 0 0 {name=l4 lab=GND}
C {code_shown.sym} 600 -340 0 0 {name=s1 only_toplevel=false value=".lib /mnt/d/EDA/pdk/open_pdks/sky130/sky130A/libs.tech/ngspice/sky130.lib.spice tt
.control
save all
tran 100p 200n
run
plot v(A) v(B) v(Y)
.endc"}
C {lab_pin.sym} -280 -200 0 0 {name=p8 sig_type=std_logic lab=B}
