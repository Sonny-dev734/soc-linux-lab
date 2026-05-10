#!/bin/bash

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

LOG_DIR="$BASE_DIR/logs"
LOG_FILE="$LOG_DIR/smart_activity.log"

mkdir -p "$LOG_DIR"

CONNECTION_BASELINE=40
ALERT_THRESHOLD=80
INTERVAL=3

touch "$LOG_FILE"

echo "SOC MONITOR INITIALIZED" >> "$LOG_FILE"

while true
do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

    CONNECTIONS=$(ss -tun state established | wc -l)
    LISTENING=$(ss -lnt | wc -l)

    if ! [[ "$CONNECTIONS" =~ ^[0-9]+$ ]]; then
        CONNECTIONS=0
    fi

    if ! [[ "$LISTENING" =~ ^[0-9]+$ ]]; then
        LISTENING=0
    fi

    STATE="NORMAL"

    if [ "$CONNECTIONS" -ge "$CONNECTION_BASELINE" ]; then
        STATE="ELEVATED"
    fi

    if [ "$CONNECTIONS" -ge "$ALERT_THRESHOLD" ]; then
        STATE="ALERT"
    fi

    echo "$TIMESTAMP | connections=$CONNECTIONS | listening_ports=$LISTENING | state=$STATE" | tee -a "$LOG_FILE"

    sleep "$INTERVAL"
done



