import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

telemetry_file = os.path.join(BASE_DIR, "telemetry", "telemetry.jsonl")
baseline_file = os.path.join(BASE_DIR, "data", "baseline.json")

events = []

with open(telemetry_file, "r") as f:
    for line in f:
        try:
            events.append(json.loads(line))
        except:
            pass

connections = []
ports = {}
processes = {}

for e in events:
    connections.append(e["connections"])

    proc = e["top_process"]
    processes[proc] = processes.get(proc, 0) + 1

    ports["listening"] = ports.get("listening", 0) + e["listening_ports"]

if connections:
    avg_conn = sum(connections) / len(connections)
    avg_ports = ports["listening"] / len(events)
else:
    avg_conn = 0
    avg_ports = 0

baseline = {
    "avg_connections": avg_conn,
    "avg_listening_ports": avg_ports,
    "process_frequency": processes
}

with open(baseline_file, "w") as f:
    json.dump(baseline, f, indent=4)

print("BASELINE UPDATED")
print("----------------")
print(f"Avg connections: {avg_conn:.2f}")
print(f"Avg ports: {avg_ports:.2f}")
print("Process baseline stored.")





