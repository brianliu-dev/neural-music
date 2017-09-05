#!/bin/sh
for filename in ../music-data/midis/*.mid; do
    s="$filename"
    s=${s##*/}
    ../midicsv-1.1/midicsv -v "$filename" ../music-data/csvs/${s%.*}.csv
done

# Script for running midi-csv on all the midis