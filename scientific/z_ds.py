import random
import csv
import datetime

orderList, masterOrderList, recordList = [],[],[]
index,masterIndex, recordIndex =1,1,1

quanlist = ['1']*5 + ['2','3']
foodlist=['BG001','BG002','BG003','BG004','BG005','BG006','BG007','BG008','BG009','BG010','BG011']
pricelist=[30,20,24,22,12,12,12,12,18,15,30,90,90,100,100,80,60,70,90,90,90,10,12]
staffList=['1','2','3','7','8']
user=["emily","haha","gc28","CW2000","bwong"]
user_key=['29ds4k','7dck3i','2x3x4x','sejicnq','12583k']
admin=["katherine"]
admin_key=['ka123']

tableList=['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13','T14','T15','T16','T17','T18','T19','T20']


for day in range(5):
    master, recordTotal = 0,0
    randTimeList = [random.randint(0,30) for i in range(8)]
print(randTimeList)



tableList.append('x');
print(tableList)

string='hydrogen'
for index,letter in enumerate(string):
    print((letter,index))





















# for day in range(120):
#     count = random.randint(50,300)
#     master, recordTotal = 0,0
#     randTimeList = [random.randint(0,46800) for i in range(count)]
#     randTimeList.sort()
#     for _ in range(count): #each day loop master orders
#         times = random.randint(1,3)
#         total=0
#         for _ in range(times): # each master order loop orders
#             food_pos = random.randint(0,len(foodlist)-1)
#             total+=pricelist[food_pos]
#             order = [str(index),random.choice(quanlist),str(masterIndex),foodlist[food_pos],str(pricelist[food_pos])]
#             orderList.append(order)
#             index+=1
#         d_date_time = datetime.datetime(2017,11,6,8,0,0) + datetime.timedelta(days=day, seconds=(randTimeList[master]) )
#         getTime = d_date_time.strftime("%H:%M:%S")
#         getDate = d_date_time.strftime("%Y-%m-%d")
#         # masterOrderID,price,payment,change,staffID,ReportID,TableNo,checkoutTime,checkoutDate
#         masterRow = [str(masterIndex),str(total),str(total),'0',random.choice(staffList),str(day+1),random.choice(tableList),getTime,getDate]
#         masterOrderList.append(masterRow)
#         master += 1
#         masterIndex += 1
#         recordTotal += total
#     # reportID, income, DATE, count, staffID
#     recordRow = [str(recordIndex),str(recordTotal),getDate,str(master),str(random.choice(staffList))]
#     recordList.append(recordRow)
#     recordIndex+=1




