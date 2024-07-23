#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <filename>"
fi

filename=$1

if [ ! -f "$filename" ]; then
  echo "File $filename does not exist"
fi

countries=()
while IFS= read -r line; do
  countries+=("$line")
done < "$filename"

concatenated=()
for ((i=0; i<3; i++)); do
  concatenated+=("${countries[@]}")
done

printf "%s " "${concatenated[@]}"
