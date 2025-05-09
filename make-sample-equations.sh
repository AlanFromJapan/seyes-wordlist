#!/bin/bash

for x in $(seq 1 10); do
    echo "Processing file $x..."
    bin/python src/seyes_maths.py "equations/equations_$x.png" 

    echo ""
done