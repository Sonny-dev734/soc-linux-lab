#!/bin/bash

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

TELEMETRY_DIR="$BASE_DIR/telemetry"
TELEMETRY_FILE="$TELEMETRY_DIR/telemetry.jsonl"

mkdir -p "$TELEMETRY_DIR"

INTERVAL=3

touch "$TELEMETRY_FILE"

echo "JSON telemetry monitor initialized"

while true
do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

    CONNECTIONS=$(ss -tun state established | wc -l)
    LISTENING=$(ss -lnt | wc -l)

    TOP_PROCESS=$(ps -eo comm,%cpu --sort=-%cpu | head -2 | tail -1 | awk '{print $1}')

    STATE="NORMAL"

    if [ "$CONNECTIONS" -ge 40 ]; then
        STATE="ELEVATED"
    fi

    if [ "$CONNECTIONS" -ge 80 ]; then
        STATE="ALERT"
    fi

    echo "{\"timestamp\":\"$TIMESTAMP\",\"connections\":$CONNECTIONS,\"listening_ports\":$LISTENING,\"top_process\":\"$TOP_PROCESS\",\"state\":\"$STATE\"}" >> "$TELEMETRY_FILE"

    echo "[$TIMESTAMP] telemetry recorded"

    sleep "$INTERVAL"
done



