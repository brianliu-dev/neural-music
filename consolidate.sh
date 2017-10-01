#!/bin/sh
for filename in ../music-data/texts/*.txt; do
    python consolidate.py "$filename"
done

# Script for combining all the txt files into input.txt