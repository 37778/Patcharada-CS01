a=int(input("work score: "))
b=int(input("midterm :"))
c=int(input("final :"))
d=a+b+c
if d >= 80:
    print("A")
elif d >= 75:
    print("B+")
elif d >= 70:
    print("B")
elif d >= 65:
    print("C+")
elif d >= 60:
    print("C")  
elif d >= 55:
    print("D+")
elif d >= 50:
    print("D")
else:
    print("F")