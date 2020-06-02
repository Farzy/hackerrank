#!/usr/local/bin/bash

declare -r HEIGHT=63
declare -r WIDTH=100
declare -r SIZE1=16

declare -A matrix

init_matrix() {
    for ((y=0 ; y < HEIGHT ; y++)); do
        for ((x=0 ; x < WIDTH ; x++)); do
            matrix[$x,$y]='_'
        done
    done
}

draw_matrix() {
    for ((y=HEIGHT-1 ; y >= 0 ; y--)); do
        for ((x=0 ; x < WIDTH ; x++)); do
            echo -n ${matrix[$x,$y]}
        done
        echo
    done
}

tree() {
    local -i iteration=$1
    local -a roots=$2
    local -i starty=$3
    local -i size=$4

    # End recursion
    if (( iteration == 0 )); then
        return
    fi

    local -i root_count=${#roots[*]}

    echo "iteration: ${iteration}, roots: '${roots[*]}', root_count: ${root_count}" 

    for (( root=0 ; root < root_count ; root++)); do
        for (( y=starty ; y < starty + size ; y++ )); do
            matrix[${roots[$root]},$y]='1'
        done
    done

    # Double roots
    roots=(${roots[*]} ${roots[*]})
    let "root_count=root_count * 2"
    echo "new roots: '${roots[*]}', root_count: ${root_count}" 
    
    for (( y=starty + size ; y < starty + 2 * size ; y++ )); do
        for (( i = 0 ; i < root_count ; i++ )); do
            if (( i % 2 == 0)); then
                roots[$i]=$(( roots[$i] - 1))
                matrix[${roots[$i]},$y]=1
            else
                roots[$i]=$(( roots[$i] + 1))
                matrix[${roots[$i]},$y]=1
            fi
        done
    done

    echo "new roots after branches: '${roots[*]}', root_count: ${root_count}" 

    # Recurse
    tree $(( iteration-1 )) $roots $(( starty + 2*size )) $(( size/2 ))
}


init_matrix
roots=(50)
tree 5 $roots 0 $SIZE1
draw_matrix
