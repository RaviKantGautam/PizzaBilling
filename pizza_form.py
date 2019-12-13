from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from pymysql import *
con = connect("127.0.0.1","root","ravi","pizzaproject")
class pizza_form:
    def gst(self, event):
        print(self.discountEntry.get())
        self.tss3.set(int(self.mrpEntry.get())-((int(self.discountEntry.get())/100)*(int(self.mrpEntry.get()))))


    def addme(self):
        print("hello")
        global con
        cr = con.cursor()
        try:
            if self.dispriceEntry.get()=="" and self.discountEntry.get()=="" and self.mrpEntry.get()=="" and self.pnameEntry.get()=="":
                showwarning('Error',"All fields are mandatory to fill")
            else:
                print(self.comb.get())
                # s = "insert into add_pizza (`p_name`,`MRP`,`Discount`,`Dis-price`) values ('"+self.pnameEntry.get()+"',"+str(self.mrpEntry.get())+","+str(self.discountEntry.get())+","+str(self.dispriceEntry.get())+")"
                s = "insert into add_pizza (`p_name`,`MRP`,`Discount`,`Disprice`,`categoryname`) values ('"+self.pnameEntry.get()+"',"+self.mrpEntry.get()+","+self.discountEntry.get()+","+self.dispriceEntry.get()+",'"+str(self.comb.get())+"')"

                print(s)
                res = cr.execute(s)
                print(res)
                con.commit()
                showinfo("Successfull", "Data Inserted successfull")
                self.tss.set("")
                self.tss1.set("")
                self.tss2.set("")
                self.tss3.set("")
                self.comb.current(0)

        except Exception as e:
            print(e)



    def __init__(self):
        global con
        cr = con.cursor()
        s = "select * from categorytable"
        cr.execute(s)
        res = cr.fetchall()
        lt =[]
        for row in res:
            lt.append(row[0])

        self.root = Tk()
        self.root.title("Add Pizza")
        #self.root.geometry("400x400+420+120")
        self.root.resizable(0,0)
        img = PhotoImage(file="Disney-Family_Mickey-Valentine-Pizza-728x485.png")
        Label(self.root, image=img).place(x=0, y=0,anchor=CENTER)
        self.pname = Label(self.root,text="P_Name: ")
        self.tss = StringVar()
        self.pnameEntry = Entry(self.root,width=20,textvariable=self.tss)
        self.mrp = Label(self.root,text="MRP:")
        self.tss1 = StringVar()
        self.mrpEntry = Entry(self.root,width=20,textvariable=self.tss1)
        self.discount = Label(self.root,text="Discount")
        self.tss2 = StringVar()
        self.discountEntry = Entry(self.root,width=20,textvariable=self.tss2)
        self.discountEntry.bind("<Return>",self.gst)
        self.disprice = Label(self.root,text="Dis-Price")
        self.tss3 = StringVar()

        self.dispriceEntry = Entry(self.root,width=20,textvariable=self.tss3,state="disabled")
        #self.dispriceEntry.bind("<Return>",self.gt)

        self.submit = Button(self.root,text="Submit",command=self.addme)
        #self.submit.config(activebackground="green")
        self.close = Button(self.root,text="Cancel",command=self.root.destroy)
        self.category = Label(self.root,text="Select Catogory")
        self.comb = Combobox(self.root,values=lt,state='readonly')



        # placing
        self.pname.grid(row=0,column=0,padx=10,pady=5)
        self.pnameEntry.grid(row=0,column=1,padx=10,pady=5)
        self.mrp.grid(row=1,column=0,padx=10,pady=5)
        self.mrpEntry.grid(row=1,column=1,padx=10,pady=5)
        self.discount.grid(row=2,column=0,padx=10,pady=5)
        self.discountEntry.grid(row=2,column=1,padx=10,pady=5)
        self.disprice.grid(row=3,column=0,padx=10,pady=5)
        self.dispriceEntry.grid(row=3,column=1,padx=10,pady=5)
        self.submit.grid(row=4,column=1,padx=10,pady=5)
        self.close.grid(row=4,column=2,padx=10,pady=5)
        self.category.grid(row=5,column=0,padx=10,pady=5)
        self.comb.grid(row=5,column=1,columnspan=1,padx=10,pady=5)
        self.root.mainloop()
if __name__ == '__main__':
    pizza_form()