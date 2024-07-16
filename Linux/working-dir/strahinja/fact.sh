#!/bin/bash

fact() {
    local fact=1    
    for i in $(seq 1 $1); do
        fact=$((fact*i))
    done
    echo $fact
}

N=-1
while [ $N -lt 0 ]; do 
    echo "Enter a non-negative number:"
    read N
done

factNum=$(fact $N)
echo "Its factorial is $factNum"