import time
from multiprocessing import Pool, Lock, Manager

def task(start):
    sub_sum = 0
    for i in range(start):
        sub_sum += i
    print(sub_sum)
    result.append(sub_sum)

# def init(l):
#     global lock
#     lock = l


global result
if __name__ == "__main__":
    t = 0
    factor = 10
    data1 = [1*factor,2*factor,3*factor,4*factor]
    # try:
    start = time.time()
    
    manager = Manager()
    result = manager.list([])
    pool = Pool(4)
    tofs = pool.map(task, data1)
    pool.close()
    pool.join()
    
    # result = []
    # for i in data1:
    #     task(i)
    
    end = time.time()
    t = end-start

    print('time used: ',t)
    print(result)
    print(sum(result))
    # finally:
    #     pass