#!/bin/bash

LOG="../logs/activity.log"
THRESHOLD=80

echo "Starting SOC monitoring..." >> $LOG

while true
do
    TIME=$(date)
    CONN=$(ss -tun state established | wc -l)

    echo "[$TIME] connections=$CONN" | tee -a $LOG

    if [ "$CONN" -gt "$THRESHOLD" ]; then
        echo "[$TIME] ALERT: abnormal connection level" | tee -a $LOG
    fi

    sleep 3
done




