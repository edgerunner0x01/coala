#!/bin/bash
url=$1
dig $url && \
sleep 3 && \
echo -ne "\n" && \
nmap -F $url
