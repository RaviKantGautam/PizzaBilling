from tkinter import *
import datetime
from tkinter.ttk import Treeview
from pymysql import *

con = connect("127.0.0.1","root","ravi","pizzaproject")

class dailybill:
    def __init__(self):
        global con
        self.window = Tk()
        self.window.title("Daily Bill")
        self.window.geometry("1140x400")
        self.window.configure(bg='skyblue')
        img = PhotoImage(file="alpine_pizza_32132_16x9.png")
        Label(self.window, image=img).place(x=0, y=0)

        # this code is for entry box
        d = datetime.datetime.now()
        self.todaysday_lb = Label(self.window,text="Today:"+str(d.date()),font=('Arial',18),bg="#ffffe6").grid(row=0,column=0,ipadx=10,pady=30,padx=10,ipady=5)


        self.tr = Treeview(self.window,
                           columns=("id", "date1", "total", "gst", "netamount", "customername", "mobileno", "email"))
        self.tr.column("0", width=130)
        self.tr.column("1", width=130)
        self.tr.column("2", width=130)
        self.tr.column("3", width=130)
        self.tr.column("4", width=130)
        self.tr.column("5", width=130)
        self.tr.column("6", width=130)
        self.tr.column("7", width=180)

        self.tr.heading("id", text="ID")
        self.tr.heading("date1", text="Date")
        self.tr.heading("total", text="Total")
        self.tr.heading("gst", text="GST")
        self.tr.heading("netamount", text="Net Amount")
        self.tr.heading("customername", text="Customer Name")
        self.tr.heading("mobileno", text="Mobile No.")
        self.tr.heading("email", text="Email")
        self.tr['show'] = "headings"

        cr = con.cursor()
        s = "select * from billtable where date1='" + str(d.date()) + "'"
        print(s)
        cr.execute(s)
        res = cr.fetchall()
        print(list(res))

        for child in self.tr.get_children():
            self.tr.delete(child)

        count = 0
        for i in res:
            self.tr.insert('', index=count, values=i)
            count += 1


        self.tr.grid(row=1, column=0, columnspan=6, ipadx=10, pady=30, padx=10, ipady=5)
        # self.close = Button(self.window, text="Cancel", command=self.window.destroy, width=15, height=3, bd=10).grid(
        #     row=2, column=2)

        self.window.mainloop()
if __name__ == '__main__':
    dailybill()