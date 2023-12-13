sed -e 's/[^0-9]//g' calibration-inputs \ 
  | sed -E 's/(.)(.*)?(.)$/\1\3/' \
  | sed -E 's/^(.)$/\1\1/' \
  | awk '{s+=$1} END {print s}'
