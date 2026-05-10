#!/bin/bash

# Absolute path safety (important in real tools)
BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

LOG_FILE="$BASE_DIR/logs/smart_activity.log"

# Safety defaults (prevents "empty variable" bugs)
CONNECTION_BASELINE=40
ALERT_THRESHOLD=80
INTERVAL=3

echo "SOC MONITOR STARTED" >> "$LOG_FILE"

while true
do
    TIME=$(date)

    CONNECTIONS=$(ss -tun state established | wc -l)
    LISTENING=$(ss -lnt | wc -l)

    echo "[$TIME] connections=$CONNECTIONS listening_ports=$LISTENING" | tee -a "$LOG_FILE"

    # Safety: ensure variables are numbers
    if [ "$CONNECTIONS" -ge "$CONNECTION_BASELINE" ] 2>/dev/null; then
        echo "[$TIME] STATE: ELEVATED" >> "$LOG_FILE"
    fi

    if [ "$CONNECTIONS" -ge "$ALERT_THRESHOLD" ] 2>/dev/null; then
        echo "[$TIME] ALERT: ANOMALY DETECTED" | tee -a "$LOG_FILE"
    fi

    sleep "$INTERVAL"
done





