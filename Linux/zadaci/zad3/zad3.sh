#!/bin/bash

if [ $1 -lt 3 ]; then
  echo "Invalid number"
  exit 1
fi

x=0
y=1
echo "$x"
echo "$y"

for i in $(seq 0 "$(($1-2))"); do
  echo $((x+y))
  tmp=$y
  y=$((x+y))
  x=$tmp
done
