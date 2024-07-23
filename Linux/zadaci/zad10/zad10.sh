#!/bin/bash

while IFS= read -r line; do
  echo "$line" | grep -iE "the|that|then|those"
done
