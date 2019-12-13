from tkinter import *
from tkinter.ttk import *
from pymysql import *

con = connect("127.0.0.1","root","ravi","pizzaproject")

class viewpizza:
    def __init__(self):
        global con
        cr= con.cursor()
        self.root = Tk()
        self.tr = Treeview(self.root,columns=("PID","p_name","MRP","Discount","Disprice","categoryname"))
        self.tr.heading("PID",text="PID")
        self.tr.heading("p_name", text="Pizza Name")
        self.tr.heading("MRP", text="MRP")
        self.tr.heading("Discount", text="Discount")
        self.tr.heading("Disprice", text="Disprice")
        self.tr.heading("categoryname", text="Category Name")
        self.tr['show']="headings"
        s = "select * from add_pizza"
        cr.execute(s)
        res = cr.fetchall()
        count=0
        for row in res:
            self.tr.insert("",index=count,values=row)
            count+=1
        self.tr.pack()
        self.root.mainloop()
#viewpizza()

