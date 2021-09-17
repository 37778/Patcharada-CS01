from tkinter import 
root = Tk()
root.title("First GUI")
myText = Label (text="My name is",fg= "blue" ,font=20), .grid(row=0,column=0)
myText = Label (text="Patcharada",fg= "green" ,font=20), .grid(row=0,column=1)
myText = Label (text="Tawaditap",fg= "red" ,font=20), .grid(row=0,column=2)
root.geometry("300x300")
root.mainloop()