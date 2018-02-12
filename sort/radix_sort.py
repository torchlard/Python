import copy

lists=[3221,1,10,9680,577,9420,7,5622,4793,2030,3138,82,2599,743,4127]


def num2dig(num,dig):
    if pow(10,dig)>num:
        return 0
    else:
        digits=list(reversed([int(i) for i in str(num)]))
        return digits[dig]

for index in range(4):
    result=[]
    tmp=[[] for i in range(10)]
    for j in lists:
        tmp[num2dig(j,index)].append(j)
    for a in tmp:
        for b in a:
            result.append(b)
    lists=copy.copy(result)
    print lists