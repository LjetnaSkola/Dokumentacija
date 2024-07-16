#!/bin/bash

read -p "Enter the position of the character (N): " N

echo "Enter the lines of input (press Ctrl+D to end):"
lines=()
while read -r line; do
  lines+=("$line")
done

for line in "${lines[@]}"; do
  echo "${line:N-1:1}"
done
