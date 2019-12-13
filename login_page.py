from first_page import *
from pymysql import *
from tkinter import *
from sign import sign
from tkinter.messagebox import *

con = connect("127.0.0.1", "root", "ravi", "pizzaproject")


class logmein:
    def logme(self):
        global con
        us = self.u.get()
        ps = self.p.get()
        cr = con.cursor()
        s = "select * from admin"
        cr.execute(s)
        res = cr.fetchall()
        print(res)
        con.commit()
        t = []
        p = []
        for j in range(0,len(res)):
            t.append(res[j][0])
            p.append(res[j][1])
        print(t)
        print(p)
        if us=="" or ps=="":
            showwarning("Pizzaproject", "Please Fill All Field")
        elif us  in t and ps in p:
            showinfo("Yipee", "Login Successful")
            self.root.destroy()
            first_page()
            pass
        else:
            showerror("Pizzaproject", "Wrong username or password")
            self.u.set("")
            self.p.set("")


    def signup(self):
        self.root.destroy()
        sign()
        logmein()
    def __init__(self):
        self.root = Tk()
        self.root.title("Login Page")
        # self.root.geometry("500x300+420+120")
        self.root.resizable(0, 0)
        #self.root.wm_attributes('-alpha',0.7)     #this code is for only optical fading the whole background of the window
        img = PhotoImage(file="istockphoto-932621316-612x612.png")
        Label(self.root, image=img).place(x=0, y=0)
        self.u = StringVar()
        self.user_lb = Label(self.root, text="Username", font=('Arial', 18)).grid(row=0, column=0, ipadx=10, pady=30, padx=10,
                                                                        ipady=5)
        self.user_Entry = Entry(self.root, textvariable=self.u, font=("bold", 18)).grid(row=0, column=1, ipadx=10, pady=30, padx=15,
                                                                         ipady=5)

        self.p = StringVar()
        self.password_lb = Label(self.root, text="Password", font=('Arial', 18)).grid(row=1, column=0, ipadx=10, pady=30, padx=10,
                                                                            ipady=5)
        self.password_Entry = Entry(self.root, textvariable=self.p, font=("bold", 18),show="*").grid(row=1, column=1, ipadx=10, pady=30,
                                                                             padx=10, ipady=5)

        self.login = Button(self.root, text="Login", font=('Arial', 18), command=self.logme, bd=5, activebackground="lightgreen").grid(
            row=2, pady=10, column=0, ipadx=10, padx=3, ipady=1)
        self.signup = Button(self.root, text="Signup", font=('Arial', 18), command=self.signup, bd=5, activebackground="lightgreen").grid(
            row=2, pady=2, column=1, ipadx=10, padx=3, ipady=1)
        self.close = Button(self.root, text="Cancel", font=('Arial', 18), command=quit, bd=5, activebackground="crimson").grid(
            row=2, column=2, ipadx=10, pady=50, padx=10, ipady=1)
        self.root.mainloop()
if __name__ == '__main__':
    logmein()