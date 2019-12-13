from tkinter import *
from tkinter.ttk import Treeview
from pymysql import *
import datetime
from tkcalendar import *


con = connect("127.0.0.1","root","ravi","pizzaproject")



class report:
    def showit(self):
        try:
            global con
            dt1 = self.fromdate.get()
            dt1 = datetime.datetime.strptime(dt1,'%m/%d/%y').strftime('%Y-%m-%d')
            dt2 = self.todate.get()
            dt2 = datetime.datetime.strptime(dt2,'%m/%d/%y').strftime('%Y-%m-%d')

            print(dt1)
            print(dt2)

            cr = con.cursor()
            s = "select * from billtable where date1>='"+str(dt1)+"' and date1<='"+str(dt2)+"'"
            print(s)
            cr.execute(s)
            res = cr.fetchall()
            print(list(res))

            for child in self.tr.get_children():
                self.tr.delete(child)

            count = 0
            for i in res:
                self.tr.insert('',index=count,values=i)
                count+=1
        except Exception as e:
            print(e)

    def __init__(self):
        self.window = Tk()
        self.window.title("Report")
        #self.window.geometry("900x500+200+100")
        self.window.resizable(0,0)
        img = PhotoImage(file="57635230-portrait-of-an-happy-couple-they-are-laughing-and-eating-pizza-and-having-a-great-time-.png")
        Label(self.window, image=img).place(x=0, y=0)

        #this code is for labels
        self.todaysday_lb = Label(self.window,text="From",font=('Arial',18)).grid(row=0,column=0,ipadx=10,pady=30,padx=10,ipady=5)
        self.day_lb = Label(self.window,text="To",font=('Arial',18)).grid(row=0,column=2,ipadx=10,pady=30,padx=10,ipady=5)

        # this code is for entry box
        d = datetime.datetime.now()
        self.ans = StringVar()
        self.ans.set(str(d.date()))
        self.fromdate = DateEntry(self.window,textvariable=self.ans,font=('Arial',12))
        self.fromdate.grid(row=0, column=1,ipadx=5,pady=30,padx=10,ipady=5)
        self.todate = DateEntry(self.window)
        self.todate.grid(row=0, column=3,ipadx=10,pady=30,padx=10,ipady=5)

        # this code is for button
        self.showme = Button(self.window,text="Show",command=self.showit,bd=10,width=10).grid(row=0, column=4,ipadx=10,pady=20,padx=20,ipady=5)
        self.tr = Treeview(self.window,
                           columns=("id", "date1", "total", "gst", "netamount", "customername", "mobileno", "email"))
        self.tr.column("0",width=130)
        self.tr.column("1",width=130)
        self.tr.column("2",width=130)
        self.tr.column("3",width=130)
        self.tr.column("4",width=130)
        self.tr.column("5",width=130)
        self.tr.column("6",width=130)
        self.tr.column("7",width=180)


        self.tr.heading("id", text="ID")
        self.tr.heading("date1", text="Date")
        self.tr.heading("total", text="Total")
        self.tr.heading("gst", text="GST")
        self.tr.heading("netamount", text="Net Amount")
        self.tr.heading("customername", text="Customer Name")
        self.tr.heading("mobileno", text="Mobile No.")
        self.tr.heading("email", text="Email")
        self.tr['show'] = "headings"


        self.tr.grid(row=1, column=0,columnspan=6,ipadx=10,pady=30,padx=10,ipady=5)
        self.close = Button(self.window, text="Cancel", command=self.window.destroy,width=15,height=3,bd=10).grid(row=2,column=2)



        self.window.mainloop()
if __name__ == '__main__':
    report()