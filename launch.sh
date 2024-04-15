#!/bin/bash
for i in $(python3 ./main.py);do bash ./scan.sh $i;done
