#!/usr/bin/env bash
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$ROOT/data" "$ROOT/plots"

(cd "$ROOT/day15" && ngspice -b inverter_vtc.cir)
(cd "$ROOT/day16" && ngspice -b inverter_transient.cir)

for W in 1u 2u 3u 4u; do
  cat > "$ROOT/day18/size_${W}.cir" <<EOF
CMOS inverter sizing test - PMOS width ${W}
VDD vdd 0 DC 1.8
VIN in 0 PULSE(0 1.8 1n 100p 100p 5n 10n)
.model NMOD NMOS (LEVEL=1 VTO=0.55 KP=200u LAMBDA=0.02)
.model PMOD PMOS (LEVEL=1 VTO=-0.55 KP=80u LAMBDA=0.02)
MP out in vdd vdd PMOD W=${W} L=0.15u
MN out in 0 0 NMOD W=1u L=0.15u
CLOAD out 0 10f
.control
set wr_singlescale
set wr_vecnames
tran 10p 30n
wrdata ../data/size_${W}.dat v(in) v(out)
quit
.endc
.end
EOF
  (cd "$ROOT/day18" && ngspice -b "size_${W}.cir")
done

python3 "$ROOT/analyse_week3.py"
echo "Completed. Generated data/ and plots/."
