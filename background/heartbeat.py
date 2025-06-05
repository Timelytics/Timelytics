import time

def start_heartbeat():
    print("💓 Heartbeat monitoring started.")
    for i in range(5):
        print("Pulse", i + 1)
        time.sleep(1)

if __name__ == "__main__":
    start_heartbeat()