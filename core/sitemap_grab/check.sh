#!/bin/bash
for i in $(cat $1);do python3 robots_stat.py $i;done
