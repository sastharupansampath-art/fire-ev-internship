v {xschem version=3.4.8RC file_version=1.3}
G {}
K {}
V {}
S {}
F {}
E {}
N -260 -370 -220 -370 {lab=#net1}
N -220 -370 -220 -290 {lab=#net1}
N -220 -290 -180 -290 {lab=#net1}
N -270 -170 -220 -170 {lab=#net2}
N -220 -250 -220 -170 {lab=#net2}
N -220 -250 -180 -250 {lab=#net2}
N -420 -350 -380 -350 {lab=T1}
N -420 -350 -420 -190 {lab=T1}
N -420 -190 -390 -190 {lab=T1}
N -470 -280 -420 -280 {lab=T1}
N -630 -300 -590 -300 {lab=A}
N -630 -390 -380 -390 {lab=A}
N -630 -390 -630 -300 {lab=A}
N -660 -390 -630 -390 {lab=A}
N -630 -260 -590 -260 {lab=B}
N -630 -260 -630 -150 {lab=B}
N -670 -150 -390 -150 {lab=B}
N 380 -250 420 -250 {lab=#net3}
N 420 -250 420 -170 {lab=#net3}
N 420 -170 460 -170 {lab=#net3}
N 370 -50 420 -50 {lab=#net4}
N 420 -130 420 -50 {lab=#net4}
N 420 -130 460 -130 {lab=#net4}
N 220 -230 260 -230 {lab=T2}
N 220 -230 220 -70 {lab=T2}
N 220 -70 250 -70 {lab=T2}
N 170 -160 220 -160 {lab=T2}
N 10 -180 50 -180 {lab=#net5}
N 10 -270 260 -270 {lab=#net5}
N 10 -270 10 -180 {lab=#net5}
N -20 -270 10 -270 {lab=#net5}
N 10 -140 50 -140 {lab=Cin}
N 10 -140 10 -30 {lab=Cin}
N -30 -30 250 -30 {lab=Cin}
N -60 -270 -20 -270 {lab=#net5}
N -670 -30 -30 -30 {lab=Cin}
N 580 -150 630 -150 {lab=Sum}
N 350 70 450 70 {lab=T1}
N 350 110 450 110 {lab=T2}
N 570 90 630 90 {lab=Cout}
C {sky130_stdcells/nand2_1.sym} -530 -280 0 0 {name=x1 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/nand2_1.sym} -320 -370 0 0 {name=x2 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/nand2_1.sym} -330 -170 0 0 {name=x3 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/nand2_1.sym} -120 -270 0 0 {name=x4 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/nand2_1.sym} 110 -160 0 0 {name=x5 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/nand2_1.sym} 320 -250 0 0 {name=x6 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/nand2_1.sym} 310 -50 0 0 {name=x7 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/nand2_1.sym} 520 -150 0 0 {name=x8 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {ipin.sym} -660 -390 0 0 {name=p1 lab=A}
C {ipin.sym} -670 -150 0 0 {name=p2 lab=B}
C {ipin.sym} -670 -30 0 0 {name=p3 lab=Cin}
C {opin.sym} 630 -150 0 0 {name=p4 lab=Sum}
C {lab_pin.sym} -420 -280 0 1 {name=p5 sig_type=std_logic lab=T1}
C {lab_pin.sym} 220 -160 0 1 {name=p6 sig_type=std_logic lab=T2}
C {sky130_stdcells/nand2_1.sym} 510 90 0 0 {name=x9 VGND=GND VNB=GND VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {opin.sym} 630 90 0 0 {name=p7 lab=Cout}
C {lab_pin.sym} 350 70 0 0 {name=p8 sig_type=std_logic lab=T1}
C {lab_pin.sym} 350 110 0 0 {name=p9 sig_type=std_logic lab=T2}
C {ipin.sym} -670 70 0 0 {name=p10 lab=VDD}
C {ipin.sym} -670 130 0 0 {name=p11 lab=GND}
