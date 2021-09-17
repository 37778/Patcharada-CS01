from tkinter import *
root = Tk()
root.title("calculator")

#แสดงผล 5*4
display = Entry(font=('arial',30,'bold'),fg="white",bg="green")
display.grid(columnspan=4)

#รับค่าผ่านปุ่ม

#row1
btn7=Button(fg="black",font=('arial',30,'bold'),text="7",padx=30,pady=15).grid(row=1,column=0)
btn8=Button(fg="black",font=('arial',30,'bold'),text="8",padx=30,pady=15).grid(row=1,column=1)
btn9=Button(fg="black",font=('arial',30,'bold'),text="9",padx=30,pady=15).grid(row=1,column=2)
btnC=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="C",padx=30,pady=15).grid(row=1,column=3)

#row2
btn4=Button(fg="black",font=('arial',30,'bold'),text="4",padx=30,pady=15).grid(row=2,column=0)
btn5=Button(fg="black",font=('arial',30,'bold'),text="5",padx=30,pady=15).grid(row=2,column=1)
btn6=Button(fg="black",font=('arial',30,'bold'),text="6",padx=30,pady=15).grid(row=2,column=2)
btnplus=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="+",padx=30,pady=15).grid(row=2,column=3)

#row3
btn1=Button(fg="black",font=('arial',30,'bold'),text="1",padx=30,pady=15).grid(row=3,column=0)
btn2=Button(fg="black",font=('arial',30,'bold'),text="2",padx=30,pady=15).grid(row=3,column=1)
btn3=Button(fg="black",font=('arial',30,'bold'),text="3",padx=30,pady=15).grid(row=3,column=2)
btnminus=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="-",padx=30,ady=15).grid(row=3,column=3)

#row4
btndot=Button(fg="black",bg="orange",font=('arial',30,'bold'),text=".",padx=30,pady=15).grid(row=4,column=0)
btn0=Button(fg="black",font=('arial',30,'bold'),text="0",padx=30,pady=15).grid(row=4,column=1)
btndivision=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="/",padx=30,pady=15).grid(row=4,column=2)
btnmultiply=Button(fg="black",bg="orange",font=('arial',30,'bold'),text="*",padx=30,pady=15).grid(row=4,column=3)

#row5
btnequal=Button(fg="black",font=('arial',30,'bold'),text="=",padx=30,pady=15).grid(row=5,column=0)
btnopen=Button(fg="black",font=('arial',30,'bold'),text="(",padx=30,pady=15).grid(row=5,column=1)
btnclose=Button(fg="black",font=('arial',30,'bold'),text=")",padx=30,pady=15).grid(row=5,column=2)

root.mainloop()