sed -e 's/one/o1e/g' -e 's/two/t2o/g' -e 's/three/t3e/g'  -e 's/four/f4e/g' -e 's/five/f5e/g' -e 's/six/s6x/g' -e 's/seven/s7n/g' -e 's/eight/e8t/g' -e 's/nine/n9e/g' calibration-inputs \
  | sed -e 's/[^0-9]//g' \ 
  | sed -E 's/(.)(.*)?(.)$/\1\3/' \
  | sed -E 's/^(.)$/\1\1/' \
  | awk '{s+=$1} END {print s}'
