#!/bin/bash

if [ $1 -le 0 ]; then
  echo "Invalid number!"
  exit 1
fi

x=1
for i in $(seq 1 "$1"); do
  x=$((x*i))
done

echo "Factorial of number $1 is $x"
