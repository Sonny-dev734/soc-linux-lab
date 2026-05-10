import json
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

telemetry_file = os.path.join(BASE_DIR, "telemetry", "telemetry.jsonl")

def load_events():
    events = []
    with open(telemetry_file, "r") as f:
        for line in f:
            try:
                events.append(json.loads(line))
            except:
                pass
    return events

def classify(event):
    c = event["connections"]

    if c < 10:
        return "INFO"
    elif c < 20:
        return "LOW"
    elif c < 40:
        return "MEDIUM"
    else:
        return "HIGH"

def print_alert(event, level):
    print("\n==============================")
    print("SOC REAL-TIME ALERT")
    print("==============================")
    print(f"Time      : {event['timestamp']}")
    print(f"Process   : {event['top_process']}")
    print(f"Connections: {event['connections']}")
    print(f"State     : {event['state']}")
    print(f"Severity  : {level}")
    print("==============================\n")

def main():

    print("SOC ALERT ENGINE STARTED")
    print("Monitoring telemetry stream...\n")

    seen = set()

    while True:

        events = load_events()

        for e in events:

            key = e["timestamp"]

            if key in seen:
                continue

            seen.add(key)

            level = classify(e)

            if level in ["MEDIUM", "HIGH"]:
                print_alert(e, level)

        time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] SOC Alert Engine stopped cleanly (user interrupt)")





