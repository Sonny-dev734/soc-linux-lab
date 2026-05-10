import json
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
telemetry_file = os.path.join(BASE_DIR, "telemetry", "telemetry.jsonl")

def get_last_event():
    try:
        with open(telemetry_file, "r") as f:
            lines = f.readlines()
            if not lines:
                return None
            return json.loads(lines[-1])
    except:
        return None

def classify(c):
    if c < 10:
        return "NORMAL"
    elif c < 20:
        return "LOW"
    elif c < 40:
        return "MEDIUM"
    else:
        return "HIGH"

while True:
    event = get_last_event()

    print("\033c", end="")  # clear screen

    print("===================================")
    print("        SOC LIVE DASHBOARD")
    print("===================================\n")

    if not event:
        print("Waiting for telemetry data...\n")
        time.sleep(2)
        continue

    severity = classify(event["connections"])

    print(f"Time       : {event['timestamp']}")
    print(f"Connections: {event['connections']}")
    print(f"Listening  : {event['listening_ports']}")
    print(f"Process    : {event['top_process']}")
    print(f"State      : {event['state']}")
    print(f"Severity   : {severity}")

    print("\n-----------------------------------")

    if severity == "NORMAL":
        print("SYSTEM STATUS: STABLE")
    elif severity == "LOW":
        print("SYSTEM STATUS: MINOR ACTIVITY")
    elif severity == "MEDIUM":
        print("SYSTEM STATUS: MONITOR CLOSELY")
    else:
        print("SYSTEM STATUS: POTENTIAL RISK")

    print("\n(CTRL+C to exit cleanly)")

    time.sleep(2)





