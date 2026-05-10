import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

telemetry_file = os.path.join(BASE_DIR, "telemetry", "telemetry.jsonl")

events = []

with open(telemetry_file, "r") as f:
    for line in f:
        try:
            events.append(json.loads(line))
        except:
            pass

total = len(events)

normal = 0
elevated = 0
alerts = 0

top_processes = {}

connections = []

for event in events:

    connections.append(event["connections"])

    state = event["state"]

    if state == "NORMAL":
        normal += 1

    elif state == "ELEVATED":
        elevated += 1

    elif state == "ALERT":
        alerts += 1

    proc = event["top_process"]

    if proc not in top_processes:
        top_processes[proc] = 0

    top_processes[proc] += 1

if connections:
    avg_conn = sum(connections) / len(connections)
    max_conn = max(connections)
else:
    avg_conn = 0
    max_conn = 0

print("SOC JSON TELEMETRY REPORT")
print("-------------------------")

print(f"Total events: {total}")
print(f"Normal states: {normal}")
print(f"Elevated states: {elevated}")
print(f"Alert states: {alerts}")

print(f"Average connections: {avg_conn:.2f}")
print(f"Peak connections: {max_conn}")

print("\nMost observed processes:")

for proc, count in sorted(top_processes.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"- {proc}: {count} events")




