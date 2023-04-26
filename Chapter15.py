import multiprocessing
import time
import random

#15.1
def worker():
    time.sleep(random.random())
    now = time.time()
    print(time.ctime(now))
    return

if __name__ == "__main__":

    processes = [multiprocessing.Process(target=worker) for i in range(3)]
        
    for process in processes:
        process.start()
        
    for process in processes:
        process.join()