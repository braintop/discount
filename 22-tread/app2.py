import time
import threading

def worker(id):
    for i in range(3):
        print(f"Worker {id} is working... {i}")
        time.sleep(1)

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All workers have finished their work")