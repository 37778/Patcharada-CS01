Num=int(input('enter your loop:'))
NumTotal=[]
for i in range(Num):
    data=int(input('enter your data:'))
    NumTotal += [data]
print(NumTotal)
print(max(NumTotal))
print(min(NumTotal))