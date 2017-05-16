import threading,time

lock1=threading.Lock()
def task1():
    lock1.acquire()
 #   try:
    for i in range(10):
        print('excute task1...')
   # finally:
    #    lock1.release()
def task2():
    for i in range(10):
        print('excute task2...')




t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()