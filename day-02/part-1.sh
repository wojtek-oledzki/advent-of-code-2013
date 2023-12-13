grep -vE '(1[3-9]|[2-9][0-9]) red' input | grep -vE '(1[4-9]|[2-9][0-9]) green' | grep -vE '(1[5-9]|[2-9][0-9]) blue' | sed  -E 's/Game ([0-9]+):.*/\1/' | awk '{s+=$1} END {print s}'
