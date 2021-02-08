from tkinter import *
from tkinter import ttk, messagebox
import time


class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing System")
        self.root.geometry("1545x847+0+0")
        self.root.resizable(False, False)
        self.root.config(bg='grey40')
        self.bg = PhotoImage(file="Login.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=170, y=0)
        self.root.iconbitmap("billing.ico")

        digi = Label(root, text='Digital Clock', font ='times 24 bold', fg='brown4',bd=10)
        digi.place(x=520, y=90, height=40, width=500)

        F01 = Label(self.root, bg='LightSteelBlue4')
        F01.place(x=520, y=140, height=100, width=500)

        self.hr = Label(F01, text=12, font=("times new roman", 50, "bold"), bg="azure", fg='navy')
        self.hr.place(x=30, y=0, height=70, width=100)

        self.hr1 = Label(F01, text='HOUR', font=("times new roman", 15, "bold"), bg="white", fg='SkyBlue4')
        self.hr1.place(x=30, y=72, height=20, width=100)

        self.mn = Label(F01, text=60, font=("times new roman", 50, "bold"), bg="azure", fg='navy')
        self.mn.place(x=150, y=0, height=70, width=100)

        self.mn1 = Label(F01, text='MINUTE', font=("times new roman", 15, "bold"), bg="white", fg='SkyBlue4')
        self.mn1.place(x=150, y=72, height=20, width=100)

        self.sc = Label(F01, text=60, font=("times new roman", 50, "bold"), bg="azure", fg='navy')
        self.sc.place(x=270, y=0, height=70, width=100)

        self.sc1 = Label(F01, text='SECOND', font=("times new roman", 15, "bold"), bg="white", fg='SkyBlue4')
        self.sc1.place(x=270, y=72, height=20, width=100)

        self.noon = Label(F01, text='AM', font=("times new roman", 30, "bold"), bg="azure", fg='navy')
        self.noon.place(x=390, y=0, height=70, width=80)

        self.noon1 = Label(F01, text='AM/PM', font=("times new roman", 15, "bold"), bg="azure", fg='SkyBlue4')
        self.noon1.place(x=390, y=72, height=20, width=80)

        self.c_clock()
        #self.c_clock(hr, mn, sc, noon)
        # ==================================Login=====================================
        Frame_login = Frame(self.root, bg='white')
        Frame_login.place(x=520, y=250, height=340, width=500)
        self.txt_user = StringVar()
        self.txt_pass = StringVar()
        title = Label(Frame_login, text='Login Here', font=('Impact', 35, 'bold'), fg='Orange', bg='white').place(x=130,
                                                                                                                  y=30)
        title = Label(Frame_login, text='Billing Software', font=('Goudy old style', 15, 'bold'),
                      fg='Orange', bg='white').place(x=160, y=100)

        lbl_user = Label(Frame_login, text='Username :-', font=('Goudy old style', 15, 'bold'), fg='grey',
                         bg='white').place(x=90, y=140)
        self.txt_user = Entry(Frame_login, textvariable=self.txt_user, font=('times new roman', 15), bd=2,
                              bg='lightgrey')
        self.txt_user.place(x=200, y=140, width=200, height=35)

        lbl_pass = Label(Frame_login, text='Password   :-', font=('Goudy old style', 15, 'bold'), fg='grey',
                         bg='white').place(x=90, y=180)
        self.txt_pass = Entry(Frame_login, textvariable=self.txt_pass, font=('times new roman', 15), show="*", bd=2,
                              bg='lightgrey')
        self.txt_pass.place(x=200, y=180, width=200, height=35)

        logn = Button(Frame_login, text='SignIn', font=('Goudy old style', 16, 'bold'), bd=5, fg='grey',
                      bg='powder blue', width=8, activebackground='gold', command=self.login_function).place(x=140,
                                                                                                             y=240)

        extbtn = Button(Frame_login, text='Exit', width=8, font=('Goudy old style', 16, 'bold'), bd=5, fg='grey',
                        bg='powder blue', command=self.exit_try, activebackground='gold').place(x=280, y=240)

    def c_clock(self):
        h = str(time.strftime("%H"))
        m = str(time.strftime("%M"))
        s = str(time.strftime("%S"))
        #print(h, m, s)
        if int(h)>12 and int(m)>0:
            self.noon.config(text="PM")
        if int(h)>12:
            h=str((int(h)-12))
        self.hr.config(text=h)
        self.mn.config(text=m)
        self.sc.config(text=s)
        self.hr.after(200,self.c_clock)

    '''

    def c_clock(self, hr, mn, sc, noon):
        def clock():
            hr.config(text=time.strftime("%H"))
            mn.config(text=time.strftime("%M"))
            sc.config(text=time.strftime("%S"))
            noon.config(text=time.strftime("%p"))
            hr.after(200, clock)

        clock()
    '''

    def exit_try(self):
        option = messagebox.askyesno("Exit", "Do you want to exit?")
        if option > 0:
            self.root.destroy()
        else:
            return

    def login_function(self):
        if self.txt_user.get() == "Deep" and self.txt_pass.get() == "123456":
            self.root.destroy()
            import software
            software.inven_app()

        else:
            messagebox.showerror("Error", "Invalid Username/password", parent=self.root)


root = Tk()
obj = login(root)
root.mainloop()
