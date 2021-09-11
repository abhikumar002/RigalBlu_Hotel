from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from PIL import Image, ImageTk


class billing:
    def __init__(self, root):
        self.root = root
        self.root.title("Check-out Panel")
        self.root.geometry("1295x550+230+230")

        self.phn = StringVar()
        self.roomnumber = StringVar()
        self.numberofrooms = StringVar()
        self.date = StringVar()
        self.roomtype = StringVar()
        self.daysstay = StringVar()
        self.adult = StringVar()
        self.children = StringVar()
        self.row = StringVar()
        self.row2 = float()
        self.tax = StringVar()
        self.atotal = StringVar()
        self.btotal = StringVar()
        self.q1 = int()
        self.totalbill = StringVar()

        photo = Image.open("reception.jpg")
        self.j = ImageTk.PhotoImage(photo)
        kk = Label(self.root, image=self.j).pack()
        m = Label(self.root, text="CHECK OUT DETAILS ", fg="Black", bg="yellow", font=("Arial", 18, "bold")).place(
            x=150, y=20)

        x = Label(self.root, text="PHONE NUMBER", fg="Black", bg="#e8bf8b").place(x=50, y=320)
        entry = Entry(self.root, width="25", textvariable=self.phn).place(x=200, y=320)

        button = Button(self.root, text="FETCH DATA", command=self.fetch,bg="#e8bf8b").place(x=360, y=320)
        button = Button(self.root, text="CHECK OUT",width="10", height="2",bg="#e8bf8b", command=self.checkout).place(x=500, y=380)
        button = Button(self.root, text="  BILL", width="10", height="2" ,bg="#e8bf8b", command=self.total).place(x=500, y=320)

    def fetch(self):
        # top=Toplevel()
        if (self.phn.get() == ""):
            messagebox.showerror("Error", "Please Enter Phone No.", parent=self.root)
        else:
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            query = ("select Name from registration where Phoneno=%s")
            value = (self.phn.get(),)
            cur.execute(query, value)
            self.row = cur.fetchone()
            # print(row)

        if self.row == None:
            messagebox.showerror("Error", "This number is not found", parent=self.root)
        else:
            conn.commit()
            conn.close()
            showdataframe = Frame(self.root, bd=4, relief=RIDGE,bg="#946b3d", padx=2)
            showdataframe.place(x=50, y=100, width=300, height=180)

            lblname = Label(showdataframe, text="Name:",bg="#946b3d", font=("arial", 12, "bold"))
            lblname.place(x=0, y=0)

            lbl = Label(showdataframe, text=self.row,bg="#946b3d", font=("arial", 12, "bold"))
            lbl.place(x=90, y=0)

            # ------------------------------------------------------------------------
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            value = (self.phn.get(),)
            query = ("Select gmail from registration where Phoneno = %s")
            cur.execute(query, value)
            self.row = cur.fetchone()

            lblg = Label(showdataframe, text="Gmail:",bg="#946b3d", font=("arial", 12, "bold"))
            lblg.place(x=0, y=30)

            lbl2 = Label(showdataframe, text=self.row, bg="#946b3d",font=("arial", 12, "bold"))
            lbl2.place(x=90, y=30)

            # ------------------------------------------------------------------------
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            query = ("Select id from registration where Phoneno = %s")
            value = (self.phn.get(),)
            cur.execute(query, value)
            self.row = cur.fetchone()

            lblit = Label(showdataframe, text="ID TYPE:",bg="#946b3d", font=("arial", 12, "bold"))
            lblit.place(x=0, y=60)
            lbl3 = Label(showdataframe, text=self.row,bg="#946b3d", font=("arial", 12, "bold"))
            lbl3.place(x=90, y=60)

            # ------------------------------------------------------------------------
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            value = (self.phn.get(),)
            query = ("Select idnumber from registration where Phoneno = %s")
            cur.execute(query, value)
            self.row = cur.fetchone()

            lblidn = Label(showdataframe, text="ID No.:", bg="#946b3d",font=("arial", 12, "bold"))
            lblidn.place(x=0, y=90)

            lbl4 = Label(showdataframe, text=self.row,bg="#946b3d", font=("arial", 12, "bold"))
            lbl4.place(x=90, y=90)

            # -- ----------------------------------------------------------------------
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            value = (self.phn.get(),)
            query = ("Select country from registration where Phoneno = %s")
            cur.execute(query, value)
            self.row = cur.fetchone()

            lblc = Label(showdataframe, text="Country:",bg="#946b3d", font=("arial", 12, "bold"))
            lblc.place(x=0, y=120)

            lbl5 = Label(showdataframe, text=self.row,bg="#946b3d", font=("arial", 12, "bold"))
            lbl5.place(x=90, y=120)

            # #------------------------------------------------------------------------
            # #------------------------------------------------------------------------
            connec = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = connec.cursor()
            query = ("select date from checkin where Phoneno=%s")
            value = (self.phn.get(),)
            cur.execute(query, value)
            self.row = cur.fetchone()
            # print(self.row)

            if self.row == None:
                messagebox.showerror("Error", "This number is not found", parent=self.root)
            else:
                showdataframe2 = Frame(self.root, bd=4, relief=RIDGE,bg="#946b3d", padx=2)
                showdataframe2.place(x=450, y=100, width=300, height=180)
                lblcw = Label(showdataframe2, text="CHECK-IN DATE:",bg="#946b3d", font=("arial", 12, "bold"))
                lblcw.place(x=0, y=0)
                lbl2b = Label(showdataframe2, text=self.row, bg="#946b3d",font=("arial", 12, "bold"))
                lbl2b.place(x=150, y=0)
                # -----------------------------------------------------------------------
                conn = pymysql.connect(host="localhost", user="root", database="hotel")
                cur = conn.cursor()
                query = ("Select ndays from checkin where Phoneno = %s")
                value = (self.phn.get(),)
                cur.execute(query, value)
                row = cur.fetchone()
                lblnd = Label(showdataframe2,bg="#946b3d", text="NO. OF DAYS:", font=("arial", 12, "bold"))
                lblnd.place(x=0, y=30)
                lbl3b = Label(showdataframe2,bg="#946b3d", text=row, font=("arial", 12, "bold"))
                lbl3b.place(x=150, y=30)

                # ------------------------------------------------------------------------
                conn = pymysql.connect(host="localhost", user="root", database="hotel")
                cur = conn.cursor()
                value = (self.phn.get(),)
                query = ("Select roomtype from checkin where Phoneno = %s")
                cur.execute(query, value)
                row = cur.fetchone()
                lblirt = Label(showdataframe2,bg="#946b3d", text="ROOM TYPE :", font=("arial", 12, "bold"))
                lblirt.place(x=0, y=60)
                lbl4b = Label(showdataframe2, text=row, font=("arial", 12, "bold"))
                lbl4b.place(x=150, y=60)
                # ------------------------------------------------------------------------
                conn = pymysql.connect(host="localhost", user="root", database="hotel")
                cur = conn.cursor()
                value = (self.phn.get(),)
                query = ("Select roomno from checkin where Phoneno = %s")
                cur.execute(query, value)
                row = cur.fetchone()
                lblrn = Label(showdataframe2, text="ROOM NO :",bg="#946b3d", font=("arial", 12, "bold"))
                lblrn.place(x=0, y=90)
                lbl5b = Label(showdataframe2, text=row,bg="#946b3d", font=("arial", 12, "bold"))
                lbl5b.place(x=150, y=90)
                # -------------------------------------------------------------------------
                conn = pymysql.connect(host="localhost", user="root", database="hotel")
                cur = conn.cursor()
                query = ("Select children from checkin where Phoneno = %s")
                value = (self.phn.get(),)
                cur.execute(query, value)
                row = cur.fetchone()
                lblnd = Label(showdataframe2, text="CHILD:",bg="#946b3d", font=("arial", 12, "bold"))
                lblnd.place(x=0, y=150)
                lbl3b = Label(showdataframe2, text=row,bg="#946b3d", font=("arial", 12, "bold"))
                lbl3b.place(x=150, y=150)
                # -------------------------------------------------------------------------
                conn = pymysql.connect(host="localhost", user="root", database="hotel")
                cur = conn.cursor()
                query = ("Select adults from checkin where Phoneno = %s")
                value = (self.phn.get(),)
                cur.execute(query, value)
                row = cur.fetchone()
                lblnd = Label(showdataframe2, text="ADULT:",bg="#946b3d", font=("arial", 12, "bold"))
                lblnd.place(x=0, y=120)
                lbl3b = Label(showdataframe2, text=row,bg="#946b3d", font=("arial", 12, "bold"))
                lbl3b.place(x=150, y=120)
                # showdataframe3=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                # showdataframe3.place(x=850,y=100,width=300,height=180)

    def calculate(self):
        showdataframe3 = Frame(self.root, bd=4, relief=RIDGE,bg="#e8bf8b", padx=2)
        showdataframe3.place(x=800, y=100, width=300, height=180)

    def total(self):
        if (self.phn.get() == ""):
            messagebox.showerror("Error", "Please Enter Phone No.", parent=self.root)
        else:
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            query = ("select roomtype from checkin where Phoneno=%s")
            value = (self.phn.get())
            cur.execute(query, value)
            self.row = cur.fetchone()
            # tr=float(self.row)
            if self.row == None:
                messagebox.showerror("Error", "This number is not found", parent=self.root)
            else:
                showdataframe3 = Frame(self.root, bd=4, relief=RIDGE,bg="#e8bf8b", padx=2)
                showdataframe3.place(x=850, y=100, width=300, height=180)
                conn.commit()
                conn.close()
                tuple1 = ('SINGLE',)
                tuple2 = ('DOUBLE',)
                tuple3 = ('SINGLE(AC)',)
                tuple4 = ('DOUBLE(AC)',)
                if (self.row == tuple1):
                    conn = pymysql.connect(host="localhost", user="root", database="hotel")
                    cur = conn.cursor()
                    query = ("select ndays from checkin where Phoneno=%s")
                    value = (self.phn.get(),)
                    cur.execute(query, value)
                    self.row2 = cur.fetchone()
                    tr = (self.row2)
                    for c in tr:
                        x = int(c)
                        print(x)
                    #   print(tr)
                    self.q1 = (x * 400.0)

                elif (self.row == tuple2):
                    conn = pymysql.connect(host="localhost", user="root", database="hotel")
                    cur = conn.cursor()
                    query = ("select ndays from checkin where Phoneno=%s")
                    value = (self.phn.get(),)
                    cur.execute(query, value)
                    self.row2 = cur.fetchone()
                    tr = (self.row2)
                    for c in tr:
                        x = int(c)
                        print(x)

                    self.q1 = (x * 700.0)

                elif (self.row == tuple3):
                    conn = pymysql.connect(host="localhost", user="root", database="hotel")
                    cur = conn.cursor()
                    query = ("select ndays from checkin where Phoneno=%s")
                    value = (self.phn.get(),)
                    cur.execute(query, value)
                    self.row2 = cur.fetchone()
                    tr = (self.row2)
                    for c in tr:
                        x = int(c)
                        print(x)
                    self.q1 = (x * 1000.0)

                elif (self.row == tuple4):
                    conn = pymysql.connect(host="localhost", user="root", database="hotel")
                    cur = conn.cursor()
                    query = ("select ndays from checkin where Phoneno=%s")
                    value = (self.phn.get(),)
                    cur.execute(query, value)
                    self.row2 = cur.fetchone()
                    tr = (self.row2)
                    for c in tr:
                        x = int(c)
                        print(x)
                    self.q1 = (x * 1200.0)

                else:
                    messagebox.showerror("Error", "Please Enter correct value in database", parent=self.root)

                #    self.GST="Rs."+str(self.q1)
                gst = ((self.q1) * 0.09)
                st = ((self.q1) * 0.05)
                totalche = gst + st + self.q1
                print(gst, st, totalche)
                #    self.q1="Rs."+str(self.q1)
                self.GST = "Rs." + str("%.2f" % ((self.q1) * 0.09))
                self.ST = "Rs." + str("%.2f" % ((self.q1) * 0.05))
                totalche = "Rs." + str(totalche)
                #    totalch="Rs."+str("%.2f"%(((self.q1)*0.09)+((self.q1)*0.05)))
                #    self.totalbill="Rs."+str("%.2f"%((float)(self.GST)+(float)(self.ST)))
                lblgst = Label(showdataframe3, text="ROOM CHARGE:     Rs.", bg="#e8bf8b",font=("arial", 12, "bold"))
                lblgst.place(x=0, y=0)
                lbl3a = Label(showdataframe3, text=self.q1, bg="#e8bf8b",font=("arial", 12, "bold"))
                lbl3a.place(x=180, y=0)
                lblgst = Label(showdataframe3, text="GST:",bg="#e8bf8b", font=("arial", 12, "bold"))
                lblgst.place(x=0, y=40)
                lbl3b = Label(showdataframe3, text=self.GST,bg="#e8bf8b", font=("arial", 12, "bold"))
                lbl3b.place(x=150, y=40)
                lblst = Label(showdataframe3, text="ST:",bg="#e8bf8b", font=("arial", 12, "bold"))
                lblst.place(x=0, y=80)
                lbl3c = Label(showdataframe3, text=self.ST,bg="#e8bf8b", font=("arial", 12, "bold"))
                lbl3c.place(x=150, y=80)
                lblt = Label(showdataframe3, text="Total:",bg="#e8bf8b", font=("arial", 12, "bold"))
                lblt.place(x=0, y=140)
                lbl3d = Label(showdataframe3, text=totalche,bg="#e8bf8b", font=("arial", 12, "bold"))
                lbl3d.place(x=150, y=140)
            #    self.tax.set(self.GST)
            #    self.atotal.set(self.ST)
            #    self.btotal.set(Total)

    def checkout(self):
        conn = pymysql.connect(host="localhost", user="root", database="hotel")
        cur = conn.cursor()
        sql = "DELETE from checkin where Phoneno=%s"
        val = (self.phn.get(),)
        cur.execute(sql,val)
        conn.commit()
        self.clear()
        messagebox.showinfo("CONGRATS", "Check-out SUCCESSFULLY",parent=self.root)
        conn.close()
 
    def clear(self):
        showdataframe = Frame(self.root,bg="#e8bf8b", bd=4, relief=RIDGE, padx=2)
        showdataframe.place(x=450, y=100, width=300, height=180)
        showdataframe3 = Frame(self.root, bd=4, relief=RIDGE,bg="#e8bf8b", padx=2)
        showdataframe3.place(x=850, y=100, width=300, height=180)
        showdataframe2 = Frame(self.root, bd=4, relief=RIDGE,bg="#946b3d", padx=2)
        showdataframe2.place(x=50, y=100, width=300, height=180)
        self.phn.set("")
        self.date.set("")
        self.daysstay.set("")
        self.roomtype.set("")
        self.roomnumber.set("")
        self.adult.set("")
        self.children.set("")


if __name__ == "__main__":
    root = Tk()
    obj = billing(root)
    root.mainloop()