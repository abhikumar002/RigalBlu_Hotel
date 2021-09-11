from tkinter import *
from tkinter import messagebox
# from tkinter import ttk
import pymysql

pymysql.connect
from PIL import Image, ImageTk
from hotel import HotelManagement


class start:
    def __init__(self, root):
        self.root = root
        self.root.title("Registraion Form")
        self.root.geometry("1300x1200")

        self.loginflag = 0
        self.username = StringVar()
        self.password = StringVar()
        # self.new_window=Toplevel(self.root)
        # self.new_window.destroy()

        a = Label(self.root, text=" RIGAL BLU HOTEL", font=("TimesNewRoman", 20, "bold"),bg="black", fg="yellow").pack()
        recption = Image.open("rigalll.jpg")
        self.g = ImageTk.PhotoImage(recption)
        im = Label(self.root, image=self.g).pack()

        frame = Frame(self.root, height="350", width="350", bg="#996515").place(x=80, y=80)
        d = Label(self.root, text="Admin Panel LOGIN", font=("Arial", 17, "bold"), bg="silver").place(x=150, y=150)
        b = Label(self.root, text="User Id :-----", font=("Arial", 13, "bold"), bg="silver", fg="red").place(x=100,
                                                                                                             y=200)
        entry = Entry(self.root, width="20", textvariable=self.username).place(x=250, y=200)
        c = Label(self.root, text="Password:-----", font=("Arial", 13, "bold"), fg="red", bg="silver").place(x=100,
                                                                                                             y=250)
        entry = Entry(self.root, width="20", show="*", textvariable=self.password).place(x=250, y=250)
        button = Button(self.root, text="LOGIN", font=("Arial", 15, "bold"), command=self.login).place(x=150, y=300)

    def login(self):
        u = self.username.get()
        p = self.password.get()
        # print(self.username)
        if u == "admin" and p == "admin":
            #    self.new_window.destroy()
            self.new_window = Toplevel(self.root)
            self.app = HotelManagement(self.new_window)
        else:
            messagebox.showinfo("ERROR", "USER ID AND PASSWORD ARE NOT MATCH")


if __name__ == "__main__":
    root = Tk()
    obj = start(root)
    root.mainloop()