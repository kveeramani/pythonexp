import multiprocessing
import time

def worker(name):
    for i in range(3):
        print(f"[Process {name}] Working... {i}")
        time.sleep(1)

if __name__ == "__main__":
    processes = []
    for i in range(100):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Multiprocessing complete.")