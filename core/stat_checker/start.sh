#!/bin/bash
for i in $(cat $1);do python3 main.py $i;done
