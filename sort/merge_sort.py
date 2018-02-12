import Queue
import copy

unsorted=[161, 41, 80, 72, 18, 146, 43, 118, 63, 124, 193, 34, 
          154, 15, 71, 82, 98, 200, 62, 47, 198, 73, 48, 117, 121, 97, 77, 91, 23, 199, 85, 44]

def merge(list01,list02):
    q1=Queue.Queue(); q2=Queue.Queue()
    result=[]
    for i in list01:
        q1.put(i)
    for i in list02:
        q2.put(i)
    while not (q1.empty()) and not(q2.empty()):
        if (q1.queue[0]<q2.queue[0]):
            result.append(q1.get())
        else:
            result.append(q2.get())
    while not q2.empty():
        result.append(q2.get())
    while not q1.empty():
        result.append(q1.get())
    
    return result

def sorting(unsorted):
    level=1
    while (level < len(unsorted)):
        tmp=[]
        for i in range(0,len(unsorted),level*2):
            for j in merge(unsorted[i:i+level],unsorted[i+level:i+level*2]):
                tmp.append(j)
        unsorted=copy.copy(tmp)
        level*=2
    return unsorted

print sorting(unsorted)