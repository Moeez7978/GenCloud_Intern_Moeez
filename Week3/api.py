import requests
import time

API_URL = "http://Sample_API_URl/metrics"

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 90
DISK_THRESHOLD = 85

def check_system():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()

        data = response.json()

        cpu = data.get("cpu", 0)
        memory = data.get("memory", 0)
        disk = data.get("disk", 0)
        service = data.get("service", "unknown")

        print("\n----- System Status -----")
        print(f"CPU: {cpu}%")
        print(f"Memory: {memory}%")
        print(f"Disk: {disk}%")
        print(f"Service: {service}")

        # Monitoring logic
        if cpu > CPU_THRESHOLD:
            print("⚠️ High CPU usage!")

        if memory > MEMORY_THRESHOLD:
            print("⚠️ High Memory usage!")

        if disk > DISK_THRESHOLD:
            print("⚠️ Disk almost full!")

        if service != "running":
            print("❌ Service is DOWN!")

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")

# Run continuously
while True:
    check_system()