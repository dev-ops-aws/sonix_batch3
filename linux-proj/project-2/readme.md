Script Title : Efficient Log Management 
---------------------------

#!/bin/bash : Bash shell script for monitoring large files, calculating disk usage, and maintaining logs. Customize paths and schedule via cron.

---------------------------


Description: 
----------------------------

This Bash script monitors a specified directory for large files (greater than 2GB), calculates disk usage, and maintains a summary log. It also performs log rotation to clean up old log files. You can schedule this script to run as a cron job.
----------------------------


Usage:
----------------------------

Edit the script to set your desired source path and log path.

Schedule the script to run at regular intervals using cron.

----------------------------


Script Details:
-----------------------------

source_path: The directory path to monitor for large files.

log_path: The directory where log files will be stored.

summary_log: The name of the summary log file.

large_file_count: Variable to store the count of large files.

Make sure to replace the source and log paths with the actual path to your script.

-----------------------------


The script performs the following tasks:
-----------------------------

1) Initializes large_file_count to 0.
 
3) Appends a timestamped header to the summary log.

5) Uses the find command to count and list files larger than 2GB in the specified source directory. The results are added to the summary log.
 
7) Calculates the disk usage of the root directory (in megabytes) using df and adds it to the summary log.
 
9) Performs log rotation by deleting summary log files older than 14 days in the specified log directory.
 -----------------------------


Alternative way to delete the logs which are 14 days old ( Through cron )
-----------------------------

0 0 * * * find /path/to/your/repository/logs -type f -name "summary.log*" -mtime +14 -exec rm {} \;
-----------------------------
