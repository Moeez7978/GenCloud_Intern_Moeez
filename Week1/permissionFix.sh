#!/bin/bash
recipient="moeez7978911@gmail.com"
#Directory
DIR="/Downloads"

#Permissions defiend by root user
permissions="750"
if [ -d "$DIR" ]; then

#Checking for current permission of Directory
current_perm=$(stat -c "%a" "$DIR")

 if [ "$current_perm" -eq 777 ]; then
 
#Send mail to recipient that someone changed the directory permissions restoring them

    chmod "$permissions" "$DIR"
    echo "Permissions Fixed"
 else 
    echo "Permissions are ok!!"
 fi

else
   echo "Directory Doesn,t Exists"
fi
