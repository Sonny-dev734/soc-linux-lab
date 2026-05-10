#!/bin/bash

echo "SOC SNAPSHOT REPORT"
echo "-------------------"
date

echo ""
echo "ACTIVE CONNECTIONS"
ss -tunap | head -20

echo ""
echo "NETWORK USAGE"
sudo nethogs -t -c 3 2>/dev/null

echo ""
echo "LISTENING SERVICES"
ss -lntup






