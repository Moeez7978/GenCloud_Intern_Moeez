#!/bin/bash

recipient="moeez7978911@gmail.com"

service="nginx"
memory=$(systemctl show "$service" --property=MemoryCurrent --value) #bytes
maxlimit=268435456      #256 MBs -> 256*1024*1024 
memory_mb=$(( memory / 1024 / 1024 ))

if [ "$memory" -gt "$maxlimit" ]; then

   sudo systemctl restart "$service"
# Send Mail to recipient that service excceeded the max memory limit and restarted successfully 

   echo "Service Restarted Successfully! on $(date)"
   echo "Service $service Restarted due to high memory usage on $(date)" | mail -s "Service Restarted" "$recipient"
else
    echo "Service Running Properly"
    echo "Usage: $memory_mb MBs on $(date)"
    echo "Service $service running fine with usage $memory_mb MBs at $(date)" | mail -s "Service Running Fine" "$recipient"
fi
