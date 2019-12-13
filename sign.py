import random
from tkinter import *
from tkinter.messagebox import *
from pymysql import *

con = connect("127.0.0.1", "root", "ravi", "pizzaproject")

class sign:
    def sign1(self):
        print("hello")
        if self.ans1.get()=="" or self.ans2.get()=="" or self.ans3.get()=="":
            showwarning("PizzaProject","All fields are mandatory to fill")
        else:
            x=random.random()
            y=int(x*1000000)
            cr = con.cursor()
            s = "insert into admin values ('"+self.ans2.get()+"','"+str(y)+"','"+self.ans1.get()+"','"+self.ans3.get()+"')"
            print(s)
            re = cr.execute(s)
            con.commit()
            if re==1:
                showinfo("Pizza Project", "SignUp Sucessfully...........\nPassword:"+str(y))


    def clear(self):
        self.ans1.set("")
        self.ans2.set("")
        self.ans3.set("")

    def __init__(self):
        self.root = Tk()
        self.ans1 = StringVar()
        self.ans2 = StringVar()
        self.ans3 = StringVar()
        self.root.geometry("550x300+400+100")
        self.root.resizable(0,0)
        img = PhotoImage(file="istockphoto-932621316-612x612.png")
        Label(self.root, image=img).place(x=0, y=0)
        self.root.configure(background="#ffffe6")
        self.lb1 = Label(self.root,text="New Pizza Member Signup",font=("Times Roman",16),fg="#000000",bg="#ccffff",padx=160)
        self.lb2 = Label(self.root,text="Name",font=("Times Roman",16),fg="blue",bg="#ffffe6")
        self.lb3 = Label(self.root,text="UserName",font=("Times Roman",16),fg="blue",bg="#ffffe6")
        self.lb1.place(x=0,y=0)
        self.lb2.place(x=10,y=60)
        self.lb3.place(x=10,y=110)
        self.tb1 = Entry(self.root,font=("Times Roman",16), textvariable=self.ans1)
        self.tb1.place(x=150,y=60)
        self.tb2 = Entry(self.root,font=("Times Roman",16), textvariable=self.ans2)
        self.tb2.place(x=150,y=110)

        self.lb4 = Label(self.root,text="Contact",font=("Times Roman",16),fg="blue",bg="#ffffe6")
        self.lb4.place(x=10,y=160)
        self.tb3 = Entry(self.root,font=("Times Roman",16), textvariable=self.ans3)
        self.tb3.place(x=150,y=165)
        self.bt1 = Button(self.root,text="Submit", bg="#fafad1",fg="#000000",font=("Times Roman",12), command=self.sign1)
        self.bt2 = Button(self.root,text="Clear", bg="#fafad1",fg="#000000",font=("Times Roman",12), command=self.clear)
        self.bt3 = Button(self.root,text="Exit", bg="#fafad1",fg="#000000",font=("Times Roman",12), command=self.root.destroy)
        self.bt1.place(x=150,y=205)
        self.bt2.place(x=230,y=205)
        self.bt3.place(x=310,y=205)
        self.root.mainloop()
if __name__ == '__main__':
    sign()
