import json
import os
from statistics import mean, stdev

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

telemetry_file = os.path.join(BASE_DIR, "telemetry", "telemetry.jsonl")

events = []

with open(telemetry_file, "r") as f:
    for line in f:
        try:
            events.append(json.loads(line))
        except:
            pass

connections = []
processes = {}

for event in events:

    connections.append(event["connections"])

    proc = event["top_process"]

    if proc not in processes:
        processes[proc] = 0

    processes[proc] += 1

avg_conn = mean(connections)

if len(connections) > 1:
    std_conn = stdev(connections)
else:
    std_conn = 0

threshold = avg_conn + (2 * std_conn)

anomalies = []

for event in events:

    if event["connections"] > threshold:
        anomalies.append(event)

# Risk evaluation
risk_level = "LOW"

if len(anomalies) > 5:
    risk_level = "MEDIUM"

if len(anomalies) > 15:
    risk_level = "HIGH"

print("\n===================================")
print("SOC SECURITY POSTURE REPORT")
print("===================================\n")

print(f"Telemetry events analyzed : {len(events)}")
print(f"Average connection count  : {avg_conn:.2f}")
print(f"Behavior deviation        : {std_conn:.2f}")
print(f"Dynamic anomaly threshold : {threshold:.2f}")

print("\nTop observed processes:")

for proc, count in sorted(processes.items(), key=lambda x: x[1], reverse=True):
    print(f"  - {proc}: {count} events")

print("\nSecurity Findings:")

if anomalies:
    for anomaly in anomalies:
        print(f"  [!] Connection spike at {anomaly['timestamp']} ({anomaly['connections']} connections)")
else:
    print("  No anomalies detected during telemetry collection")

print("\nOperational Assessment:")

if risk_level == "LOW":
    print("  System behavior appears stable and consistent with normal local workstation activity.")

elif risk_level == "MEDIUM":
    print("  Moderate behavioral deviations detected. Continued monitoring recommended.")

else:
    print("  Significant behavioral anomalies detected. Investigation advised.")

print(f"\nOverall Risk Level: {risk_level}")

print("\n===================================")



