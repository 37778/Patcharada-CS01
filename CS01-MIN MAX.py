Num=int(input('enter your loop:'))
NumTotal=[]
for i in range(Num):
    data=int(input('enter your data:'))
    NumTotal += [data]
print(NumTotal)
print("M =",max(NumTotal))
print("m =",min(NumTotal))