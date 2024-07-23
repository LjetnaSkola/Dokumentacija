#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <filename>"
fi

filename=$1

if [ ! -f "$filename" ]; then
  echo "File $filename does not exist"
fi

x=$(tail -c5 "$filename")
echo "Last 4 characters of file are: $x"
