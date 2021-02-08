from tkinter import *
from tkinter import ttk, messagebox
import time
import os, re
import math, random
import datetime
import smtplib
import requests
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


class inven_app:
    def __init__(self):
        self.master = Tk()
        self.master.geometry("1545x847+0+0")
        self.master.resizable(False, False)
        self.master.title("Billing System")
        bg_color = "dark slate grey"
        self.bg = "black"
        title = Label(self.master, relief=GROOVE, text="Billing Software", font=("time new roman", 30, "bold"), bd=12, fg="orange", bg=bg_color, pady=2).pack(fill=X)

        # =========================Variables=========================================
        # =========================Cosmetic==========================================
        self.mois = IntVar()
        self.make = IntVar()
        self.face = IntVar()
        self.per = IntVar()
        self.sun = IntVar()
        self.eye = IntVar()
        self.blu = IntVar()
        # =========================Cold Drinks=======================================
        self.mou = IntVar()
        self.coc = IntVar()
        self.red = IntVar()
        self.pep = IntVar()
        self.spr = IntVar()
        self.vod = IntVar()
        self.zom = IntVar()
        # =========================Grocery===========================================
        self.rice = IntVar()
        self.oil = IntVar()
        self.milk = IntVar()
        self.mas = IntVar()
        self.whe = IntVar()
        self.salt = IntVar()
        self.dal = IntVar()
        # ==========================Total price & Tax variable========================
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ===========================customer=========================================
        self.c_name = StringVar()
        self.c_phon = StringVar()
        # num = lambda c_phon: c_phon < 11
        # self.c_phon.set(str(num))
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # ==========================Digital clock=============================
        digi = Label(self.master, text='Digital Clock', font='times 12 bold', relief=GROOVE, fg='orange', bd=12, pady=2, bg=bg_color)
        digi.place(x=0, y=75, height=40, width=1545)

        F0 = LabelFrame(self.master, font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        bd=10, relief=GROOVE)
        F0.place(x=0, y=115, relwidth=1, height=85)

        btn_C = Frame(F0, bd=10, relief=GROOVE, bg=bg_color)
        btn_C.place(x=570, width=360, height=70)

        # F0 = LabelFrame(self.master, bg='LightSteelBlue4',font='times 15 bold',relief=GROOVE, fg='orange',bd=12,pady=2)
        # F0.place(x=0, y=115, height=85, width=1530)

        self.hr = Label(btn_C, text=12, font=("times new roman", 25, "bold"), relief=RIDGE, bg="black", bd=10, fg='red', pady=5)

        # hr.grid(row=0,column=0,padx=0,pady=3)
        self.hr.place(x=7, y=0, height=51, width=78)

        # self.hr1 = Label(F01, text='HOUR', font=("times new roman", 15, "bold"), bg="white", fg='SkyBlue4')
        # self.hr1.place(x=30, y=72, height=20, width=100)

        self.mn = Label(btn_C, text='60', font=("times new roman", 25, "bold"), bg="black", fg='red', bd=10, relief=RIDGE, pady=5)

        # mn.grid(row=0, column=1, padx=0, pady=3)
        self.mn.place(x=92, y=0, height=51, width=78)

        # self.mn1 = Label(F01, text='MINUTE', font=("times new roman", 15, "bold"), bg="white", fg='SkyBlue4')
        # self.mn1.place(x=150, y=72, height=20, width=100)

        self.sc = Label(btn_C, text='60', font=("times new roman", 25, "bold"), bg="black", fg='red', bd=10, pady=5, relief=RAISED)
        self.sc.place(x=175, y=0, height=51, width=78)

        # self.sc1 = Label(F01, text='SECOND', font=("times new roman", 15, "bold"), bg="white", fg='SkyBlue4')
        # self.sc1.place(x=270, y=72, height=20, width=100)

        self.noon = Label(btn_C, text='AM', font=("times new roman", 20, "bold"), bg="black", fg='red', pady=5, bd=10, relief=RAISED)
        self.noon.place(x=258, y=0, height=51, width=78)

        # self.noon1 = Label(F01, text='AM/PM', font=("times new roman", 15, "bold"), bg="azure", fg='SkyBlue4')
        # self.noon1.place(x=390, y=72, height=20, width=80)

        # ==========================Customer Details=======================================
        F1 = LabelFrame(self.master, text="Customer Details", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color, bd=10, relief=GROOVE)
        F1.place(x=0, y=200, relwidth=1)  # y=80

        custname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="orange", font=("time new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        custname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        custno_lbl = Label(F1, text="Phone Number", bg=bg_color, fg="orange",
                           font=("time new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        custno_txt = Entry(F1, width=15, textvariable=self.c_phon, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        custbill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="orange",
                             font=("time new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        custbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=5, bg="powder blue", font="arial 15 bold", relief=RAISED).grid(row=0, column=7, pady=7, padx=10)

        # ===========================Cosmetics Frame=================================
        F2 = LabelFrame(self.master, text="Cosmetics", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        bd=10, relief=GROOVE)
        F2.place(x=5, y=300, width=325, height=380)  # y=180

        moi_lbl = Label(F2, text="Moisturizers", font=("time new roman", 12, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        moi_txt = Entry(F2, width=10, textvariable=self.mois, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        mak_lbl = Label(F2, text="Makeup Kits", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        mak_txt = Entry(F2, width=10, textvariable=self.make, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                                             padx=10, pady=10)

        fac_lbl = Label(F2, text="Face Powder", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        fac_txt = Entry(F2, width=10, textvariable=self.face, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                                             padx=10, pady=10)

        per_lbl = Label(F2, text="Perfume", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        per_txt = Entry(F2, width=10, textvariable=self.per, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                                            padx=10, pady=10)
        sun_lbl = Label(F2, text="Sun Scream", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sun_txt = Entry(F2, width=10, textvariable=self.sun, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                                            padx=10, pady=10)

        eye_lbl = Label(F2, text="Eyelash Curler", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        eye_txt = Entry(F2, width=10, textvariable=self.eye, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                                            padx=10, pady=10)

        blu_lbl = Label(F2, text="Blusher", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        blu_txt = Entry(F2, width=10, textvariable=self.blu, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=6, column=1,
                                                                                                                            padx=10, pady=10)

        # ===========================Cold Drink Frame=================================
        F3 = LabelFrame(self.master, text="Cold Drinks", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        bd=10, relief=GROOVE)
        F3.place(x=340, y=300, width=325, height=380)  # y=180

        mou_lbl = Label(F3, text="Mountain Dew", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        mou_txt = Entry(F3, width=10, textvariable=self.mou, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                                            padx=10, pady=10)

        coc_lbl = Label(F3, text="Coca-Cola", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        coc_txt = Entry(F3, width=10, textvariable=self.coc, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                                            padx=10, pady=10)

        red_lbl = Label(F3, text="Red Bull", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        red_txt = Entry(F3, width=10, textvariable=self.red, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                                            padx=10, pady=10)

        pep_lbl = Label(F3, text="Pepper Soda", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        pep_txt = Entry(F3, width=10, textvariable=self.pep, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                                            padx=10, pady=10)
        spr_lbl = Label(F3, text="Sprite", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        spr_txt = Entry(F3, width=10, textvariable=self.spr, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                                            padx=10, pady=10)

        vod_lbl = Label(F3, text="Vodka", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        vod_txt = Entry(F3, width=10, textvariable=self.vod, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                                            padx=10, pady=10)

        zom_lbl = Label(F3, text="Zombie", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        zom_txt = Entry(F3, width=10, textvariable=self.zom, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=6, column=1,
                                                                                                                            padx=10, pady=10)

        # ===========================Grocery Frame=================================
        F4 = LabelFrame(self.master, text="Grocery", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        bd=10, relief=GROOVE)
        F4.place(x=675, y=300, width=325, height=380)  # y=180

        ric_lbl = Label(F4, text="Rice", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ric_txt = Entry(F4, width=10, textvariable=self.rice, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1,
                                                                                                                             padx=10, pady=10)

        oil_lbl = Label(F4, text="Oil", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        oil_txt = Entry(F4, width=10, textvariable=self.oil, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                                            padx=10, pady=10)

        mil_lbl = Label(F4, text="Milk", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        mil_txt = Entry(F4, width=10, textvariable=self.milk, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                                             padx=10, pady=10)

        mas_lbl = Label(F4, text="Masala", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        mas_txt = Entry(F4, width=10, textvariable=self.mas, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                                            padx=10, pady=10)
        whe_lbl = Label(F4, text="Wheat", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        whe_txt = Entry(F4, width=10, textvariable=self.whe, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                                            padx=10, pady=10)

        sal_lbl = Label(F4, text="Salt", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sal_txt = Entry(F4, width=10, textvariable=self.salt, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                                             padx=10, pady=10)

        dal_lbl = Label(F4, text="Dal Mix", font=("time new roman", 12, "bold"), bg=bg_color,
                        fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        dal_txt = Entry(F4, width=10, textvariable=self.dal, font=("time new roman", 12, "bold"), bd=5, relief=SUNKEN).grid(row=6, column=1,
                                                                                                                            padx=10, pady=10)

        # ===========================Billing Frame=================================
        F5 = Frame(self.master, relief=GROOVE, bd=10, bg="powder blue")
        F5.place(x=1070, y=300, width=395, height=380)  # x=1070y=180
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrl_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrl_y.set, bg="powder blue")
        scrl_y.pack(side=RIGHT, fill=Y)
        scrl_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ==============================Button Frame===================================
        F6 = LabelFrame(self.master, text="Bill Menu", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                        bd=10, relief=GROOVE)
        F6.place(x=0, y=688, relwidth=1, height=140)  # 568

        m1 = Label(F6, text="Total Cosmetic Price", font=("time new roman", 12, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2 = Label(F6, text="Total Cold Drink Price", font=("time new roman", 12, "bold"), bg=bg_color,
                   fg="lightgreen").grid(row=1, column=0, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total Grocery Price", font=("time new roman", 12, "bold"), bg=bg_color,
                   fg="lightgreen").grid(row=2, column=0, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1 = Label(F6, text="Cosmetic Tax", font=("time new roman", 12, "bold"), bg=bg_color,
                   fg="lightgreen").grid(row=0, column=2, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2 = Label(F6, text="Cold Drink Tax", font=("time new roman", 12, "bold"), bg=bg_color,
                   fg="lightgreen").grid(row=1, column=2, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3 = Label(F6, text="Grocery Tax", font=("time new roman", 12, "bold"), bg=bg_color,
                   fg="lightgreen").grid(row=2, column=2, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE, bg="powder blue")
        btn_F.place(x=700, width=750, height=105)

        total_btn = Button(btn_F, text="Total", command=self.total, font=("time new roman", 10, "bold"), bg="dark slate blue", fg="white", pady=12,
                           width=10, bd=10).grid(row=0, column=0, padx=10, pady=10)
        gbill_btn = Button(btn_F, text="Genrate Bill", command=self.bill_area, font=("time new roman", 10, "bold"), bg="dark slate blue", fg="white", pady=12,
                           width=10, bd=10).grid(row=0, column=1, padx=10, pady=10)
        clear_btn = Button(btn_F, text="Clear", command=self.clear_data, font=("time new roman", 10, "bold"), bg="dark slate blue", fg="white", pady=12,
                           width=10, bd=10).grid(row=0, column=2, padx=10, pady=10)
        logout_btn = Button(btn_F, text="Logout", font=("time new roman", 10, "bold"),
                            bg="dark slate blue", command=self.logoutbtn, fg="white", pady=12,
                            width=10, bd=10).grid(row=0, column=3, padx=10, pady=10)

        exit_btn = Button(btn_F, text="Exit", command=self.Exit_App, font=("time new roman", 10, "bold"), bg="dark slate blue", fg="white", pady=12,
                          width=10, bd=10).grid(row=0, column=4, padx=10, pady=10)

        send_btn = Button(btn_F, text="Send", command=self.Send, font=("time new roman", 10, "bold"), bg="dark slate blue", fg="white", pady=12,
                          width=7, bd=10).grid(row=0, column=5, padx=10, pady=10)

        # ===================================
        # F7 = LabelFrame(self.master, text="Notes&Signature", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
        #                bd=10, relief=GROOVE)
        # F7.place(x=0, y=700, relwidth=1, height=120)

        self.c_clock()
        self.welcome_bill()
        self.root.mainloop()

    '''
    def p_num(self):

        if self.c_phon == 10:
            return self.c_phon
        else:
            messagebox.showerror("Error","Enter valid number")
    '''

    def c_clock(self):
        h = str(time.strftime("%H"))
        m = str(time.strftime("%M"))
        s = str(time.strftime("%S"))
        # print(h, m, s)
        if int(h) > 12 and int(m) > 0:
            self.noon.config(text="PM")
        if int(h) > 12:
            h = str((int(h) - 12))
        self.hr.config(text=h)
        self.mn.config(text=m)
        self.sc.config(text=s)
        self.hr.after(200, self.c_clock)

    def total(self):
        self.c_mo_p = self.mois.get() * 120
        self.c_ma_p = self.make.get() * 375
        self.c_fa_p = self.face.get() * 185
        self.c_pe_p = self.per.get() * 225
        self.c_su_p = self.sun.get() * 150
        self.c_ey_p = self.eye.get() * 320
        self.c_bl_p = self.blu.get() * 120

        self.total_cosmetic_price = float(
            self.c_mo_p +
            self.c_ma_p +
            self.c_fa_p +
            self.c_pe_p +
            self.c_su_p +
            self.c_ey_p +
            self.c_bl_p
        )
        self.cosmetic_price.set("Rs. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.24), 2)
        self.cosmetic_tax.set("Rs. " + str(self.c_tax))

        self.c_m_p = self.mou.get() * 40
        self.c_c_p = self.coc.get() * 35
        self.c_r_p = self.red.get() * 120
        self.c_p_p = self.pep.get() * 30
        self.c_s_p = self.spr.get() * 35
        self.c_v_p = self.vod.get() * 450
        self.c_z_p = self.zom.get() * 1100

        self.total_cold_drink_price = float(
            self.c_m_p +
            self.c_c_p +
            self.c_r_p +
            self.c_p_p +
            self.c_s_p +
            self.c_v_p +
            self.c_z_p
        )
        self.cold_drink_price.set("Rs. " + str(self.total_cold_drink_price))
        self.cold_tax = round((self.total_cold_drink_price * 0.18), 2)
        self.cold_drink_tax.set("Rs. " + str(self.cold_tax))

        self.g_r_p = self.rice.get() * 65
        self.g_o_p = self.oil.get() * 85
        self.g_m_p = self.milk.get() * 28
        self.g_ma_p = self.mas.get() * 250
        self.g_w_p = self.whe.get() * 25
        self.g_s_p = self.salt.get() * 20
        self.g_d_p = self.dal.get() * 350

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_o_p +
            self.g_m_p +
            self.g_ma_p +
            self.g_w_p +
            self.g_s_p +
            self.g_d_p
        )
        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.Total_bill = round(float(self.total_cosmetic_price +
                                      self.total_cold_drink_price +
                                      self.total_grocery_price +
                                      self.c_tax +
                                      self.cold_tax +
                                      self.g_tax
                                      ), 2)

    def realtime(self):
        now = datetime.datetime.now()
        return now.strftime("%Y/%m/%d")

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t    Welcome Bhavani Store\n")
        self.txtarea.insert(END, f"\n Bill Number      :{self.bill_no.get()}")
        self.txtarea.insert(END, f"          {self.realtime()}")
        self.txtarea.insert(END, f"\n Customer Name    :{self.c_name.get()}")
        self.txtarea.insert(END, f"\n Customer Number  :{self.c_phon.get()}")
        self.txtarea.insert(END, f"\n============================================")
        self.txtarea.insert(END, f"\n Products Name\t\t      QTY  \t\t      Price")
        self.txtarea.insert(END, f"\n============================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phon.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif self.cosmetic_price.get() == "Rs. 0.0" and self.cold_drink_tax.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No any product purchase")
        else:
            self.welcome_bill()
            # ==============Cosmetic======================
            if self.mois.get() != 0:
                self.txtarea.insert(END, f"\n Moisturizers\t\t\t{self.mois.get()}          \t{self.c_mo_p}")
            if self.make.get() != 0:
                self.txtarea.insert(END, f"\n Makeup Kits\t\t\t{self.make.get()}          \t{self.c_ma_p}")
            if self.face.get() != 0:
                self.txtarea.insert(END, f"\n Face Powder\t\t\t{self.face.get()}          \t{self.c_fa_p}")
            if self.per.get() != 0:
                self.txtarea.insert(END, f"\n Perfume\t\t\t{self.per.get()}          \t{self.c_pe_p}")
            if self.sun.get() != 0:
                self.txtarea.insert(END, f"\n Sun Scream\t\t\t{self.sun.get()}          \t{self.c_su_p}")
            if self.eye.get() != 0:
                self.txtarea.insert(END, f"\n Eyelash Curler\t\t\t{self.eye.get()}          \t{self.c_ey_p}")
            if self.blu.get() != 0:
                self.txtarea.insert(END, f"\n Blusher\t\t\t{self.blu.get()}          \t{self.c_bl_p}")

            # ============================Cold Drink================================
            if self.mou.get() != 0:
                self.txtarea.insert(END, f"\n Mountain Dew\t\t\t{self.mou.get()}          \t{self.c_m_p}")
            if self.coc.get() != 0:
                self.txtarea.insert(END, f"\n Coca-Cola\t\t\t{self.coc.get()}          \t{self.c_c_p}")
            if self.red.get() != 0:
                self.txtarea.insert(END, f"\n Red Bull\t\t\t{self.red.get()}          \t{self.c_r_p}")
            if self.pep.get() != 0:
                self.txtarea.insert(END, f"\n Pepper Soda\t\t\t{self.pep.get()}          \t{self.c_p_p}")
            if self.spr.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t\t{self.spr.get()}          \t{self.c_s_p}")
            if self.vod.get() != 0:
                self.txtarea.insert(END, f"\n Vodka\t\t\t{self.vod.get()}          \t{self.c_v_p}")
            if self.zom.get() != 0:
                self.txtarea.insert(END, f"\n Zombie\t\t\t{self.zom.get()}          \t{self.c_z_p}")

            # ================================Grocery===================================
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t\t{self.rice.get()}        \t{self.g_r_p}")
            if self.oil.get() != 0:
                self.txtarea.insert(END, f"\n Oil\t\t\t{self.oil.get()}          \t{self.g_o_p}")
            if self.milk.get() != 0:
                self.txtarea.insert(END, f"\n Milk\t\t\t{self.milk.get()}          \t{self.g_m_p}")
            if self.mas.get() != 0:
                self.txtarea.insert(END, f"\n Masala\t\t\t{self.mas.get()}          \t{self.g_ma_p}")
            if self.whe.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t\t{self.whe.get()}          \t{self.g_w_p}")
            if self.salt.get() != 0:
                self.txtarea.insert(END, f"\n Salt\t\t\t{self.salt.get()}          \t{self.g_s_p}")
            if self.dal.get() != 0:
                self.txtarea.insert(END, f"\n Dal Mix\t\t\t{self.dal.get()}          \t{self.g_d_p}")

            self.txtarea.insert(END, f"\n--------------------------------------------")
            if self.cosmetic_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cosmatic Tax:\t\t\t\t{self.cosmetic_tax.get()}")

            if self.cold_drink_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax:\t\t\t\t{self.cold_drink_tax.get()}")

            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax:\t\t\t\t{self.grocery_tax.get()}")

            self.txtarea.insert(END, f"\n--------------------------------------------")
            self.txtarea.insert(END, f"\n Total Bill\t\t\t\tRs. {round(self.Total_bill, 2)}")
            self.txtarea.insert(END, f"\n============================================")
            self.txtarea.insert(END, f"\n\t\t\t\t   Thank you")
            self.txtarea.insert(END, f"\n Notes:-")
            self.txtarea.insert(END, f"\n*Please check product before purchase")
            self.txtarea.insert(END, f"\n*No returns No Exchanges")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill No. : {self.bill_no.get()} Saved Successfully")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            # =========================Cosmetic==========================================
            self.mois.set(0)
            self.make.set(0)
            self.face.set(0)
            self.per.set(0)
            self.sun.set(0)
            self.eye.set(0)
            self.blu.set(0)
            # =========================Cold Drinks=======================================
            self.mou.set(0)
            self.coc.set(0)
            self.red.set(0)
            self.pep.set(0)
            self.spr.set(0)
            self.vod.set(0)
            self.zom.set(0)
            # =========================Grocery===========================================
            self.rice.set(0)
            self.oil.set(0)
            self.milk.set(0)
            self.mas.set(0)
            self.whe.set(0)
            self.salt.set(0)
            self.dal.set(0)
            # ==========================Total price & Tax variable========================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            # ===========================customer=========================================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def logoutbtn(self):
        self.master.destroy()
        import Billing_system

    def Exit_App(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.master.destroy()

    def Send(self):
        root = Tk()
        root.geometry('500x500')
        root.title("Sending Bill")
        root['bg'] = "white"

        frame4 = Frame(root, width=500, height=60, relief=RIDGE, borderwidth=5, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        frame4.place(x=0, y=0)

        l2 = Label(frame4, text="Send Bill", font=('roboto', 22, 'bold'), bg='#248aa2', fg="#ffffff")
        l2.place(x=100, y=1)

        frame5 = Frame(root, width=500, height=440, relief=RIDGE, borderwidth=5, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        frame5.place(x=0, y=55)

        innerframe5 = Frame(frame5, width=485, height=425, relief=RIDGE, borderwidth=3, bg='#248aa2', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        innerframe5.place(x=0, y=0)

        l3 = LabelFrame(innerframe5, text="Send Bill Through Email", width=470, height=410, borderwidth=3, font=('verdana', 10, 'bold'), fg='#248aa2', relief=RIDGE, highlightbackground="white", highlightcolor="white", highlightthickness=2)
        l3.place(x=2, y=2)

        uname = Label(innerframe5, text="Username", font=('verdana', 10, 'bold'))
        uname.place(x=40, y=20)

        number01 = Entry(innerframe5, width=40, borderwidth=2)
        number01.place(x=40, y=40)

        pw = Label(innerframe5, text="Password", font=('verdana', 10, 'bold'))
        pw.place(x=40, y=60)

        number02 = Entry(innerframe5, width=40, borderwidth=2, show='*')
        number02.place(x=40, y=80)

        too = Label(innerframe5, text="To", font=('verdana', 10, 'bold'))
        too.place(x=40, y=100)

        number03 = Entry(innerframe5, width=40, borderwidth=2)
        number03.place(x=40, y=120)

        sub = Label(innerframe5, text="Subject", font=('verdana', 10, 'bold'))
        sub.place(x=40, y=140)

        number04 = Entry(innerframe5, width=40, borderwidth=2)
        number04.place(x=40, y=160)

        l5 = Label(innerframe5, text="Bill Details", font=('verdana', 10, 'bold'))
        l5.place(x=40, y=180)

        b_detail = ScrolledText(innerframe5, width=45, height=10, relief=RIDGE, borderwidth=3)
        b_detail.place(x=40, y=200)

        b_detail.insert(1.0, self.txtarea.get('1.0', END))

        def send_bill():
            try:
                username = number01.get()
                password = number02.get()
                receiver = number03.get()
                subject = number04.get()
                messages = b_detail.get("1.0", "end-1c")

                if username == "" or password == "" or receiver == "" or subject == "" or messages == "":
                    messagebox.showerror("Error", 'Please fill the phone number')
                elif messages == "":
                    messagebox.showerror("Error", 'Bill Details is empty')
                else:
                    finalMessage = 'Subject: {}\n\n{}'.format(subject, messages)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(username, password)
                    server.sendmail(username, receiver, finalMessage)
                    messagebox.showinfo("Send Mail", 'Bill has been send to your successfully')

            except:
                messagebox.showinfo("Error", "Something wrong")

        send_msg = Button(innerframe5, text="Send Bill", relief=RAISED, borderwidth=2, font=('verdana', 8, 'bold'), bg='#248aa2', fg="white", padx=20, command=send_bill)
        send_msg.place(x=100, y=380)

        root.mainloop()
