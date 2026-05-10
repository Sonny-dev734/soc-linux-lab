import re

log_file = "../logs/smart_activity.log"

connections = []
alerts = 0

with open(log_file, "r") as f:
    for line in f:
        match = re.search(r"connections=(\d+)", line)
        if match:
            connections.append(int(match.group(1)))

        if "ALERT" in line:
            alerts += 1

if connections:
    max_conn = max(connections)
    avg_conn = sum(connections) / len(connections)
else:
    max_conn = 0
    avg_conn = 0

# Simple SOC-style risk scoring
risk_score = 0

if max_conn > 80:
    risk_score += 50
elif max_conn > 50:
    risk_score += 20

if alerts > 0:
    risk_score += 30

if avg_conn > 40:
    risk_score += 20

print("SOC RISK ANALYSIS REPORT")
print("------------------------")
print(f"Max connections: {max_conn}")
print(f"Average connections: {avg_conn:.2f}")
print(f"Alerts triggered: {alerts}")
print(f"Risk score: {risk_score}/100")

if risk_score < 30:
    print("Status: LOW RISK (normal system behavior)")
elif risk_score < 70:
    print("Status: MEDIUM RISK (monitor recommended)")
else:
    print("Status: HIGH RISK (investigation needed)")



