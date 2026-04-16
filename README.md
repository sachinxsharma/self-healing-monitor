# 🚀 Self-Healing Infrastructure Monitoring System

> 💡 A production-inspired DevOps project that not only monitors infrastructure but also **automatically heals failures** without human intervention.

---

## 📌 Overview

This project demonstrates a **complete monitoring + alerting + self-healing pipeline** using modern DevOps tools.

It continuously monitors system health (CPU, Memory, Disk, Containers) and:

✅ Detects failures  
✅ Sends alerts  
✅ Automatically fixes issues  
✅ Provides real-time dashboards  

---

## 🧠 Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/b52435e9-3dba-4f12-9d0c-e05ef25d3440" />


---

## ⚙️ Tech Stack

- 🐳 Docker & Docker Compose
- 📊 Prometheus (Monitoring)
- 📈 Grafana (Visualization)
- 🚨 Alertmanager (Alerting)
- 🖥️ Node Exporter (System Metrics)
- 🐍 Python (Self-Healing Automation)
- ☁️ AWS EC2 (Deployment)

---

## 🔥 Features

- 📊 Real-time CPU, RAM, Disk monitoring
- 🚨 Email alerts on threshold breach
- 🤖 Automatic container restart (Self-Healing)
- 🔁 Auto-start services on reboot (Cron)
- 📈 Interactive Grafana dashboards
- ⚡ Live failure simulation & recovery

---

## 📸 Screenshots

### 📊 Grafana Dashboard
- Real-time system metrics visualization

### 🚨 Alerts in Prometheus
- CPU, Memory, Disk alerts

### 🤖 Self-Healing Logs
- Automatic detection & recovery

---

## 🚀 How It Works

1. **Node Exporter** collects system metrics
2. **Prometheus** scrapes and stores data
3. **Alert rules** evaluate thresholds
4. **Alertmanager** sends email notifications
5. **Python script** detects failures and fixes them automatically
6. **Grafana** visualizes everything

---

## 🧪 Demo (How to Test)

### 🔥 Simulate CPU Spike
```bash
stress --cpu 4 --timeout 120

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/6802bfb4-f388-49b3-8995-b4bb2e3be47c" />

Simulate Failure
docker stop grafana

👉 Result:

System detects failure
Auto restarts container 🤖
Logs updated


⚙️ Setup Instructions
git clone https://github.com/sachinxsharma/self-healing-monitor.git
cd monitoring
docker-compose up -d

🧠 Key Concepts Learned
Infrastructure Monitoring
Alerting Systems
Self-Healing Automation
Docker Networking
PromQL Queries
DevOps Workflow
🎯 Use Cases
Cloud Infrastructure Monitoring
DevOps Automation
Production System Reliability
Incident Detection & Recovery

Author
Sachin Sharma

⭐ If you like this project
- Give it a ⭐ on GitHub!







