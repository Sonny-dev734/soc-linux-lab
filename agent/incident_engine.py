import json
import os
from statistics import mean, stdev
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

telemetry_file = os.path.join(BASE_DIR, "telemetry", "telemetry.jsonl")
report_file = os.path.join(BASE_DIR, "reports", "incident_report.txt")

events = []

with open(telemetry_file, "r") as f:
    for line in f:
        try:
            events.append(json.loads(line))
        except:
            pass

connections = [e["connections"] for e in events]

avg_conn = mean(connections)
std_conn = stdev(connections) if len(connections) > 1 else 0
threshold = avg_conn + (2 * std_conn)

incidents = []

for e in events:
    if e["connections"] > threshold:
        incidents.append(e)

# Risk classification
if len(incidents) == 0:
    risk = "LOW"
elif len(incidents) < 3:
    risk = "MEDIUM"
else:
    risk = "HIGH"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = []
report.append("======================================")
report.append("SOC INCIDENT REPORT")
report.append("======================================")
report.append(f"Generated: {timestamp}")
report.append("")
report.append(f"Total events analyzed: {len(events)}")
report.append(f"Average connections: {avg_conn:.2f}")
report.append(f"Standard deviation: {std_conn:.2f}")
report.append(f"Anomaly threshold: {threshold:.2f}")
report.append(f"Detected incidents: {len(incidents)}")
report.append("")
report.append("INCIDENT DETAILS:")

if incidents:
    for i in incidents:
        report.append(f"- [{i['timestamp']}] connections={i['connections']} state={i['state']}")
else:
    report.append("No significant incidents detected.")

report.append("")
report.append(f"FINAL RISK LEVEL: {risk}")
report.append("======================================")

with open(report_file, "w") as f:
    f.write("\n".join(report))

print("INCIDENT REPORT GENERATED")
print(f"Risk Level: {risk}")
print(f"Saved to: reports/incident_report.txt")



