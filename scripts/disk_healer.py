import shutil
import os
import logging
import time
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename='/home/ubuntu/monitoring/logs/disk_healer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DISK_THRESHOLD = 85  # Trigger cleanup if disk usage goes above 85%

LOG_PATHS = [
    '/var/log',
    '/tmp'
]

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    return round(percent_used, 2)

def clean_old_logs():
    logging.warning("Disk usage high! Starting cleanup...")
    print(f"[{datetime.now()}] ⚠️  Disk usage high! Cleaning old logs...")
    
    cleaned = 0
    
    for path in LOG_PATHS:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.log') or file.endswith('.gz') or file.endswith('.old'):
                    try:
                        full_path = os.path.join(root, file)
                        size = os.path.getsize(full_path)
                        os.remove(full_path)
                        cleaned += size
                        logging.info(f"Deleted: {full_path} ({size} bytes)")
                        print(f"[{datetime.now()}] 🗑️  Deleted: {full_path}")
                    except Exception as e:
                        logging.error(f"Could not delete {file}: {e}")
    
    cleaned_mb = round(cleaned / (1024 * 1024), 2)
    logging.info(f"Cleanup complete. Freed {cleaned_mb} MB.")
    print(f"[{datetime.now()}] ✅ Cleanup done. Freed {cleaned_mb} MB.")

def disk_healer_loop():
    print(f"[{datetime.now()}] 🚀 Disk Healer started.")
    logging.info("Disk Healer started.")
    
    while True:
        usage = get_disk_usage()
        print(f"[{datetime.now()}] 💾 Disk usage: {usage}%")
        
        if usage > DISK_THRESHOLD:
            clean_old_logs()
        else:
            logging.info(f"Disk usage normal: {usage}%")
        
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    disk_healer_loop()
