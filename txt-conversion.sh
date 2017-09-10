#!/bin/sh
for filename in ../music-data/csvs/*.csv; do
    python data_cleansing.py "$filename"
done

# Script for running data_cleansing on all the csvs