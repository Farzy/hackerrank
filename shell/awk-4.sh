awk '{
    getline LINE2
    if (length(LINE2) != 0)
        printf "%s;%s\n", $0, LINE2
    else
        printf "%s;", $0
    }'
