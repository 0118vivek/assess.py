#!/bin/bash
# This script monitors CPU and memory usage

# Define the log file
LOGFILE="usage.log"

# Start the loop to monitor CPU and memory usage
while :
do
  # Get the current usage of CPU and memory
  cpuUsage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}' | awk '{printf "%.2f%%\n", $1}')
  memUsage=$(free -m | awk '/Mem/{printf "%.2f%%\n", $3*100/$2}')

  # Log the usage to the file
  echo "CPU Usage: $cpuUsage" >> $LOGFILE
  echo "Memory Usage: $memUsage" >> $LOGFILE

  # Sleep for 5 seconds
  sleep 5
done