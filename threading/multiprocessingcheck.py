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

# You can create 100 processes also in a 8 core machine, but they will not run in parallel due to Core limitations. 
# But context switching will help in trying to run them in parallel.
# There is no true CPU hold processing. we can try to make it so much intenstive only, not 100%