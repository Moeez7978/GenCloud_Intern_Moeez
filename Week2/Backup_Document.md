# Automated Backup Script

This script creates a backup of a specified directory, stores it in a backup folder, logs, and removes old backups after a certain number of days.

## Script Overview

The script performs the following tasks:

1. Defines the source directory to back up.
2. Creates backup and log directories if they do not exist.
3. Generates a timestamped backup file.
4. Logs all actions performed by the script.
5. Compresses the source directory into a `.tar.gz` archive.
6. Deletes backups older than a specified number of days.

## Configuration Variables

These variables can be modified based on your system and requirements.

```bash
SOURCE="/var/www"
BACKUP_DIR="$HOME/backups/daily"
LOG_FILE="$HOME/backups/logs/backup.log"
RETENTION_DAYS=7
```

* **SOURCE** – Directory that will be backed up.
* **BACKUP_DIR** – Location where backup archives will be stored.
* **LOG_FILE** – File where script logs will be saved.
* **RETENTION_DAYS** – Number of days backups will be kept before deletion.

## How the Script Works

### 1. Generate Backup Name

The script creates a timestamp to ensure each backup file is unique.

```bash
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
ARCHIVE="backup_$DATE.tar.gz"
```

### 2. Create Required Directories

The script ensures the log and backup directories exist.

```bash
mkdir -p "$HOME/backups/logs"
mkdir -p "$BACKUP_DIR"
```

### 3. Logging Function

A function is used to record messages in the log file and display them in the terminal.

```bash
log(){
 echo "[$(date)] $1" | tee -a "$LOG_FILE"
}
```

### 4. Check Source Directory

Before creating a backup, the script checks if the source directory exists.

```bash
if [ ! -d "$SOURCE" ]; then
 log "Source directory not found"
 exit 1
fi
```

### 5. Create Backup

The script compresses the source directory using `tar`.

```bash
tar -czf "$BACKUP_DIR/$ARCHIVE" "$SOURCE"
```

If the backup is successful, it logs a success message. Otherwise, it stops execution.

### 6. Remove Old Backups

Backups older than the specified retention period are deleted.

```bash
find "$BACKUP_DIR" -type f -mtime +$RETENTION_DAYS -delete
```

## Example Log Output

```
[Thu Mar 26 10:00:01] Backup job started
[Thu Mar 26 10:00:05] Backup created successfully
[Thu Mar 26 10:00:05] Cleaning old backups
[Thu Mar 26 10:00:06] Backup completed
```

## How to Run the Script

1. Save the script as `backup.sh`
2. Give execute permission:

```bash
chmod +x backup.sh
```

3. Run the script:

```bash
./backup.sh
```

## Optional: Run Automatically with Cron

To run the backup daily, add a cron job:

```bash
crontab -e
```

Example (runs every day at 2 AM):

```bash
0 2 * * * /path/to/backup.sh
```

---

This script is useful for automating daily backups and maintaining a clean backup directory by removing old files.
