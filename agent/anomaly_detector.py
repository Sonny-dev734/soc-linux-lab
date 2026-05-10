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

    conn = event["connections"]
    proc = event["top_process"]

    connections.append(conn)

    if proc not in processes:
        processes[proc] = 0

    processes[proc] += 1

# Statistical baseline
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

print("SOC ANOMALY DETECTION REPORT")
print("----------------------------")

print(f"Telemetry events analyzed: {len(events)}")
print(f"Average connections: {avg_conn:.2f}")
print(f"Standard deviation: {std_conn:.2f}")
print(f"Dynamic anomaly threshold: {threshold:.2f}")

print("\nProcess frequency:")

for proc, count in sorted(processes.items(), key=lambda x: x[1], reverse=True):
    print(f"- {proc}: {count}")

print("\nAnomaly findings:")

if anomalies:
    for anomaly in anomalies:
        print(f"[!] Spike detected at {anomaly['timestamp']} ({anomaly['connections']} connections)")
else:
    print("No anomalies detected")



