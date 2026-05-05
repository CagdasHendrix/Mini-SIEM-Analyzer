# 🛡️ Mini-SIEM-Analyzer

A lightweight, real-time Security Information and Event Management (SIEM) simulation tool developed in Python. This project demonstrates log analysis, pattern matching, and threat detection capabilities.

## 🌟 Key Features
- **Real-Time Log Tracking:** Monitors system/application logs as they are generated using non-blocking I/O.

- **Threat Detection Engine:**
  - **SQL Injection (SQLi):** Detects malicious patterns like `UNION SELECT`, `1=1`, and encoded payloads.
  - **Brute Force Detection:** Tracks failed login attempts from unique IP addresses and triggers alerts based on configurable thresholds.
- **Automated Simulation:** Includes a "Red Team" script to generate realistic attack scenarios for testing.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Core Modules:** `re` (Regex), `collections`, `os`, `time`
- **Logic:** Follows the "tail -f" operational principle for high performance and low memory footprint.

## 📸 Screenshots
<img width="2558" height="1368" alt="Ekran görüntüsü 2026-05-05 225423" src="https://github.com/user-attachments/assets/99d79cce-6cf1-415c-98d0-e8431220fdeb" />

## 🚀 How to Use
1. **Clone the repository:**
   
```bash
   git clone [https://github.com/CagdasHendrix/Mini-SIEM-Analyzer.git](https://github.com/CagdasHendrix/Mini-SIEM-Analyzer.git)
   cd Mini-SIEM-Analyzer
