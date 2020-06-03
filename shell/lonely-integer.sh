#!/usr/local/bin/bash

read N
read -a ARR < <(paste -s -d ' ' -)

echo "Array size: ${N} or ${#ARR[*]}"
echo "Array : ${ARR[*]}"

for NUMBER in ${ARR[@]}; do
    echo $NUMBER
done | sort | uniq -u

