import multiprocessing
import time

def worker(name):
    print(f"[Process {name}] Starting CPU work for 10 seconds")
    start = time.time()
    x = 0
    while time.time() - start < 10:
        x += 1  # Simple increment, keeps CPU busy
    print(f"[Process {name}] Done. Loop count: {x}")

if __name__ == "__main__":
    start_time = time.time()  # Start timer

    processes = []
    for i in range(50):  # Use a small number to avoid overloading your system
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()  # End timer
    print("Multiprocessing complete.")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")


# Running 50 process has taken 29.78 seconds. 
# Running anything less than 8 processes has taken 10 seconds.
# It is not in a batch of 8 processes, the time taken is based on the CPU context switching.

