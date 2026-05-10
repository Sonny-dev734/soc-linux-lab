#!/bin/bash

LOG="../logs/smart_activity.log"

echo "SOC SECURITY REPORT"
echo "-------------------"

TOTAL=$(grep "connections=" $LOG | wc -l)
NORMAL=$(grep "STATE: NORMAL" $LOG | wc -l)
ELEVATED=$(grep "STATE: ELEVATED" $LOG | wc -l)
ALERTS=$(grep "ALERT" $LOG | wc -l)

echo "Total samples: $TOTAL"
echo "Normal states: $NORMAL"
echo "Elevated states: $ELEVATED"
echo "Alerts: $ALERTS"

echo ""
echo "INTERPRETATION"

if [ "$ALERTS" -eq 0 ]; then
    echo "System behavior is stable. No anomaly detected."
else
    echo "Anomalies detected. Requires manual review (educational context)."
fi



