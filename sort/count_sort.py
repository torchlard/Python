listing=[5,15,6,5,28,16,4,2,3,3,3,2,5,2,8,9,9,4,7,1]

set_list=list(set(listing))
n=len(set_list)
count=[0]*n
result=[]

for i in listing:
    for j in range(n):
        if (i==set_list[j]):
            count[j]+=1
for i in range(n):
    number=set_list[i]
    for j in range(count[i]):
        result.append(number)
print result