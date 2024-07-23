#!/bin/bash

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <n> <filename>"
  exit 1
fi


num=$1
filename="$2"

if [ ! -f "$filename" ]; then
  echo "File not found"
  exit 1
fi

while IFS= read -r line; do
  echo "The $num-th character of $line is: ${line:num-1:1}"
done < "$filename"
