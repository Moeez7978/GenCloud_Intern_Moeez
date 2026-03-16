#!/bin/bash

#Directory
DIR="/home/moeez/Downloads2"
#Permissions defiend by root user
permissions="750"
if [ -d "$DIR" ]; then
#Checking for current permission of Directory
current_perm=$(stat -c "%a" "$DIR")
 if [ "$current_perm" -eq 777 ]; then
    chmod "$permissions" "$DIR"
    echo "Permissions Fixed"
 else 
    echo "Permissions are ok!!"
 fi
else
   echo "Directory Doesn,t Exists"
fi
