import os
import shutil
import time
import schedule
from datetime import datetime

def backup_files(source_dirs, backup_dir):
    """Backs up the specified directories to the backup directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    for src_dir in source_dirs:
        if os.path.exists(src_dir):
            backup_subdir = os.path.join(backup_dir, os.path.basename(src_dir) + '_' + datetime.now().strftime('%Y%m%d%H%M%S'))
            shutil.copytree(src_dir, backup_subdir)
            print(f"Backup of {src_dir} completed successfully.")
        else:
            print(f"Source directory {src_dir} does not exist, skipping backup.")

def schedule_backups(source_dirs, backup_dir, interval_hours):
    """Schedules backups at regular intervals."""
    schedule.every(interval_hours).hours.do(backup_files, source_dirs=source_dirs, backup_dir=backup_dir)
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    source_dirs = ['C:\\path\\to\\important_folder1', 'C:\\path\\to\\important_folder2']
    backup_dir = 'C:\\path\\to\\backup_location'
    interval_hours = 24  # Schedule backups every 24 hours

    print(f"Starting backup process every {interval_hours} hours.")
    schedule_backups(source_dirs, backup_dir, interval_hours)

if __name__ == "__main__":
    main()