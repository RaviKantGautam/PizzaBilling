from tkinter import *
from tkinter.ttk import *
from pymysql import *
from tkinter.messagebox import *
#from PIL import ImageTk,Image
import datetime
import http.client
import smtplib
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import subprocess
import random

con = connect("127.0.0.1","root","ravi","pizzaproject")
i=0
class billing:
    CART=[]
    def add_table(self):
        if self.category_combo.get()=="" and self.pizza_combo.get()=="" and self.qty_combo.get()=="":
            showwarning("Empty values","All columns are mandatory")
        else:
            global i
            c=self.category_combo.get()
            p=self.pizza_combo.get()
            q=self.qty_combo.get()
            cr = con.cursor()
            PID = str(str(p).split("-")[1])
            print("pid",PID)
            flag = False

            for i in range(0,len(self.CART)):
                if int(self.CART[i][0]==int(PID)):
                    self.CART[i][3]=int(self.CART[i][3])+int(q)
                    self.CART[i][4]=float(self.CART[i][2])*float(self.CART[i][3])
                    flag=True
                    break
            if flag==False:
                query="Select * from add_pizza where pid='"+str(PID)+"'"
                print(query)
                cr.execute(query)
                res = cr.fetchone()
                amt = float(q)*float(res[4])
                self.CART.append([res[0],res[1],res[4],q,amt])
            print(self.CART)
            for child in self.tr.get_children():
                self.tr.delete(child)

            i=0
            self.total=0.0
            for row in self.CART:
                self.total+=float(row[4])
                self.tr.insert('',index=i,values=row)
                i+=1
            #
            # query = "Select disprice from add_pizza where p_name='"+self.pizza_combo.get()+"'"
            # cr.execute(query)
            # res = cr.fetchone()
            # amount = int(res[0]*int(self.qty_combo.get()))
            #
            #
            # down_lis=[]
            # up_lis = []
            # down_lis.append(p)
            # down_lis.append(res[0])
            # down_lis.append(q)
            # down_lis.append(amount)
            # up_lis.append(down_lis)
            # for i in range(0,len(up_lis)):
            #     #self.total+=int(up_lis[i][3])
            # #     self.total+=int(amount)
            # #
            #     self.tr.insert('',index=i,values=up_lis[i])
            gst = self.total*5/100
            nst_amt = self.total+gst
            self.ans.set(self.total)
            self.ans2.set(gst)
            self.ans3.set(str(nst_amt))
            # print(self.ans,"---",self.ans2,"---",self.ans3)
            #
            # self.t = self.ans.get()
            # self.g = self.ans2.get()
            # self.n = self.ans3.get()
            # print(self.t,"--",self.g,"--",self.n)

            self.category_combo.current(0)
            self.qty_combo.current(0)
            self.pizza_combo.current(0)

    def getpizza(self,event):
        global con
        lst_pizza = []
        cr = con.cursor()
        s = "select p_name,PID from add_pizza where categoryname='"+self.category_combo.get()+"'"
        cr.execute(s)
        res = cr.fetchall()
        for k in range(0,len(res)):
            lst_pizza.append(str(res[k][0])+"-"+str(res[k][1]))
        self.pizza_combo.config(values=list(lst_pizza))





    def __init__(self):
        #code for database connection
        self.total = 0.0
        self.ted = (self.total * 0.05)
        self.netme = self.total+self.ted
        global con
        cr = con.cursor()
        s = "select * from categorytable"
        cr.execute(s)
        res = cr.fetchall()
        lt = []
        ct = []
        for row in res:
            lt.append(row[0])
            ct.append((row[1]))

        # this block of code is for window configuration
        self.root = Tk()
        self.root.geometry("1100x500")
        self.root.resizable(0,0)
        self.root.title("Billing")
        self.root.configure(bg = 'khaki')
        img = PhotoImage(file="alpine_pizza_32132_16x9.png")
        Label(self.root, image=img).place(x=0, y=0)
        # image = Image.open(r"C:\Users\Jeiven Randhawa\Desktop\abc.jpg")
        # image = image.resize((1080,460),Image.ANTIALIAS)
        # self.img = ImageTk.PhotoImage(image)


        #code for labels used
        self.l1 = Label(self.root,text="Billing",font=("Arial",20))
        category_label = Label(self.root,text="Category",width=10)
        pizza_label = Label(self.root,text="Pizza",width=10)
        qty_label = Label(self.root,text="Qty",width=10)
        self.total_label = Label(self.root,text="Total",width=10)
        self.gst_label = Label(self.root,text="GST",width=10)
        self.netamounnt_lb = Label(self.root,text="Net Amount",width=10)
        customername_lb = Label(self.root, text="Customer Name")
        customerphone_lb = Label(self.root, text="Phone number")
        customerEmail_lb = Label(self.root, text="Email")


        #code for entry
        self.ans = StringVar()
        self.total_Entry = Entry(self.root, width=20, textvariable=self.ans, state='disabled')
        self.ans2 = StringVar()
        self.gst_Entry = Entry(self.root, width=20, textvariable=self.ans2, state='disabled')
        self.ans3 = StringVar()
        self.netamounnt_Entry = Entry(self.root, width=20, textvariable=self.ans3, state='disabled')
        self.customername_Entry = Entry(self.root, width=20)
        self.customerphone_Entry = Entry(self.root, width=20)
        self.customerEmail_Entry = Entry(self.root, width=20)


        #code for combobox
        self.category_combo=Combobox(self.root,state="readonly",values=lt)
        self.category_combo.bind("<<ComboboxSelected>>",self.getpizza)
        self.pizza_combo = Combobox(self.root,state="readonly")
        self.qty_combo = Combobox(self.root,values=(1,2,3,4,5,6,7,8,9,10),state="readonly")

        #code for button
        add_button = Button(self.root,text="Add",command=self.add_table)
        self.generatebill = Button(self.root, text="Generate Bill", command=self.bill_table)
        self.close = Button(self.root, text="Cancel", command=self.root.destroy)


        #code for treeview
        self.tr = Treeview(self.root, columns=("PID","item", "price","qty","amount"))
        self.tr.heading("PID", text="PID")
        self.tr.heading("item",text="item")
        self.tr.heading("price", text="Price")
        self.tr.heading("qty", text="Quantity")
        self.tr.heading("amount", text="Amount")
        self.tr['show'] = "headings"


        #code for packing
        self.l1.pack(fill=X)
        category_label.place(x=60,y=60)
        self.category_combo.place(x=140,y=60)
        pizza_label.place(x=310,y=60)
        self.pizza_combo.place(x=390,y=60)
        qty_label.place(x=560,y=60)
        self.qty_combo.place(x=650,y=60)
        add_button.place(x=850,y=60)
        self.tr.place(x=60,y=100)
        self.total_label.place(x=200,y=350)
        self.gst_label.place(x=200,y=380)
        self.netamounnt_lb.place(x=200,y=410)
        self.generatebill.place(x=200,y=440)
        self.total_Entry.place(x=300,y=350)
        self.gst_Entry.place(x=300,y=380)
        customername_lb.place(x=600,y=350)
        customerphone_lb.place(x=600,y=380)
        customerEmail_lb.place(x=600,y=410)
        self.customername_Entry.place(x=700,y=350)
        self.customerphone_Entry.place(x=700,y=380)
        self.customerEmail_Entry.place(x=700,y=410)
        self.netamounnt_Entry.place(x=300,y=410)
        self.close.place(x=300,y=440)
        self.root.mainloop()


    def bill_table(self):
        global con
        cr = con.cursor()
        s = datetime.datetime.now()
        s = "insert into billtable (`date1`,`total`,`gst`,`netamount`,`customername`,`mobileno`,`email`) values ('" + str(
        s.date()) + "','" + str(self.total) + "','" + str(self.ted) + "','" + str(self.netme) + "','" + str(
        self.customername_Entry.get()) + "','" + str(self.customerphone_Entry.get()) + "','" + str(
        self.customerEmail_Entry.get()) + "')"
        print(s)
        cr.execute(s)
        con.commit()

        billid = cr.lastrowid
        print(billid)
        for row in self.CART:
            q = "insert into billdetail values (null,'" + str(billid) + "','" + str(row[0]) + "','" + str(
            row[2]) + "','" + str(row[3]) + "','" + str(row[4]) + "')"
            print(q)
            cr.execute(q)
        con.commit()


        x = str(random.randint(0, 100))
        t = str("'a" + x + ".pdf'")
        my_canvas = canvas.Canvas(t, pagesize=A4)
        # -=========================================================
        my_canvas.setLineWidth(.5)
        my_canvas.setFont('Helvetica', 24)
        my_canvas.drawString(235, 780, 'BILL')
        my_canvas.line(235, 775, 285, 775)
        my_canvas.setLineWidth(1)
        my_canvas.setFont('Helvetica', 20)
        my_canvas.setFont('Helvetica', 12)
        my_canvas.setLineWidth(.7)

        # -===================================DATA===========================

        # -=====================Patient==================================
        my_canvas.line(50, 755, 50, 600)
        my_canvas.line(50, 755, 465, 755)
        my_canvas.drawString(70, 740, ' Bill Id')
        my_canvas.line(120, 755, 120, 600)
        # my_canvas.drawString(145, 745, ':')


        my_canvas.drawString(150, 740, ' Pizza Name')
        my_canvas.line(235, 755, 235, 600)
        # my_canvas.drawString(145, 745, ':')
        my_canvas.drawString(240, 740, ' Price')
        my_canvas.line(305, 755, 305, 600)
        # my_canvas.drawString(145, 745, ':')
        my_canvas.drawString(320, 740, ' Quantity')
        my_canvas.line(395, 755, 395, 600)
        # my_canvas.drawString(145, 745, ':')
        my_canvas.drawString(400, 740, ' Amount')
        y = 720
        for j in range(0,len(self.CART)):
            my_canvas.drawString(70, y, str(self.CART[j][0]))
            my_canvas.drawString(150, y, str(self.CART[j][1]))
            my_canvas.drawString(240, y, str(self.CART[j][2]))
            my_canvas.drawString(320, y, str(self.CART[j][3]))
            my_canvas.drawString(400, y, str(self.CART[j][4]))
            y = y - 20

        my_canvas.line(465, 755, 465, 600)
        my_canvas.line(50, 735, 465, 735)
        my_canvas.line(50, 600, 465, 600)

        # my_canvas.drawString(145, 745, ':')
        my_canvas.drawString(380, 565, ' Total')
        my_canvas.drawString(420, 565, ':')
        my_canvas.drawString(440, 565, str(self.ans.get()))

        # z
        my_canvas.drawString(380, 545, ' GST')
        my_canvas.drawString(420, 545, ':')
        my_canvas.drawString(440, 545, str(self.ans2.get()))

        my_canvas.drawString(380, 525, ' Net')
        my_canvas.drawString(420, 525, ':')
        my_canvas.drawString(440, 525, str(self.ans3.get()))

        my_canvas.drawString(50, 565, 'Customer Name')
        my_canvas.drawString(140, 565, ':')
        my_canvas.drawString(160, 565, self.customername_Entry.get())

        my_canvas.drawString(50, 545, ' Email')
        my_canvas.drawString(140, 545, ':')
        my_canvas.drawString(160, 545, self.customerEmail_Entry.get())

        my_canvas.drawString(50, 525, 'Phone Number')
        my_canvas.drawString(140, 525, ':')
        my_canvas.drawString(160, 525, self.customerphone_Entry.get())


        my_canvas.drawString(50, 465, ' Bill Pay by  :-')
        my_canvas.drawString(388, 455, ' (Signature Personnel/Family)')
        my_canvas.line(50, 452, 580, 452)
        # -=======================================================
        my_canvas.save()
        subprocess.Popen([t], shell=True)

        msg = "Hii" + self.customername_Entry.get() + ", Thanks for your order with us for Rs." + str(
            self.netamounnt_Entry.get())
        msg = msg.replace(" ", "%20")
        conn1 = http.client.HTTPConnection("server1.vmm.education")
        conn1.request('GET',
                      "/VMMCloudMessaging/AWS_SMS_Sender?username=monika&password=L78E7CIB&message=" + msg + "&phone_numbers=" +
                      self.customerphone_Entry.get())
        response = conn1.getresponse()
        print(response.read())

        sender = 'tania.vmmteachers23@gmail.com'
        receiver = self.customerEmail_Entry.get()
        password = 'Teachers@123'
        try:
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(sender, password)
            msg = msg.replace('%20', " ")
            body = "\n" + msg + "\n\n"
            subject = "Subject:Bill "
            msgl = subject + body
            smtpserver.sendmail(sender, receiver, msgl)
            print('sent')
            smtpserver.close()
        except smtplib.SMTPException as e:
            print("not send becoz: ", e)
if __name__ == '__main__':
    billing()