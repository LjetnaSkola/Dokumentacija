#!/bin/bash

fib() {
    local prevPrev=1
    local prev=2
    local res=0
    for i in $(seq 4 $1); do
        res=$((prev + prevPrev))
        prevPrev=$prev
        prev=$res
    done
    echo "Fib($1) = $res"
}

N=0

while [ $N -le 3 ]; do
    echo "Enter a number greater than 3:"
    read N
done

fib $N

