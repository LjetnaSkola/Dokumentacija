#!/bin/bash

echo Enter start number:
read start
echo Enter end number:
read end

if [ $((start % 2)) -eq 0 ]; then
    for i in $(seq $((start + 1)) 2 $end); do
        echo $i
    done
else
    for i in $(seq $start 2 $end); do
        echo $i
    done
fi
