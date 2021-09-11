from tkinter import *
from tkinter import messagebox
# from tkinter import ttk
# import pymysql
from PIL import Image, ImageTk
from checkin import roombooking
from customer_res import register
from billing_cus import billing


# from room_detail import room

class HotelManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel RIGAL BLU")
        self.root.geometry("1550x800+0+0")

        self.new_window1 = Toplevel(self.root)
        self.new_window2 = Toplevel(self.root)
        self.new_window3 = Toplevel(self.root)
        self.new_window1.destroy()
        self.new_window2.destroy()
        self.new_window3.destroy()
        # img
        photo = Image.open("roo33.jpg")
        self.photoimg1 = ImageTk.PhotoImage(photo)
        Label(root, image=self.photoimg1).pack()


        # frames and buttons
        frame2 = Frame(self.root, height="950", width="200", bg="black").place(x=0, y=0)
        frame2 = Frame(self.root, height="150", width="1500", bg="black").place(x=0, y=0)
        logo = Image.open("logo8.jpg")
        self.photoimg2 = ImageTk.PhotoImage(logo)
        Label(self.root, image=self.photoimg2).place(x=0,y=0)
        saq = Label(self.root, text=" RIGAL BLU HOTEL", font=("TimesNewRoman", 25, "bold"), bg="black",fg="yellow").place(x=450, y=50)
        aa = Label(self.root, text="Menu", font=("Arial", 10, "bold"), bg="yellow", height=2, width=24).place(x=0,  y=150)
        button = Button(self.root, text="Customer", font=("Arial", 10, "bold"), bg="yellow", height=2, width=24,
                        command=self.customer).place(x=0, y=200)
        button = Button(self.root, text=" CHECK IN  ", font=("Arial", 10, "bold"), bg="yellow", height=2, width=24,
                        command=self.booking).place(x=0, y=250)
        button = Button(self.root, text="LOGOUT", font=("Arial", 10, "bold"), bg="yellow", height=2, width=24,
                        command=self.logout).place(x=0, y=350)
        button = Button(self.root, text="BILLING", font=("Arial", 10, "bold"), bg="yellow", height=2, width=24,
                        command=self.billing).place(x=0, y=300)

    def customer(self):
        self.new_window2.destroy()
        self.new_window3.destroy()
        try:
            self.new_window1.deiconify()
        except:
            self.new_window1 = Toplevel(self.root)
            self.app = register(self.new_window1)

    def booking(self):
        self.new_window1.destroy()
        self.new_window3.destroy()
        try:
            self.new_window2.deiconify()
        except:
            self.new_window2 = Toplevel(self.root)
            self.app = roombooking(self.new_window2)

    def billing(self):
        self.new_window1.destroy()
        self.new_window2.destroy()
        try:
            self.new_window3.deiconify()
        except:
            self.new_window3 = Toplevel(self.root)
            self.app = billing(self.new_window3)


    def logout(self):
        self.answer =messagebox.askyesno('Confirmation','Are you sure that you want to logout?',parent=self.root)
        if self.answer:
            self.root.destroy()
        

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagement(root)
    root.mainloop()