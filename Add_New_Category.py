# from tkinter import *
# from pymysql import *
from tkinter.messagebox import *
# from tkinter.ttk import *
from viewcategory import *

con = connect("127.0.0.1","root","ravi","pizzaproject")

class Add_New_Catogory:
    def example(self):
        global con
        cr = con.cursor()
        try:
            if self.CategoryNameEntry.get()=="" and len(self.DescriptionEntry.get(0.1,END))==1:
                print("wrong")
            else:
                s = "insert into categorytable values ('"+self.CategoryNameEntry.get()+"','"+ self.DescriptionEntry.get(0.1,END) +"')"
                res = cr.execute(s)
                con.commit()
                showinfo("","Data Inserted successfull"+str(res))
                self.tss.set("")
                self.DescriptionEntry.delete(0.1,END)
        except Exception as e:
            print(e)


    def __init__(self):
        self.root = Tk()
        #self.root.geometry("400x300")
        self.root.resizable(0,0)
        self.root.configure(background="skyblue")
        self.root.title("Add New Category")
        img = PhotoImage(file="recipe-pizza-pollo-arrosto.png")
        Label(self.root, image=img).place(x=0, y=0)
        #self.title = Label(self.root, text="Add New Category")
        self.CategoryName = Label(self.root, text="Enter Category Name:")
        self.tss = StringVar()
        self.CategoryNameEntry = Entry(self.root, width=20,textvariable=self.tss)
        self.Description = Label(self.root, text="Description")
        self.DescriptionEntry = Text(self.root, width=15, height=3)
        self.submit = Button(self.root, text="Submit", command=self.example)
        self.close = Button(self.root, text="Cancel", command=self.root.destroy)


        self.Description.grid(row=2, column=0, ipadx=10, pady=30, padx=5,
                                                                         ipady=5,sticky=W)
        self.CategoryName.grid(row=1, column=0, ipadx=10, pady=30, padx=5,
                                                                         ipady=5)
        self.close.grid(row=3, column=2, ipadx=10, pady=30, padx=15,
                                                                         ipady=5)
        self.CategoryNameEntry.grid(row=1, column=1,columnspan=2, ipadx=10, pady=30, padx=15,
                                                                         ipady=5)
        self.DescriptionEntry.grid(row=2, column=1, columnspan=2, ipadx=10, pady=30, padx=15,
                                                                         ipady=5)
        self.submit.grid(row=3, column=1, ipadx=10, pady=30, padx=15,
                                                                         ipady=5)

        self.root.mainloop()
if __name__ == '__main__':
    Add_New_Catogory()