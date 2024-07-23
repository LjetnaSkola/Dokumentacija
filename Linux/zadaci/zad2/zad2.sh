#!/bin/bash

for i in $(seq "$1" "$2"); do
  if [ $((i % 2)) -ne 0 ]; then
    echo "ODD $i"
  fi
done
