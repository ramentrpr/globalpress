# GlobalPress

## Overview

GlobalPress is a Python-based application designed to automate the backup process for critical files and folders on Windows. It provides scheduled backups to ensure your important data is safe and up-to-date.

## Features

- Automates the backup of specified directories
- Schedules backups at user-defined intervals
- Organizes backups in timestamped folders for easy retrieval

## Requirements

- Python 3.6 or higher
- Third-party libraries: `schedule`

## Installation

1. Ensure Python is installed on your system.
2. Install the required package by running:
   ```bash
   pip install schedule
   ```

## Usage

1. Modify the `source_dirs` list in `globalpress.py` to include the paths of the directories you want to back up.
2. Set the `backup_dir` to the location where you want backups to be stored.
3. Define the `interval_hours` to specify how frequently backups should occur (e.g., `24` for daily backups).
4. Run the script:
   ```bash
   python globalpress.py
   ```
5. The script will print messages to the console indicating the progress of each backup.

## Important Notes

- Ensure that the backup directory has sufficient space to store the files.
- The script must have permission to read the source directories and write to the backup directory.
- This script is designed for Windows systems. Paths and functionality may need adjustment for other operating systems.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.