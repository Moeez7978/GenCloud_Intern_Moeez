#!/bin/bash

recipient="moeez7978911@gmail.com"

service="nginx"
memory=$(systemctl show "$service" --property=MemoryCurrent --value)
maxlimit=268435456      #256 MBs -> 256*1024*1024 

if [ "$memory" -gt "$maxlimit" ]; then

   systemctl restart "$service"
# Send Mail to recipient that service excceeded the max memory limit and restarted successfully 

   echo "Service Restarted Successfully!"

else
    echo "Service Running Properly"
fi