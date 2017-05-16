import time,threading
balance=0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    print('Thread %s ,  balance is +++%d'%(threading.current_thread().name,balance))


def run_thread(n):
    for i in range(10000):
        change_it(n)

print(time.time())
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
print(time.process_time())