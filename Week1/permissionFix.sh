#!/bin/bash

#Directory
DIR="/Downloads"
#Permissions defiend by root user
permissions="750"
#Checking for current permission of Directory
current_perm=$(stat -c "%a" "$DIR")

if [ "$current_perm" -eq 777 ]; then
    chmod "$permissions" "$DIR"
    echo "Permissions Fixed"
else 
    echo "Permissions are ok!!"
fi