#!/bin/bash

SOURCE="/var/www"
BACKUP_DIR="$HOME/backups/daily"
LOG_FILE="$HOME/backups/logs/backup.log"
RETENTION_DAYS=7

DATE=$(date +"%Y-%m-%d_%H-%M-%S")
ARCHIVE="backup_$DATE.tar.gz"

mkdir -p "$HOME/backups/logs"
mkdir -p "$BACKUP_DIR"

log(){
 echo "[$(date)] $1" | tee -a "$LOG_FILE"
}

log "Backup job started"

if [ ! -d "$SOURCE" ]; then
 log "Source directory not found"
 exit 1
fi

tar -czf "$BACKUP_DIR/$ARCHIVE" "$SOURCE"

if [ $? -eq 0 ]; then
 log "Backup created successfully"
else
 log "Backup failed"
 exit 1
fi

log "Cleaning old backups"
find "$BACKUP_DIR" -type f -mtime +$RETENTION_DAYS -delete

log "Backup completed"
