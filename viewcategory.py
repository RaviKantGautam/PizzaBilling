from tkinter import *
from tkinter.ttk import *
from pymysql import *
#from tkinter.messagebox import *

con = connect("127.0.0.1","root","ravi","pizzaproject")

class viewcategory:
    def __init__(self):
        global con
        cr= con.cursor()
        self.root = Tk()
        self.tr = Treeview(self.root,columns=("CategoryNameEntry","DescriptionEntry"))
        self.tr.heading("CategoryNameEntry",text="Category Name")
        self.tr.heading("DescriptionEntry", text="Category Description")
        self.tr['show']="headings"
        s = "select * from categorytable"
        cr.execute(s)
        res = cr.fetchall()
        count=0
        for row in res:
            self.tr.insert("",index=count,values=row)
            count+=1
        self.tr.pack()
        self.root.mainloop()
#viewcategory()

