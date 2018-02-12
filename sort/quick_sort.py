def swap(unsorted,i,j):
    tmp=unsorted[j]
    unsorted[j]=unsorted[i]
    unsorted[i]=tmp

def sorting(unsorted,a0,a1):
    current=unsorted[a0]
    flag=-1
    for i in range(a0,a1+1):
#         print unsorted,'i= ',i
        if (flag==-1 and current < unsorted[i]):
            flag = i
        if flag != -1:
            if (unsorted[i] < current):
                swap(unsorted,flag,i)
                flag += 1
    if flag==-1: 
        pivot = a1
    else:
        pivot = flag-1
    
    swap(unsorted,a0,pivot)
    print unsorted,'pivot= ',pivot
    if pivot-a0 > 1:
        sorting(unsorted,a0,pivot)
    if a1-(pivot+1) > 1:
        sorting(unsorted,pivot+1,a1)
    
    return unsorted
    
def real_sort():
    listing=[5,4,3,2,1,6,7,8,9]
    sorting(listing,0,len(listing)-1)

real_sort()