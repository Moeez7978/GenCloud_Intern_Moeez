#!/bin/bash

service="nginx"
memory=$(systemctl show "$service" --property=MemoryCurrent --value)
maxlimit=268435456 #256 MBs -> 256*1024*1024 

if [ "$memory" -gt "$maxlimit" ]; then
   systemctl restart "$service"
   echo "Service Restarted Successfully!"
else
    echo "Service Running Properly"
fi    