#from tkinter import *
#from PIL import ImageTk,Image
from Add_New_Category import *
from viewcategory import *
from pizza_form import *
from viewpizza import *
from billing import *
from dailybill import *
from report import *


def func4():
    viewpizza()
    first_page()


def func2():
    viewcategory()
    first_page()


class first_page:
    def func7(self):
        self.window.destroy()
        dailybill()
        first_page()

    def func1(self):
        self.window.destroy()
        Add_New_Catogory()
        first_page()

    def func3(self):
        self.window.destroy()
        pizza_form()
        first_page()

    def func5(self):
        self.window.destroy()
        billing()
        first_page()

    def func6(self):
        self.window.destroy()
        report()
        first_page()

    def __init__(self):
        self.window = Tk()
        self.window.title("Menu Page")
        self.window.geometry("400x400+420+120")
        img = PhotoImage(file="login.png")
        Label(self.window, image=img).place(x=0, y=0)
        self.main_menu = Menu()
        self.window.config(menu=self.main_menu)

        #code for file menu
        self.file = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file)
        self.file.add_command(label="Exit", command=quit)

        #code for manage category
        self.managecat = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Manage Category", menu=self.managecat)
        self.managecat.add_command(label="Add Category", command=self.func1)
        self.managecat.add_command(label="View Category", command=func2)

        #code for manage pizza
        self.managepiz = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Manage Pizza", menu=self.managepiz)
        self.managepiz.add_command(label="Add Pizza", command=self.func3)
        self.managepiz.add_command(label="View Pizza", command=func4)

        #code for billng
        self.bil = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Billing", menu=self.bil)
        self.bil.add_command(label="New Bill", command=self.func5)

        #code for report
        self.rept = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Report", menu=self.rept)
        self.rept.add_command(label="Daily Date", command=self.func7)
        self.rept.add_command(label="Datewise", command=self.func6)
        self.window.mainloop()
if __name__ == '__main__':
    first_page()