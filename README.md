# SOC-Linux-Lab

## 1. Project Overview

SOC-Linux-Lab is a local Security Operations Center (SOC) simulation framework designed to replicate the core principles of endpoint security monitoring, telemetry analysis, and incident detection in a controlled Linux environment.

The objective of this project is not to provide production-grade security tooling, but to model how SOC pipelines operate conceptually and technically: from raw system telemetry acquisition to anomaly detection and structured incident reporting.

This system is intentionally built in a lightweight and transparent manner using Bash scripting and Python in order to emphasize logic, data flow, and security reasoning rather than external dependencies or complex infrastructure.

---

## 2. Motivation and Educational Purpose

Modern cybersecurity operations rely heavily on continuous monitoring systems that collect system-level telemetry, analyze behavioral patterns, and detect deviations from expected baselines.

This project was developed to understand and reproduce these principles in a simplified environment. The motivation is to bridge the gap between theoretical cybersecurity knowledge and operational SOC workflows by implementing a full detection pipeline locally.

Key learning objectives include:
- Understanding how telemetry is collected from an operating system
- Learning how behavioral baselines are computed and interpreted
- Exploring statistical anomaly detection techniques
- Simulating incident generation and classification logic
- Structuring a complete SOC-style data pipeline

---

## 3. System Architecture

The system follows a sequential security monitoring pipeline inspired by real SOC environments:

System Activity (Linux Kernel Level)
        ↓
Telemetry Collection Layer (Bash Scripts)
        ↓
Structured Logging (JSONL Format)
        ↓
Data Processing Layer (Python)
        ↓
Statistical Analysis (Baseline + Drift Detection)
        ↓
Anomaly Detection Engine
        ↓
Incident Classification Engine
        ↓
SOC Monitoring Dashboard (Real-Time CLI View)

Each layer is intentionally decoupled to reflect modular SOC architecture principles, where ingestion, analysis, detection, and visualization operate independently.

---

## 4. Functional Description

### 4.1 Telemetry Collection
The system collects periodic snapshots of Linux system activity including:
- Active network connections
- Listening ports
- Process-level activity indicators

This data is structured and stored in a JSONL format to allow incremental processing and time-series analysis.

---

### 4.2 Analysis and Baseline Modeling
The Python analysis layer computes statistical baselines such as:
- Average system connections over time
- Variance and deviation from normal behavior
- Process frequency distribution

This allows the system to define what “normal behavior” means dynamically rather than using static thresholds.

---

### 4.3 Anomaly Detection Logic
Anomalies are detected using deviation-based logic derived from the computed baseline. If system behavior diverges significantly from expected statistical norms, the system flags this as potential abnormal activity.

---

### 4.4 Incident Engine
Detected anomalies are converted into structured incident reports. Each incident is classified into severity levels (LOW / MEDIUM / HIGH) based on deviation magnitude and system state context.

---

### 4.5 SOC Dashboard
A real-time terminal interface provides continuous monitoring of system state, simulating a Security Operations Center visualization layer used by analysts to observe ongoing system behavior.

---

## 5. Security and Ethical Scope

This project is strictly limited to local system observation and defensive analysis.

It does NOT:
- Perform network scanning or external probing
- Interact with remote systems or third-party servers
- Execute offensive security operations
- Modify external environments beyond the host machine

All operations remain confined to the local environment for educational purposes only.

---

## 6. Responsibility Disclaimer

This software is provided strictly for educational, research, and portfolio demonstration purposes.

The author assumes no responsibility for any misuse, misconfiguration, or unintended consequences arising from the use of this project.

Users are expected to operate the system in a controlled environment and ensure compliance with applicable laws and institutional policies.

---

## 7. Technologies Used

- Python 3 (data processing and analysis)
- Bash scripting (system telemetry collection)
- Linux system utilities (process and network inspection)
- JSONL structured logging format

---

## 8. Author Intent

This project was developed as a cybersecurity learning exercise to simulate SOC operations and improve understanding of real-world monitoring and detection systems.

It is intended to demonstrate:
- Security engineering thinking
- System design capability
- Data-driven anomaly detection logic
- Understanding of SOC workflows

