from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from PIL import Image, ImageTk


class roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Check-in Panel")
        self.root.geometry("1295x550+230+230")

        self.phn = StringVar()
        self.roomnumber = StringVar()
        self.numberofrooms = StringVar()
        self.date = StringVar()
        self.roomtype = StringVar()
        self.daysstay = StringVar()
        self.adult = StringVar()
        self.children = StringVar()

        photo = Image.open("rigalroom.jpg")
        self.j = ImageTk.PhotoImage(photo)
        kk = Label(self.root, image=self.j).pack()
        m = Label(self.root, text="CHECK IN DETAILS ", fg="Black", bg="#d8c677", font=("Arial", 18, "bold")).place(
            x=150, y=20)

        x = Label(self.root, text="PHONE NUMBER", fg="Black", bg="#d8c677").place(x=50, y=100)
        entry = Entry(self.root, width="25", textvariable=self.phn).place(x=200, y=100)
        o = Label(self.root, text="Date", fg="Black", bg="#d8c677").place(x=50, y=150)
        entry = Entry(self.root, width="25", textvariable=self.date).place(x=200, y=150)
        f = Label(self.root, text="NO. OF DAYS", fg="Black", bg="#d8c677").place(x=50, y=200)
        entry = Entry(self.root, width="25", textvariable=self.daysstay).place(x=200, y=200)
        p = Label(self.root, text="ROOM TYPE", fg="Black", bg="#d8c677").place(x=50, y=250)
        q = Label(self.root, text="ROOM NO.", fg="Black", bg="#d8c677").place(x=50, y=300)
        entry = Entry(self.root, width="25", textvariable=self.roomnumber).place(x=200, y=300)
        combo_id = ttk.Combobox(self.root, textvariable=self.roomtype, font=("Arial", 10), state='readonly')
        combo_id['values'] = ('SINGLE', 'DOUBLE', 'SINGLE(AC)', 'DOUBLE(AC)')
        combo_id.current(0)
        combo_id.place(x=200, y=250)
        r = Label(self.root, text="NO OF ADULTS", fg="Black", bg="#d8c677").place(x=50, y=350)
        entry = Entry(self.root, width="25", textvariable=self.adult).place(x=200, y=350)
        s = Label(self.root, text="NO OF CHILDREN", fg="Black", bg="#d8c677").place(x=50, y=400)
        entry = Entry(self.root, width="25", textvariable=self.children).place(x=200, y=400)
        button = Button(self.root, text="FETCH DATA", command=self.fetch,bg="#a58048").place(x=355, y=100)
        button = Button(self.root, text="CHECK IN", command=self.checkin,bg="#a58048").place(x=550, y=480)

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
            row = cur.fetchone()
            # print(row)

        if row == None:
            messagebox.showerror("Error", "This number is not found", parent=self.root)
        else:
            conn.commit()
            conn.close()
            showdataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2,bg="#a58048")
            showdataframe.place(x=450, y=100, width=300, height=180)

            lblname = Label(showdataframe, text="Name:", bg="#a58048",font=("arial", 12, "bold"))
            lblname.place(x=0, y=0)

            lbl = Label(showdataframe, text=row,bg="#a58048",font=("arial", 12, "bold"))
            lbl.place(x=90, y=0)

            # ------------------------------------------------------------------------
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            value = (self.phn.get(),)
            query = ("Select gmail from registration where Phoneno = %s")
            cur.execute(query, value)
            row = cur.fetchone()

            lblg = Label(showdataframe, text="Gmail:", bg="#a58048",font=("arial", 12, "bold"))
            lblg.place(x=0, y=30)

            lbl2 = Label(showdataframe, text=row,bg="#a58048", font=("arial", 12, "bold"))
            lbl2.place(x=90, y=30)

            # ------------------------------------------------------------------------
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            query = ("Select id from registration where Phoneno = %s")
            value = (self.phn.get(),)
            cur.execute(query, value)
            row = cur.fetchone()

            lblit = Label(showdataframe, text="ID TYPE:", bg="#a58048",font=("arial", 12, "bold"))
            lblit.place(x=0, y=60)
            lbl3 = Label(showdataframe, text=row,bg="#a58048", font=("arial", 12, "bold"))
            lbl3.place(x=90, y=60)

            # ------------------------------------------------------------------------
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            value = (self.phn.get(),)
            query = ("Select idnumber from registration where Phoneno = %s")
            cur.execute(query, value)
            row = cur.fetchone()

            lblidn = Label(showdataframe, text="ID No.:", bg="#a58048",font=("arial", 12, "bold"))
            lblidn.place(x=0, y=90)

            lbl4 = Label(showdataframe, text=row,bg="#a58048", font=("arial", 12, "bold"))
            lbl4.place(x=90, y=90)

            # -- ----------------------------------------------------------------------
            conn = pymysql.connect(host="localhost", user="root", database="hotel")
            cur = conn.cursor()
            value = (self.phn.get(),)
            query = ("Select country from registration where Phoneno = %s")
            cur.execute(query, value)
            row = cur.fetchone()

            lblc = Label(showdataframe, text="Country:", bg="#a58048",font=("arial", 12, "bold"))
            lblc.place(x=0, y=120)

            lbl5 = Label(showdataframe, text=row,bg="#a58048", font=("arial", 12, "bold"))
            lbl5.place(x=90, y=120)

    def checkin(self):
        conn = pymysql.connect(host="localhost", user="root", database="hotel")
        cur = conn.cursor()
        sql = "INSERT INTO checkin(Phoneno,date,ndays,roomtype,roomno,adults,children) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (self.phn.get(), self.date.get(), self.daysstay.get(), self.roomtype.get(), self.roomnumber.get(),
               self.adult.get(), self.children.get())
        cur.execute(sql, val)
        conn.commit()
        self.clear()
        messagebox.showinfo("CONGRATS", "Check-in SUCCESSFULLY",parent=self.root)
        conn.close()

    def clear(self):
        showdataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
        showdataframe.place(x=450, y=100, width=300, height=180)
        self.phn.set("")
        self.date.set("")
        self.daysstay.set("")
        self.roomtype.set("")
        self.roomnumber.set("")
        self.adult.set("")
        self.children.set("")


if __name__ == "__main__":
    root = Tk()
    obj = roombooking(root)
    root.mainloop()