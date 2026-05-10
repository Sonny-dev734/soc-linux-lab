#!/bin/bash

LOG="../logs/activity.log"

echo "SOC ANALYSIS REPORT"
echo "-------------------"

TOTAL=$(grep "connections=" $LOG | wc -l)
ALERTS=$(grep "ALERT" $LOG | wc -l)
MAX=$(grep "connections=" $LOG | awk -F'=' '{print $2}' | sort -n | tail -1)

echo "Total samples collected: $TOTAL"
echo "Alerts triggered: $ALERTS"
echo "Peak connection count: $MAX"

echo ""
echo "INTERPRETATION:"
echo "- Stable low values = normal system behavior"
echo "- Sudden spikes = potential anomaly"
echo "- No alerts = system within expected baseline"




