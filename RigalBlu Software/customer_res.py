from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
pymysql.connect
from PIL import Image, ImageTk


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registraion Form")
        self.root.geometry("1260x630+230+250")

        # Variables
        self.loginflag = 0
        self.totalrooms = StringVar()
        self.occupiedrooms = StringVar()
        self.vacantrooms = StringVar()
        self.name = StringVar()
        self.phn = StringVar()
        self.gmail = StringVar()
        self.address = StringVar()
        self.country = StringVar()
        self.idtype = StringVar()
        self.idnumber = StringVar()
        self.id = StringVar()

        # photo
        photo = Image.open("3.jpg")
        self.j = ImageTk.PhotoImage(photo)
        k = Label(self.root, image=self.j).pack()

        m = Label(self.root, text="GUEST INFORMATION", fg="Black", bg="#e3e2e6", font=("Arial", 18, "bold")).place(
            x=150, y=20)

        z = Label(self.root, text="NAME", fg="Black", bg="Silver").place(x=50, y=100)
        entry = Entry(self.root, width="25", textvariable=self.name).place(x=200, y=100)
        o = Label(self.root, text="PHONE NUMBER", fg="Black", bg="Silver").place(x=50, y=150)
        entry = Entry(self.root, width="25", textvariable=self.phn).place(x=200, y=150)
        p = Label(self.root, text="GMAIL ID", fg="Black", bg="Silver").place(x=50, y=200)
        entry = Entry(self.root, width="25", textvariable=self.gmail).place(x=200, y=200)
        q = Label(self.root, text="ADDRESS", fg="Black", bg="Silver").place(x=50, y=250)
        entry = Entry(self.root, width="25", textvariable=self.address).place(x=200, y=250)
        r = Label(self.root, text="COUNTRY", fg="Black", bg="Silver").place(x=50, y=300)
        entry = Entry(self.root, width="25", textvariable=self.country).place(x=200, y=300)
        O = Label(self.root, text="ID TYPE", fg="Black", bg="Silver").place(x=50, y=350)
        p = r = Label(self.root, text="ID NUMBER", fg="Black", bg="Silver").place(x=50, y=400)
        clicked = StringVar()
        # Create an instance of Menu in the frame
        combo_id = ttk.Combobox(self.root, textvariable=self.id, font=("Arial", 10), state='readonly')
        combo_id['values'] = ('AADHAR CARD', 'VOTER ID', 'PAN CARD', 'DRIVING LICINSES')
        combo_id.current(0)
        combo_id.place(x=200, y=350)
        entry = Entry(self.root, width="25", textvariable=self.idnumber).place(x=200, y=400)
        button = Button(self.root, text="SAVE DETAILS", command=self.saveregistration).place(x=450, y=480)
        button = Button(self.root, text="RESET", command=self.clear).place(x=300, y=480)
        self.clear()

    def saveregistration(self):
        conn = pymysql.connect(host="localhost", user="root", password="", database="hotel")
        cur = conn.cursor()
        sql = "INSERT INTO registration(name,phoneno,Gmail,Address,country,id,idnumber) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (self.name.get(), self.phn.get(), self.gmail.get(), self.address.get(), self.country.get(), self.id.get(),
               self.idnumber.get())
        cur.execute(sql, val)
        conn.commit()
        self.clear()
        messagebox.showinfo("CONGRATS", "Registration SUCCESSFULLY",parent=self.root)
        conn.close()

    def clear(self):
        self.country.set("")
        self.address.set("")
        self.gmail.set("")
        self.phn.set("")
        self.name.set("")
        self.id.set("")
        self.idnumber.set("")


if __name__ == "__main__":
    root = Tk()
    obj = register(root)
    root.mainloop()