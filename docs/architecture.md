# SOC-Linux-Lab Architecture

## System Flow


[ System Activity ]
↓
[ json_monitor.sh ]
↓
[ telemetry.jsonl ]
↓
[ Python Analysis Layer ]
↓
[ Anomaly + Drift Detection ]
↓
[ Incident Engine ]
↓
[ SOC Dashboard / Reports ]


---

## Components

### 1. Collector
- Bash script
- captures system state periodically

### 2. Telemetry Store
- JSONL format
- append-only log system

### 3. Analysis Engine
- Python-based processing
- statistical evaluation

### 4. Detection System
- anomaly detection
- baseline comparison
- risk classification

### 5. Output Layer
- CLI dashboard
- incident reports
- alert engine

---

## Design Philosophy

- Local-first security monitoring
- Minimal dependencies
- Transparent data flow
- Educational SOC simulation model



