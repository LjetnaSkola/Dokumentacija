#!/bin/bash

if [ "$@" -le 1 ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

filename="$1"

if [ ! -f "$filename" ]; then
  echo "File not found!"
  exit 1
fi

while IFS= read -r line; do
  echo "$line"
  counter=$((counter + 1))
  if [ "$counter" -ge 5 ]; then
    break
  fi
done < "$filename"
