import threading
import time

def worker(name):
    for i in range(3):
        print(f"[Thread {name}] Working... {i}")
        time.sleep(10)

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# This code will work in parallel along with the main threads
print  ("Threads started, waiting for them to complete...")

# Wait for all threads to complete

for t in threads:
    t.join()

print("Multithreading complete.")
