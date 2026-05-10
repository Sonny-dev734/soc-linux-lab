import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

telemetry_file = os.path.join(BASE_DIR, "telemetry", "telemetry.jsonl")
baseline_file = os.path.join(BASE_DIR, "data", "baseline.json")

with open(baseline_file, "r") as f:
    baseline = json.load(f)

events = []

with open(telemetry_file, "r") as f:
    for line in f:
        try:
            events.append(json.loads(line))
        except:
            pass

connections = [e["connections"] for e in events]

avg_conn = sum(connections) / len(connections)

drift = abs(avg_conn - baseline["avg_connections"])

print("\n============================")
print("BASELINE DRIFT ANALYSIS")
print("============================\n")

print(f"Baseline avg connections : {baseline['avg_connections']:.2f}")
print(f"Current avg connections  : {avg_conn:.2f}")
print(f"Drift magnitude          : {drift:.2f}")

if drift < 2:
    print("\nStatus: STABLE BEHAVIOR (no significant drift)")
elif drift < 5:
    print("\nStatus: MODERATE DRIFT (monitor changes)")
else:
    print("\nStatus: SIGNIFICANT DRIFT (behavior change detected)")

print("\n============================")




