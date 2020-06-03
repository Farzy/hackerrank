#!/usr/local/bin/bash

read -a ARR < <(paste -s -d ' ' -)

echo "Array size: ${#ARR[*]}"
echo "Array : ${ARR[*]}"

declare -a ARR2=${ARR[@]/[A-N]/.}
echo "Array2: ${ARR2[*]}"
