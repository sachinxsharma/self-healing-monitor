import threading
import time
import logging
from datetime import datetime
import subprocess
import shutil
import os

# Setup logging
logging.basicConfig(
    filename='/home/ubuntu/monitoring/logs/master_healer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

MONITORED_CONTAINERS = ['prometheus', 'node-exporter', 'alertmanager', 'grafana']
DISK_THRESHOLD = 85
LOG_PATHS = ['/var/log', '/tmp']

# ── Container Watchdog ──
def get_running_containers():
    result = subprocess.run(
        ['docker', 'ps', '--format', '{{.Names}}'],
        capture_output=True, text=True
    )
    return result.stdout.strip().split('\n')

def restart_container(name):
    logging.warning(f"Container '{name}' DOWN. Restarting...")
    print(f"[{datetime.now()}] ⚠️  '{name}' is down. Restarting...")
    result = subprocess.run(['docker', 'restart', name], capture_output=True, text=True)
    if result.returncode == 0:
        logging.info(f"'{name}' restarted successfully.")
        print(f"[{datetime.now()}] ✅ '{name}' restarted.")
    else:
        logging.error(f"Failed to restart '{name}': {result.stderr}")
        print(f"[{datetime.now()}] ❌ Failed to restart '{name}'.")

def container_watchdog():
    logging.info("Container Watchdog thread started.")
    while True:
        running = get_running_containers()
        for container in MONITORED_CONTAINERS:
            if container not in running:
                restart_container(container)
            else:
                print(f"[{datetime.now()}] ✅ {container} running.")
        time.sleep(30)

# ── Disk Healer ──
def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    return round((used / total) * 100, 2)

def clean_logs():
    logging.warning("High disk usage. Cleaning logs...")
    print(f"[{datetime.now()}] ⚠️  High disk! Cleaning...")
    cleaned = 0
    for path in LOG_PATHS:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(('.log', '.gz', '.old')):
                    try:
                        fp = os.path.join(root, file)
                        size = os.path.getsize(fp)
                        os.remove(fp)
                        cleaned += size
                        print(f"[{datetime.now()}] 🗑️  Deleted {fp}")
                    except Exception as e:
                        logging.error(f"Error deleting {file}: {e}")
    print(f"[{datetime.now()}] ✅ Freed {round(cleaned/(1024*1024), 2)} MB.")

def disk_healer():
    logging.info("Disk Healer thread started.")
    while True:
        usage = get_disk_usage()
        print(f"[{datetime.now()}] 💾 Disk: {usage}%")
        if usage > DISK_THRESHOLD:
            clean_logs()
        time.sleep(60)

# ── Main ──
if __name__ == "__main__":
    print(f"[{datetime.now()}] 🚀 Master Healer starting...")
    logging.info("Master Healer started.")

    t1 = threading.Thread(target=container_watchdog, daemon=True)
    t2 = threading.Thread(target=disk_healer, daemon=True)

    t1.start()
    t2.start()

    print(f"[{datetime.now()}] ✅ All healers running. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n[{datetime.now()}] 🛑 Master Healer stopped.")
        logging.info("Master Healer stopped by user.")
