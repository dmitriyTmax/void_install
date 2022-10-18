#!/bin/bash
if ! /usr/bin/l2ping -c 1 28:16:7F:B6:03:D9; then 
sleep 10
else  
swaylock -f -c 000000 
fi
