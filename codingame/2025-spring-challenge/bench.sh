#!/bin/sh
# Simple benchmark script that runs a program multiple times with the same input
# Usage: ./bench.sh <program> <iterations> <input>

if [ $# -lt 3 ]; then
    echo "Usage: $0 <program> <iterations> <input>"
    exit 1
fi

PROGRAM="$1"
ITERATIONS="$2"
INPUT="$3"

for _ in $(seq 1 "$ITERATIONS"); do
    echo "$INPUT" | $PROGRAM
done
