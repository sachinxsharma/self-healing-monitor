import subprocess
import time
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename='/home/ubuntu/monitoring/logs/watchdog.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Containers we want to always keep running
MONITORED_CONTAINERS = [
    'prometheus',
    'node-exporter',
    'alertmanager',
    'grafana'
]

def get_running_containers():
    result = subprocess.run(
        ['docker', 'ps', '--format', '{{.Names}}'],
        capture_output=True, text=True
    )
    return result.stdout.strip().split('\n')

def restart_container(container_name):
    logging.warning(f"Container '{container_name}' is DOWN. Attempting restart...")
    print(f"[{datetime.now()}] ⚠️  Container '{container_name}' is down. Restarting...")
    
    result = subprocess.run(
        ['docker', 'restart', container_name],
        capture_output=True, text=True
    )
    
    if result.returncode == 0:
        logging.info(f"Container '{container_name}' successfully restarted.")
        print(f"[{datetime.now()}] ✅ Container '{container_name}' restarted successfully.")
    else:
        logging.error(f"Failed to restart '{container_name}': {result.stderr}")
        print(f"[{datetime.now()}] ❌ Failed to restart '{container_name}'.")

def watchdog_loop():
    print(f"[{datetime.now()}] 🚀 Watchdog started. Monitoring containers...")
    logging.info("Watchdog started.")
    
    while True:
        running = get_running_containers()
        
        for container in MONITORED_CONTAINERS:
            if container not in running:
                restart_container(container)
            else:
                print(f"[{datetime.now()}] ✅ {container} is running.")
        
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    watchdog_loop()
