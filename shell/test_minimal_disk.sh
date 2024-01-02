#!/bin/bash
set -x

free_space=$(df -h / | awk 'NR==2{print $4}' | sed 's/G//')
free_space=200.5
warning_threshold=200
if [ $(echo "$free_space < $warning_threshold" | awk '{print ($1 < $3) ? "1" : "0"}') -eq 1 ]; then
  echo "Warning: The remaining disk space on this host may not be an integer."
fi
