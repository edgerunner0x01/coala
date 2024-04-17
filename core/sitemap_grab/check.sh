#!/bin/bash
for i in $(cat $1);do python3 sitemap_stat.py $i;done
