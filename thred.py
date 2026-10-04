import threading
import time 

def task_given():
    print("thread is started")
    time.sleep(10)
    
t1 = threading.Thread(target=task_given)
t2 = threading.Thread(target=task_given)

t1.start()
t2.start()

t1.join()
t2.join()

print('threads completed')