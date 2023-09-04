Automating Housekeeping with Crontab and Linux Utilities
Script performs the following tasks:

Sets up paths for directories and log files.

Initializes a counter for large files.

Creates a log entry with the current date and time.

Searches for files larger than 2GB in a specified directory.

Counts and logs the number of large files found.

Lists the names of large files in the log.

Calculates the disk usage of the system.

Logs the disk usage information.

Cleans up old log files that are more than 2 weeks old.

Schedules cron to execute this script daily

These lines set up paths for different folders and files.

search_path="/home/prasanthkumar/github/sonix_batch3/linux-proj/project-2/source"

log_path="/home/prasanthkumar/github/sonix_batch3/linux-proj/project-2/logs"

summary_log="team2.log"

This line sets up a counter for large files and initializes it to zero.

large_file_count=0

This line creates a log entry with the current date and time, and it adds it to the summary log file.

echo "$(date): Summary Log" >> "$log_path/$summary_log"

This line searches for files larger than 2GB in the specified search path. It counts how many such files are found and stores the count in the large file count variable.

large_file_count=$(find "$search_path" -type f -size +2G | wc -l)

This line adds a line to the summary log indicating the count of files larger than 2GB.

echo "Number of files larger than 2GB: $large_file_count" >> "$log_path/$summary_log"

This line lists the names of files larger than 2GB and adds them to the summary log.

find "$search_path" -type f -size +2G >> "$log_path/$summary_log"

This line checks how much disk space is used on the system. It extracts the disk usage value and stores it in the disk usage variable.

disk_usage=$(df -BM / | awk 'NR==2 {print $3}')

This line adds the disk usage information to the summary log.

echo "Disk usage: $disk_usage MB" >> "$log_path/$summary_log"

This line finds log files older than 14 days in the specified log path. It deletes those old log files to keep the folder clean.

find "$log_path" -name "$summary_log*" -mtime +14 -exec rm {} ;

CRON:
It allows you to automate the execution of tasks or commands at specific times, on specific days, or at regular intervals.

0 0 * * * /home/prasanthkumar/github/sonix_batch3/linux-proj/project-2/project2 

