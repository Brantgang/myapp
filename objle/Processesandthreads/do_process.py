from multiprocessing import Process
from multiprocessing import Pool
import os, time,random
def run_proc(name):
    print('run child process %s (%s).... ' % (name, os.getpid()))

#if __name__=='__main__':
#   print('Parent process %s.' % os.getpid())
#    p = Process(target=run_proc,args=('test',))
#    print('Child process will start')
#    p.start()
#    p.join()
#    print('Chlid process end %s.' % os.getpid())

def long_time_task(name):
    print('Run task(%s) time is %s.' %(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s is %0.2f seconds .' % (name,(end - start)))


if __name__ =='__main__':
    print('rum process(%s) is doing .' %(os.getpid()))
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('waiting for subprocess done...')
    p.close()
    p.join()
    print('All subprocess done')

