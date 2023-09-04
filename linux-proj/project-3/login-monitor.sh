#!/bin/bash

# Define the log file to monitor
LOG_FILE="/var/log/auth.log"

# Define the email recipient
EMAIL_RECIPIENT="meghanakusuma@sonixhub.com"

# Define the email subject
EMAIL_SUBJECT="Unauthorized Login Attempt Detected on Your Server"

# Check the log file for failed login attempts
if grep -q "Failed password" "$LOG_FILE"; then
  MESSAGE="Unauthorized login attempt detected on your server. Please review the system logs for more details."
  #echo "$MESSAGE" | ssmtp "$EMAIL_RECIPIENT" -s "$EMAIL_SUBJECT"
  echo "$MESSAGE" | mail -s "$EMAIL_SUBJECT" $EMAIL_RECIPIENT
fi
