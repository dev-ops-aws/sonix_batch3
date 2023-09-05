#!/bin/bash

source_path="/home/prasanthkumar/github/sonix_batch3/linux-proj/project-2/source"
log_path="/home/prasanthkumar/github/sonix_batch3/linux-proj/project-2/logs"
summary_log="team2.log"

#Initialize to count
large_file_count=0

#append to summary log
echo "$(date): Summary Log" >> "$log_path/$summary_log"

# Find large files and add to summary
large_file_count=$(find "$source_path" -type f -size +2G | wc -l)
echo "Number of files larger than 2GB: $large_file_count" >> "$log_path/$summary_log"
find "$source_path" -type f -size +2G >> "$log_path/$summary_log"

# Calculate disk usage and add to summary
disk_usage=$(df -BM / | awk 'NR==2 {print $3}')
echo "Disk usage: $disk_usage (MB)" >> "$log_path/$summary_log"

# Rotate and cleanup old summary logs
find "$log_path" -name "$summary_log*" -mtime +14 -exec rm {} \;

# CRON 
0 0 * * * /home/prasanthkumar/github/sonix_batch3/linux-proj/project-2/project2
