from tkinter import *
from login_page import *
class spashScreen:
    def logt(self):
        self.root.destroy()
        logmein()
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("SplashScreen")
        self.bt = Button(self.root,text="Admin",command=self.logt,bg ="skyblue",bd=5,activeforeground="green",activebackground="red", font=('Arial BOLD', 20)).pack(side=TOP,fill=X,expand="yes")
        img = PhotoImage(file="Girl-eating-burger-1068x623.png")
        Label(self.root, image=img).pack(side=BOTTOM)
        self.root.mainloop()
if __name__ == '__main__':
    spashScreen()