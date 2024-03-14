import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from PIL import Image, ImageTk

class Login:
    def __init__(self, root):
        self.root = root
        self.bg = ImageTk.PhotoImage(file="andoo.jpg")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #Background image
        self.bg_image = tk.Label(self.root, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        #frame
        self.frame_login = tk.Frame(self.root, bg="white")
        self.frame_login.place(x=330, y=150, width=500, height=400)
   
        #title & subtitle
        title = tk.Label(self.frame_login, text="Login Here", font=("impact", 35, "bold"), fg="#6162ff", bg="white")
        title.place(x=90, y=30)
        subtitle = tk.Label(self.frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white")
        subtitle.place(x=90, y=100)

        # username label and entry
        lbl_user = tk.Label(self.frame_login, text="Username", font=("impact", 20, "bold"), fg="grey", bg="white")
        lbl_user.place(x=90, y=140)
        self.txt_user = Entry(self.frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        # password label and entry
        lbl_pass = tk.Label(self.frame_login, text="Password", font=("impact", 20, "bold"), fg="grey", bg="white")
        lbl_pass.place(x=90, y=210)
        self.txt_pass = Entry(self.frame_login, font=("times new roman", 15), show="*", bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        # login button
        btn_login = Button(self.frame_login, text="Login", font=("times new roman", 20, "bold"), bg="#6162ff", fg="white", command=self.login)
        btn_login.place(x=90, y=290, width=350, height=40)

    def login(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        
        # Check if username and password are correct (dummy check)
        if username == "admin" and password == "admin123":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

root = tk.Tk()
login = Login(root)
root.mainloop()
