import logging
import time
import threading
import random
import multiprocessing
from multiprocessing import Process,Queue

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

# def worker(start, end):
#     result = 0
#     # print(start,end)
#     logging.debug(str(start)+","+str(end))
#     print(threading.currentThread().getName(),'starting')
#     for i in range(start, end):
#         result += i
#     output.append(result)
#     print(threading.currentThread().getName(),'exiting')
#     return
# 
# output = []
# for i in range(4):
#     t = threading.Thread(name='thread-'+str(i), target=worker, args=( i*25,(i+1)*25 ))
#     t.start()

# ====== daemon threads ==========
# def worker():
#     t = threading.currentThread()
#     pause = random.randint(1,5)
#     logging.debug('sleeping %s', pause)
#     time.sleep(pause)
#     logging.debug('ending')
#     return
# 
# for i in range(3):
#     t = threading.Thread(target=worker)
#     t.setDaemon(True)
#     t.start()
# 
# main_thread = threading.currentThread()
# for t in threading.enumerate():
#     if t is main_thread:
#         continue
#     logging.debug('joining %s', t.getName())
#     # daemon thread for service does not lose work by interrupt
#     t.join()

# ====== event ==========
# def wait_for_event(e):
#     logging.debug('wait_for_event start')
#     event_is_set = e.wait()
#     logging.debug('event is set %s', event_is_set)
# 
# def wait_for_event_timeout(e, t):
#     while not e.isSet():
#         logging.debug('wait_for_event_timeout start')
#         event_is_set = e.wait(t)
#         logging.debug('event set: %s', event_is_set)
#         if event_is_set:
#             logging.debug('processing event')
#         else:
#             logging.debug('doing other work')
# 
# e = threading.Event()
# t1 = threading.Thread(name='block', target=wait_for_event, args=(e,))
# t1.start()
# # wait for event to complete, and then run; every t seconds check for event
# t2 = threading.Thread(name='non-block', target=wait_for_event_timeout, args=(e,1))
# t2.start()
# 
# logging.debug('wait before calling Event.set()')
# time.sleep(3)
# e.set()
# logging.debug('event is set')

# ########### synchronizing threads ############
# def consumer(cond):
#     # wait for condition and use resource
#     logging.debug('starting consumer thread')
#     t = threading.currentThread()
#     with cond:
#         cond.wait()
#         logging.debug('resource is available to consumer')
# 
# def producer(cond):
#     # set up resource used by consumer
#     logging.debug('starting producer thread')
#     with cond:
#         logging.debug('starting producer thread')
#         cond.notifyAll()
# 
# condition = threading.Condition()
# c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
# c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
# p = threading.Thread(name='p', target=producer, args=(condition,))
# 
# c1.start()
# time.sleep(2)
# c2.start()
# time.sleep(2)
# p.start()

# ########## Multi-processing ################3
output = []
def worker(start, end):
    result = 0
    print(start,end)
    logging.debug(str(start)+","+str(end))
    print(multiprocessing.current_process().name,'starting')
    for i in range(start, end):
        result += i
    output.append(result)
    print(result)
    return

steps = 10000
if __name__=='__main__':
    for i in range(5):
        p = multiprocessing.Process(name='thread-'+str(i), target=worker, args=(i*steps, (i+1)*steps))
        p.start()

# def f(q):
#     q.put([42, None, 'hello'])
# if __name__=='__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()



