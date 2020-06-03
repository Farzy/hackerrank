#!/usr/local/bin/bash

declare -a ARR

# Hack to read the last line even if then is no final "\n"
while read NAME || [[ -n "$NAME" ]]; do
    ARR=(${ARR[@]} "$NAME")
done

echo ${ARR[@]} ${ARR[@]} ${ARR[@]}
