from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import database
import fhandle

###########################################################       Login Window      ##################################################################################

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("News Feed")
        wih = 600
        wiw = 400
        sch = self.root.winfo_screenheight()
        scw = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d+%d+%d"%(wiw, wih, (scw/2)-(wiw/2), (sch/2)-(wih/2)))
        self.root.configure(background="#ffffff")
        self.root.resizable(height=False, width=False)

        self.uname = StringVar()
        self.pass0 = StringVar()

        self.img = Image.open('images.jpg')
        self.user = Image.open('user.jpg')
        self.pas = Image.open('pass.png')
        self.img = self.img.resize((170, 170), Image.ANTIALIAS)
        self.user = self.user.resize((30, 30), Image.ANTIALIAS)
        self.pas = self.pas.resize((40, 40), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(self.img)
        self.user1 = ImageTk.PhotoImage(self.user)
        self.pas1 = ImageTk.PhotoImage(self.pas)

        self.heading = Label(text='News Feed', bg='white', fg='#700000', font='Papyrus 35 bold', pady=20, image=self.photoImg, bd=0, compound=TOP)
        self.heading.pack()

        self.frame = Frame(self.root, bg="#ffffff")
        self.frame.pack(pady=30)
        self.frame.config(height=300, width=300)

        Label(self.frame, image=self.user1, bg='#ffffff', text=" Username", font="Verdana", compound=LEFT).grid(row=0, column=0, padx=10, pady=10)
        Label(self.frame, image=self.pas1, bg='#ffffff', text=" Password", font="Verdana", compound=LEFT).grid(row=1, column=0, padx=10, pady=10)

        Entry(self.frame, bd=4, relief=GROOVE, textvariable=self.uname, font='Verdana 10').grid(row=0, column=1)
        Entry(self.frame, bd=4, show="*", relief=GROOVE, textvariable=self.pass0, font="Verdana 10").grid(row=1, column=1)

        Button(self.frame, text="Login",font="Comic 14", bd=3, relief=RAISED, command=self.login).grid(row=2, columnspan=2, pady=4)
        Button(self.frame,text="Create New Account",font="Comic 14",bd=3,relief=RAISED,command = self.register).grid(row=3, columnspan=2, pady=16)


    def login(self):
        if self.uname.get() == "" or self.pass0.get() == "":
            messagebox.showerror(title="Error",message="All Fields are Required")
        else:
            data= database.readdata(self.uname.get())
            if data == []:
                messagebox.showerror(title="Error", message="Username Does'nt Exist\nTry a Different One")
            else:
                if self.pass0.get() == data[0][2]:
                    self.root.destroy()
                    obj = SucLogin(self.uname.get())
                elif self.pass0.get() != data[0][2] and data[0][2] != "":
                    messagebox.showerror(title="Error", message="Wrong Password\nTry a Different One")


    def register(self):
        self.root.destroy()
        window = Tk()
        obj = Register(window)
        window.mainloop()

###########################################################       Register Window      ##################################################################################

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("News Feed")
        wih = 600
        wiw = 400
        self.name = StringVar()
        self.gender = StringVar()
        self.gender.set("Male")
        self.username= StringVar()
        self.password = StringVar()
        self.sports = IntVar()
        self.enter = IntVar()
        self.sci = IntVar()
        self.poli = IntVar()
        sch = self.root.winfo_screenheight()
        scw = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d+%d+%d" % (wiw, wih, (scw / 2) - (wiw / 2), (sch / 2) - (wih / 2)))
        self.root.configure(background="#ffffff")
        self.root.resizable(height=False, width=False)

        self.frame1 = Frame(self.root,bg="#ffffff")
        self.frame1.pack(pady=10)
        self.frame1.configure(height=50,width=300)

        Label(self.frame1, text="Register Yourself", font = "Papyrus 27 bold", bg="#ffffff", fg="#700000").pack(pady=20)

        self.frame2 = Frame(self.root,width=300,height=480,bg="#ffffff")
        self.frame2.pack(pady=0)

        Label(self.frame2, text="Enter Full Name",bg="#ffffff",font="Verdana 11").grid(row=0, column=0,padx=20,pady=20)
        Entry(self.frame2, bd=4, relief=GROOVE, textvariable=self.name, font='Verdana 10').grid(row=0, column=1)

        Label(self.frame2, text="Select Gender", bg="#ffffff", font="Verdana 11").grid(row=1, column=0, padx=20, pady=20,sticky=W)
        Radiobutton(self.frame2,text="Male",font="Verdana 10", variable=self.gender,value="Male", bg="#ffffff").grid(row=1,column=1,sticky=W)
        Radiobutton(self.frame2, text="Female",font="Verdana 10", variable=self.gender, value="Female", bg="#ffffff").grid(row=1,column=1,sticky=E)

        Label(self.frame2, text="Enter Username", bg="#ffffff", font="Verdana 11").grid(row=2, column=0, padx=20,
                                                                                       pady=20, sticky=W)
        Entry(self.frame2, bd=4, relief=GROOVE, textvariable=self.username, font='Verdana 10').grid(row=2, column=1)

        Label(self.frame2, text="Enter Password", bg="#ffffff", font="Verdana 11").grid(row=3, column=0, padx=20,
                                                                                       pady=20, sticky=W)
        Entry(self.frame2, bd=4, relief=GROOVE, textvariable=self.password, font='Verdana 10').grid(row=3, column=1)

        Label(self.frame2, text="Select Interests", bg="#ffffff", font="Verdana 11").grid(row=4, column=0, padx=20, sticky=W)

        Checkbutton(self.frame2, text="Sports",font="Verdana 11",bg="#ffffff", variable=self.sports, onvalue=1, offvalue=0).grid(row=4,column=1, sticky=W)
        Checkbutton(self.frame2, text="Politics", font="Verdana 11", bg="#ffffff", variable=self.poli, onvalue=1, offvalue=0).grid(row=6, column=1, sticky=W)
        Checkbutton(self.frame2, text="Entertainment", font="Verdana 11", bg="#ffffff", variable=self.enter, onvalue=1, offvalue=0).grid(row=5, column=1, sticky=W)
        Checkbutton(self.frame2, text="Science", font="Verdana 11", bg="#ffffff", variable=self.sci, onvalue=1, offvalue=0).grid(row=7, column=1, sticky=W)

        Button(self.frame2, text="Register",font="Comic 14",bd=3,relief=RAISED, command=self.register1).grid(row=8, columnspan=2,pady=20)
        Button(self.frame2, text="Back", font="Comic 14", bd=3, relief=RAISED, command=self.back1).grid(row=8, columnspan=1, pady=20,sticky=W)
        Button(self.frame2, text="Exit", font="Comic 14", bd=3, relief=RAISED, command=self.exit1).grid(row=8, columnspan=3, pady=20,sticky=E)

    def back1(self):
        self.root.destroy()
        window = Tk()
        obj = Login(window)
        window.mainloop()

    def exit1(self):
        exit(0)

    def register1(self):
        if len(self.name.get()) != 0 and len(self.password.get()) != 0 and len(self.username.get()) != 0:
            sec=database.readdata(self.username.get())
            if sec == []:
                database.adddata(self.name.get(), self.username.get(), self.password.get(), self.gender.get(),
                                 self.sports.get(), self.poli.get(), self.enter.get(), self.sci.get())
                self.root.destroy()
                obj = SucReg()
            else:
                messagebox.showerror(title="Error", message="Username Already Exist")

        else:
            messagebox.showerror(title="Error", message="All Fields are Required")

###########################################################       Registering Window      ##################################################################################

class SucReg():
    def __init__(self):
        self.regwin = Tk()
        self.regwin.title("News Feed")
        wih = 600
        wiw = 400
        sch = self.regwin.winfo_screenheight()
        scw = self.regwin.winfo_screenwidth()
        self.regwin.geometry("%dx%d+%d+%d" % (wiw, wih, (scw / 2) - (wiw / 2), (sch / 2) - (wih / 2)))
        self.regwin.configure(background="#ffffff")
        self.regwin.resizable(height=False, width=False)

        Label(self.regwin, text="Congratulations!", bg='white', fg='#700000', font='Papyrus 35 bold underline').pack(pady=50)
        Label(self.regwin, text="You are Succesfully", bg='white', fg='#700000', font='Papyrus 24 bold').pack(pady=10)
        Label(self.regwin, text="Registered", bg='white', fg='#700000', font='Papyrus 24 bold').pack(pady=10)
        #Label(self.regwin, text="", bg='white', fg='#700080', font='Papyrus 20 bold').pack()

        Button(self.regwin, text="Login", font="Comic 14", bd=3, relief=RAISED,command=self.login_).pack(pady=10)
        Button(self.regwin, text="Back", font="Comic 14", bd=3, relief=RAISED,command=self.back2).pack(pady=10)
        Button(self.regwin, text="Exit", font="Comic 14", bd=3, relief=RAISED, command=self.exit2).pack(pady=10)

        self.regwin.mainloop()

    def exit2(self):
        exit(0)

    def back2(self):
        self.regwin.destroy()
        window = Tk()
        obj = Register(window)
        window.mainloop()

    def login_(self):
        self.regwin.destroy()
        window = Tk()
        obj = Login(window)
        window.mainloop()

###########################################################       LoggedIn Window      ##################################################################################

class SucLogin:
    def __init__(self,uname):
        self.logwin = Tk()
        self.logwin.title("News Feed")
        wih = 700
        wiw = 1400
        sch = self.logwin.winfo_screenheight()
        scw = self.logwin.winfo_screenwidth()
        self.logwin.geometry("%dx%d+%d+%d" % (wiw, wih, (scw / 2) - (wiw / 2), (sch / 2) - (wih / 2)))
        self.logwin.configure(background="#ffffff")
        self.logwin.resizable(height=False, width=False)

        data=database.read_int(uname)
        udata=database.readdata(uname)

        self.frame1 = Frame(self.logwin, bg="#ffffff")
        self.frame1.pack()
        Label(self.frame1, bg="#ffffff", fg="#700000", text="Welcome "+udata[0][0],font="Papyrus 35 bold").pack(pady=20)

        self.frame2=Frame(self.logwin,bg="#ffffff")
        self.frame2.pack()
        file=["sp","ent","poli","sci"]
        new=["Sports News","Entertainment News","Politics News","Science News"]
        interest=0
        for x in data[0]:
            if x:
                news=fhandle.readnews(file[interest])
                Label(self.frame2, text=new[interest], bg="#ffffff", font="Verdana 15 bold").pack()
                Label(self.frame2,text=news,bg="#ffffff",font="Times 15").pack(pady=5)
            interest+=1
        self.frame3=Frame(self.logwin,bg="#ffffff")
        self.frame3.pack(pady=10)

        Button(self.frame3,text="Logout",font="Comic 14", bd=3, relief=RAISED,command=self.login).pack(side=LEFT,padx=50)
        Button(self.frame3, text="Exit", font="Comic 14", bd=3, relief=RAISED, command=self.exit0).pack(side=RIGHT,padx=50)

    def login(self):
        self.logwin.destroy()
        win = Tk()
        obj = Login(win)
        win.mainloop()

    def exit0(self):
        exit(0)

window = Tk()
obj = Login(window)
window.mainloop()
