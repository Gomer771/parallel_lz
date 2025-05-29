import threading
import time

counter = 0
lock = threading.Lock()

def increment_counter(thread_old):
    global counter
    
    with lock:
        counter += 1000

        start_time = time.time()  
        end_time = time.time()
        final = end_time - start_time
        print(f"Поток {thread_old} увеличил счетчик на 1000. Время выполнения: {final:} сек")
        
threads = []
for i in range(10):
    
    thread = threading.Thread(target=increment_counter, args=(i,))
    threads.append(thread)
    thread.start()
    time.sleep(0.1)

for thread in threads:
    thread.join()

print(f"Конечное значение счетчика: {counter}")





