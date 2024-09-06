#!/bin/bash

for f in wordslist/*.txt; do
    echo "Processing $f file..."
    bin/python src/seyes_wordlist.py "$f" repeat

    echo ""
done