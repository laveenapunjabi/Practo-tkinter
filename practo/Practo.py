from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import webbrowser
import requests
import json
import smtplib

from smtplib import SMTPException



import sqlite3
connection = sqlite3.connect("laveena.db")
cursor = connection.cursor()

# create table

query = """
CREATE TABLE laveena ( 
username VARCHAR(20) PRIMARY KEY, 
password VARCHAR(20) NOT NULL);"""

cursor.execute(query)
connection.commit()


query = """ 
CREATE TABLE Appointment1(
    id INTEGER,
    docName VARCHAR(20) NOT NULL,
    patientName VARCHAR(20) NOT NULL);"""
cursor.execute(query)
connection.commit()


query = """
CREATE TABLE LabTest(
    Lid INTEGER,
    testName VARCHAR(20) NOT NULL,
    patientName VARCHAR(20) NOT NULL);"""
cursor.execute(query)
connection.commit()

query = """
CREATE TABLE Medicines(
    Mid INTEGER,
    medName VARCHAR(20) NOT NULL,
    patientName VARCHAR(20) NOT NULL);"""
cursor.execute(query)
connection.commit()


query = """
CREATE TABLE patient ( 
username VARCHAR(20) PRIMARY KEY, 
password VARCHAR(20) NOT NULL,
name VARCHAR(20) NOT NULL,
email VARCHAR(20) NOT NULL,
gender VARCHAR(10),
age INTEGER,
bloodgroup VARCHAR(10));"""

cursor.execute(query)
connection.commit()

query = """
CREATE TABLE buy(
    Pid INTEGER,
    planName VARCHAR(20) NOT NULL,
    patientName VARCHAR(20) NOT NULL);"""
cursor.execute(query)
connection.commit()

cursor.execute(" INSERT INTO laveena(username, password) values(?,?)",('lavi','123'))
query = "select * from laveena " 
cursor.execute(query)
result = cursor.fetchall()


cursor.execute("INSERT INTO patient(username,password,name,email,gender,age,bloodgroup) values(?,?,?,?,?,?,?)", ('username','password','name','email','gender','age','bloodgroup'))
query1 = "select * from patient "
cursor.execute(query1)
result = cursor.fetchall()


def f1():
	acc.deiconify()
	root.withdraw()
def f2():
	root.deiconify()
	acc.withdraw()
def f3():
	log.deiconify()
	root.withdraw()
def f4():
	wel.deiconify()
	log.withdraw()
def f6():
	news.deiconify()
	wel.withdraw()
def f17():
    home.deiconify()
    news.withdraw()
def f7():
	book.deiconify()
	home.withdraw()
def f8():
	home.deiconify()
	book.withdraw()
def f9():
	lab.deiconify()
	home.withdraw()
def f10():
	home.deiconify()
	lab.withdraw()
def f11():
	alpharoot.deiconify()
	home.withdraw()
def f12():
	home.deiconify()
	alpharoot.withdraw()
def f13():
	plan.deiconify()
	home.withdraw()
def f14():
	home.deiconify()
	plan.withdraw()
def f15():
    root.deiconify()
    log.withdraw()
def f16():
	acc.deiconify()
	home.withdraw()


#FIRST PAGE:
root = Tk()
root.title("Login page")
root.geometry("500x400+300+100")
# root.withdraw()
canvas0 = Canvas(root, width=500, height=400)
image0 = PhotoImage(file = r"log.png")
canvas0.create_image(0,0, anchor=NW, image=image0)
canvas0.pack()
image_samp = image0.subsample(4,4)
Label(root, image = image_samp).pack()

btn0 = Button(root,text="Login", bg= 'blue', fg = 'white', width="25", height = "2", command = f3)
btn0.place(x=160, y=100, anchor= 'nw')

label0 = Label(root, text="OR",width=10,bg= 'red', fg = 'yellow')
label0.place(x=210,y=180)

btn1 = Button(root, text="Create New Account", bg= 'blue', fg= 'white', width="25", height = "2", command = f1)
btn1.place(x=160, y=230, anchor= 'nw')


# #SECOND PAGE
acc = Toplevel(root)
acc.geometry('500x700+300+100')
acc.title("Registration Form")
acc.withdraw()
canvas1 = Canvas(acc, width = 500, height =700)
image1 = ImageTk.PhotoImage(Image.open("acc.jpg"))
canvas1.create_image(0,0,anchor = NW,image = image1)
canvas1.pack()

label1 = Label(acc, text="Registration Form",width=18,font=("Harlow Solid Italic", 20), bg= "light coral")
label1.place(x=80,y=53)

#changed here
fullname = StringVar()
email = StringVar()
age = StringVar()
bloodgrp = StringVar()
sign_username = StringVar()
passw = StringVar()

label2 = Label(acc, text="FullName", width=20,font=("bold", 10) ,bg = "teal")
label2.place(x=80,y=130)
entry2 = Entry(acc, textvariable=fullname)#changed here
entry2.place(x=260,y=130)

label3 = Label(acc, text="Email", width=20,font=("bold", 10) ,bg = "teal")
label3.place(x=80,y=180)
entry3 = Entry(acc, textvariable=email)#changed here
entry3.place(x=260,y=180)

label4 = Label(acc, text="Gender",width=20,font=("bold", 10) ,bg = "teal")
label4.place(x=80,y=230)
var = IntVar()
Radiobutton(acc, text="M",padx = 5, variable=var, value=1 ,bg = "dark sea green").place(x=260,y=230)
Radiobutton(acc, text="F",padx = 20, variable=var, value=2,bg = "dark sea green").place(x=300,y=230)

label5 = Label(acc, text="Age",width=20,font=("bold", 10) ,bg = "teal")
label5.place(x=80,y=280)
entry5 = Entry(acc, textvariable=age)#changed here
entry5.place(x=260,y=280)

label6 = Label(acc, text="Blood Group",width=20,font=("bold", 10) ,bg = "teal")
label6.place(x=80,y=330)
entry6 = Entry(acc, textvariable=bloodgrp)#changed here
entry6.place(x=260,y=330)

label_6 = Label(acc, text="Username:",width=20,font=("bold", 10) ,bg = "teal")
label_6.place(x=80,y=380)
entry_5 = Entry(acc,textvariable=sign_username)#changed here
entry_5.place(x=260,y=380)

label_7 = Label(acc, text="Password:",width=20,font=("bold", 10) ,bg = "teal")
label_7.place(x=80,y=430)
entry_6 = Entry(acc, show = '*', textvariable=passw)#changed here
entry_6.place(x=260,y=430)

Button(acc, text='Submit',width=20,command = lambda: regPatient(fullname.get(), email.get(), var.get(),age.get(), bloodgrp.get(), sign_username.get(),passw.get()),font=("Harlow Solid Italic", 11), bg= "light coral").place(x=160,y=500)

Button(acc,text="Back",width=20,font=("Harlow Solid Italic", 11),bg="light coral",command=f2).place(x=160,y=550)

#Button(acc,text="update",width=20,font=("Harlow Solid Italic", 11),bg="light coral",command= lambda: regPatient(fullname.get(), email.get(), var.get(),age.get(),bloodgrp(), sign_username.get(),passw.get())).place(x=160,y=550)

def regPatient(fullname,email,gender,age,bloodgrp, username,passw):
    cursor.execute("INSERT INTO patient(username,password,name,email,gender,age,bloodgroup) VALUES(?,?,?,?,?,?,?)", (username,passw,fullname,email,gender,age,bloodgrp))
    connection.commit()
    messagebox.showinfo("Registered!")
	
#THIRD PAGE:
def login(username, password):
	
	cursor.execute(f"SELECT * FROM laveena")
    
	result = cursor.fetchall()
	
	for res in result:
		if res[0] == username and res[1] == password:
			f4()
		else:
			messagebox.showerror("login error", "incorrect username or password")
			f3()
            
log = Toplevel(root)
log.geometry('450x460+300+100')
log.title("login")
log.withdraw()
canvas2 = Canvas(log, width=450, height=450)
image2 = ImageTk.PhotoImage(Image.open("login.jpg"))
canvas2.create_image(0,0,anchor = NW,image = image2)
canvas2.pack()
log.withdraw()
label8 = Label(log, text="Login",width=15,font=("Harlow Solid Italic", 18), bg="ivory")
label8.place(x=105,y=53)

label9 = Label(log, text="Username",width=20,font=("bold", 10), bg = "lightcyan")
label9.place(x=72,y=130)
username = StringVar() #changed here
entry9 = Entry(log, textvariable=username) #changed here
entry9.place(x=255,y=130)

label10 = Label(log, text="Password",width=20,font=("bold", 10), bg = "lightcyan")
label10.place(x=72,y=180)
password = StringVar()
entry11 = Entry(log,show = '*', textvariable=password) #changed here
entry11.place(x=255,y=180)

Button(log, text='Login',width=10,font=("algerian", 15),bg='ivory',fg='black', command= lambda: login(username.get(), password.get())).place(x=150,y=230) #changed here


label12 = Button(log, text="Back",width=15, font=("algerian", 15), bg= "dimgray", fg = "white", command=f15)
label12.place(x=120,y=300)

#FOURTH PAGE:
wel=Toplevel(log)
wel.title("Welcome page")
wel.geometry("600x400+300+100")

canvas3 = Canvas(wel, width=600, height=400)
image3 = ImageTk.PhotoImage(Image.open("welcome.jpg"))
canvas3.create_image(0,0, anchor=NW, image=image3)
canvas3.pack()
wel.withdraw()

label13=Label(wel,text='Welcome to our project',font='times 18 bold italic',fg="black",bg='light blue')
label13.place(x=180,y=10)

label14=Label(wel,text="Practo is giving you ₹100.00 worth of heatlthcare as a welcome gift\nYou canuse Healthcash to order medicines,chat with doctors online\n &even pay for health checkups @home ",font="12",bg="paleturquoise")
label14.place(x=0, y=60)

label15=Label(wel,text="Your HealthCash expires in 7 days ",font=("bold", 15), width=30, bg="paleturquoise")
label15.place(x=150, y=140)
w=Label(wel,text="Use HealthCash to stay healthy",font=("bold", 15), width=30, bg="paleturquoise")
w.place(x=150,y=180)

btn2=Button(wel,text="OK,got it!",font=("algerian",15,"bold"),width=15,bg = "black" , fg= "white", command =f6)
btn2.place(x=210, y=260)

def call_back():
    webbrowser.open_new(r"https://www.who.int/")


news = Toplevel(wel)
news.geometry('650x600+300+100')
news.title('Latest News')
news.withdraw()

l1 = Label(news, text = 'practo ', fg='blue',font = 'times 30 bold')
l1.pack()
l2 = Label(news, text='Precautions to be taken to amid \nCoronavirus outbreak!', font = "Helvetica 18 bold ")
l2.pack()

canvas19 = Canvas(news, width = 390, height =260)
image19 = ImageTk.PhotoImage(Image.open("img0.jpg"))
canvas19.create_image(0,0,anchor = NW,image = image19)
canvas19.pack(pady=20)

l3=Label(news, height = 200)
l3.pack(side=BOTTOM, fill = X)
b1 = Button(news, bg = 'red', text = 'Learn More', font = 'times 18 bold',fg='white', relief = RIDGE, command=call_back)
b1.place(x=250,y=480)
b2 = Button(news, bg = 'grey', text = 'cancel', font = 'times 18 bold',fg='black', relief = RIDGE, command=f17)
b2.place(x=540,y=10)




#FIVTH PAGE:
home = Toplevel(news)
home.title("Home")
home.geometry("500x400+300+100")
home.withdraw()
canvas4 = Canvas(home, width=500, height=400)
image4 = ImageTk.PhotoImage(Image.open("home.jpg"))
canvas4.create_image(0,0, anchor=NW, image=image4)
canvas4.pack()


label16 = Label(home, text='Location', width= 10, font=("bold", 15), bg= "silver", fg = "black" )
label16.place(x=5, y=5)

variable = StringVar(home)
variable.set("\t\t\t\t")
w = OptionMenu(home, variable,"\t Ahemdabad \t", "\t Auranagabad \t", "\t Bangalore \t", "\t Chennai \t", 
"\t Delhi \t", "\t Himachal Pradesh \t", "\t Hyderabad \t", "\t Jaipur \t", "\t Kolkata \t",
 "\t Mumbai \t", "\t Pune \t", "\t Rajasthan \t",  "\t Thane \t")
w.place(x=120, y=5)

btn3 = Button(home, text = 'Plans', width = 10, font=("bold", 15), bg= "teal", fg = "white", command = f13)
btn3.place(x=30,y=50)

#btn4 = Button(home, text = 'Profile', command=f16, width = 10, font=("bold", 15), bg= "teal", fg = "white")
#btn4.place(x=380,y=40)

btn5 = Button(home, text = 'Book Appointment', width = 25, font=("algerian", 15), bg= "ivory", fg = "black", command =f7)
btn5.place(x=100,y=160)

btn6 = Button(home, text = 'Lab Test', width = 20, font=("algerian", 15), bg= "ivory", fg = "black", command=f9)
btn6.place(x=120,y=220)

btn7 = Button(home, text = 'Medicines Booking', width = 20, font=("algerian", 15), bg= "ivory", fg = "black", command =f11)
btn7.place(x=120,y=280)




#SIXTH PAGE:BOOK

def b1():
	dbs.deiconify()
	book.withdraw()
def b2():
	book.deiconify()
	dbs.withdraw()

def b3():
	ski1.deiconify()
	book.withdraw()
def b4():
	book.deiconify()
	ski1.withdraw()

def b5():
	gp.deiconify()
	book.withdraw()
def b6():
	book.deiconify()
	gp.withdraw()

def b7():
	ds.deiconify()
	book.withdraw()
def b8():
	book.deiconify()
	ds.withdraw()


book = Toplevel(home)
book.title("Book Appointment")
book.geometry("750x600+300+100")

canvas5 = Canvas(book, width = 750, height = 200)
image5 = ImageTk.PhotoImage(Image.open("book.png"))
canvas5.create_image(0,0,anchor = NW,image = image5)
canvas5.pack()
book.withdraw()

btn8= Button(book, text="Back", font=('comic sans ms', 16, 'bold'),width = 10, command =f8)
btn8.place(x=600, y=580, anchor='sw')

lbl17 = Label(book, text="Search ", font=('comic sans ms', 16, 'bold'),bg= "cyan")
lbl17.place(x=0, y=210, anchor = 'nw')
variable = StringVar(book)
variable.set("\t\t\t\t")
w1 = OptionMenu(book,variable, "\t Dr. Akshay Jain \t", "\t Dr.Ajay Jhaveri \t", "\t Dr.Aparna Bhasker \t", 
 "\t Dr. Shubhashree Patil \t", "\t Dr.Smita Dash \t", "\t Dr.Dhruv Singh \t", "\t Dr.Shaurya Rohatgi \t", "\t Dr.Neha shah \t")
w1.place(x=90, y=210, anchor = 'nw')

photo5 = PhotoImage(file = r"ring.png") 
photoimage5 = photo5.subsample(6, 6) 
btnr = Button(book, text = 'Diabetes Specialist', image = photoimage5,compound = LEFT, width = 180,height = 70, command =b1)
btnr.place(x=100, y=270, anchor = 'nw')

photo6 = PhotoImage(file = r"skin.png") 
photoimage6 = photo6.subsample(5, 7) 
btnSk = Button(book, text = 'Skin Specialist', image = photoimage6,compound = LEFT, width = 180,height = 70, command = b3)
btnSk.place(x=330, y= 270, anchor = 'nw')

photo7 = PhotoImage(file = r"dr.png") 
photoimage7 = photo7.subsample(5, 6) 
btnDr1 = Button(book, text = 'General Physician', image = photoimage7,compound = LEFT, width = 185,height = 70, command = b5)
btnDr1.place(x=100, y=400, anchor = 'nw')

photo8 = PhotoImage(file = r"digestive.png") 
photoimage8 = photo8.subsample(8, 8) 
btnDi1 = Button(book, text = 'Digestive Issues', image = photoimage8,compound = LEFT, width = 180,height = 70, command = b7)
btnDi1.place(x=330, y=400, anchor = 'nw')

def booknow(id, docName, username):
	try:
		cursor.execute("INSERT INTO Appointment1(id,docName,patientName) VALUES(?,?,?)",(id,docName,username))
		messagebox.showinfo("booking", "appointment booked")
		b2()
	except:
		messagebox.showerror("booking error", "appointment canceled")
		cursor.execute("select * from Appointment1")
		res = cursor.fetchall
		print()


#diabetes

dbs = Toplevel(book)
dbs.geometry("500x400+300+100")
dbs.title("diabetes")
dbs.withdraw()

canvas6 = Canvas(dbs, width = 500, height = 400)
image6 = ImageTk.PhotoImage(Image.open("bg.jpg"))
canvas6.create_image(0,0,anchor = NW,image = image6)
canvas6.pack()

lbl18 = Label(dbs, text='Book your appointment with doctors', font=('algerian', 15), bg='ivory', fg= 'black', width= 40)
lbl18.place(x=0, y=10)

lbl19 = Label(dbs, text='Dr.Shubhashree Patil \n10 years experience overall \n consultation fee: ₹1,000',compound = LEFT, font=('book antique', 15), bg='light grey', fg= 'black', width= 30, height= 3)
lbl19.place(x=0, y=75, anchor = NW)

lbl20 = Label(dbs, text='Dr.Dhruv Singh \n22 years experience overall \n consultation fee: ₹1,500',  compound = LEFT, font=('book antique', 15), bg='light grey', fg= 'black', width= 30, height= 3)
lbl20.place(x=0, y=175, anchor = NW)
 
btn_book1= Button(dbs, text= 'Book Now', command= lambda : booknow(1,'Shubhashree',username.get()), font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 10)
btn_book1.place(x=350, y=90)

btn_book2= Button(dbs, text= 'Book Now',command= lambda : booknow(2,'Dhruv',username.get()), font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 10)
btn_book2.place(x=350, y=190)

btn_back= Button(dbs, text= 'Back',font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 5 , command=b2)
btn_back.place(x=400, y=300)

#skin

ski1 = Toplevel(book)
ski1.geometry("500x400+300+100")
ski1.title("skin")
ski1.withdraw()

canvas7 = Canvas(ski1, width = 500, height = 400)
image7 = ImageTk.PhotoImage(Image.open("bg.jpg"))
canvas7.create_image(0,0,anchor = NW,image = image7)
canvas7.pack()

lbl21 = Label(ski1, text='Book your appointment with doctors', font=('algerian', 15), bg='ivory', fg= 'black', width= 40)
lbl21.place(x=0, y=10)

lbl22 = Label(ski1, text='Dr.Shaurya Rohatgi \n10 years experience overall \n consultation fee: ₹700',compound = LEFT, font=('book antique', 15), bg='light grey', fg= 'black', width= 30, height= 3)
lbl22.place(x=0, y=75, anchor = NW)

lbl23 = Label(ski1, text='Dr.Neha Shah \n11 years experience overall \n consultation fee: ₹600',  compound = LEFT, font=('book antique', 15), bg='light grey', fg= 'black', width= 30, height= 3)
lbl23.place(x=0, y=175, anchor = NW)
 
btn_book3= Button(ski1, text= 'Book Now',command= lambda : booknow(3,'Shaurya',username.get()),font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 10)
btn_book3.place(x=350, y=90)

btn_book4= Button(ski1, text= 'Book Now',command= lambda : booknow(4,'Neha',username.get()), font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 10)
btn_book4.place(x=350, y=190)

btn_back1= Button(ski1, text= 'Back',font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 5 , command=b4)
btn_back1.place(x=400, y=300)


# general

gp = Toplevel(book)
gp.geometry("500x400+300+100")
gp.title("general")
gp.withdraw()

canvas8 = Canvas(gp, width = 500, height = 400)
image8 = ImageTk.PhotoImage(Image.open("bg.jpg"))
canvas8.create_image(0,0,anchor = NW,image = image8)
canvas8.pack()
lbl24 = Label(gp, text='Book your appointment with doctors', font=('algerian', 15), bg='ivory', fg= 'black', width= 40)
lbl24.place(x=0, y=10)

lbl25 = Label(gp, text='Dr.Akshay Jain \n6 years experience overall \n consultation fee: ₹400',compound = LEFT, font=('book antique', 15), bg='light grey', fg= 'black', width= 30, height= 3)
lbl25.place(x=0, y=75, anchor = NW)

lbl26 = Label(gp, text='Dr.Smita Dash \n17 years experience overall \n consultation fee: ₹600',  compound = LEFT, font=('book antique', 15), bg='light grey', fg= 'black', width= 30, height= 3)
lbl26.place(x=0, y=175, anchor = NW)
 
btn_book5= Button(gp, text= 'Book Now',command= lambda : booknow(5,'Akshay',username.get()), font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 10)
btn_book5.place(x=350, y=90)

btn_book6= Button(gp, text= 'Book Now',command= lambda : booknow(6,'Smita',username.get()), font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 10)
btn_book6.place(x=350, y=190)

btn_back2= Button(gp, text= 'Back',font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 5 , command=b6)
btn_back2.place(x=400, y=300)


#digestive
ds = Toplevel(book)
ds.geometry("500x400+300+100")
ds.title("digestive")
ds.withdraw()

canvas9 = Canvas(ds, width = 500, height = 400)
image9 = ImageTk.PhotoImage(Image.open("bg.jpg"))
canvas9.create_image(0,0,anchor = NW,image = image9)
canvas9.pack()
lbl0 = Label(ds, text='Book your appointment with doctors', font=('algerian', 15), bg='ivory', fg= 'black', width= 40)
lbl0.place(x=0, y=10)

lbl27 = Label(ds, text='Dr.Ajay Jhaveri \n14 years experience overall \n consultation fee: ₹2,000',compound = LEFT, font=('book antique', 15), bg='light grey', fg= 'black', width= 30, height= 3)
lbl27.place(x=0, y=75, anchor = NW)

lbl28 = Label(ds, text='Dr.Aparna Bhasker \n13 years experience overall \n consultation fee: ₹1,000',  compound = LEFT, font=('book antique', 15), bg='light grey', fg= 'black', width= 30, height= 3)
lbl28.place(x=0, y=175, anchor = NW)
 
btn_book7= Button(ds, text= 'Book Now',command= lambda : booknow(7,'Ajay',username.get()), font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 10)
btn_book7.place(x=350, y=90)

btn_book8= Button(ds, text= 'Book Now',command= lambda : booknow(8,'Aparna',username.get()), font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 10)
btn_book8.place(x=350, y=190)

btn_back3= Button(ds, text= 'Back',font=('book antique', 15), bg='ivory', fg= 'black', bd = 5, width= 5 , command=b8)
btn_back3.place(x=400, y=300)


#SEVENTH PAGE: LAB TEST

def l4():
	lab.withdraw()
	diab.deiconify()

def l5():
	lab.withdraw()
	ski.deiconify()	

def l6():
	lab.withdraw()
	fev.deiconify()	

def l7():
	lab.withdraw()
	dig.deiconify()	

def l8():
	diab.withdraw()
	lab.deiconify()

def l9():
	ski.withdraw()
	lab.deiconify()

def l10():
	fev.withdraw()
	lab.deiconify()

def l11():
	dig.withdraw()
	lab.deiconify()

#Lab test page

lab = Toplevel(home)
lab.geometry("750x600+300+00")
lab.withdraw()
canvas = Canvas(lab, width = 1000, height = 1000)
scrollbar = Scrollbar(lab,orient='vertical',command = canvas.yview)
image = ImageTk.PhotoImage(Image.open("test3.png"))

scrollable_frame = Frame(canvas)

scrollable_frame.bind(
'<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox('all','all')))

canvas.create_window((0,0),window = scrollable_frame,anchor='nw')

canvas.configure(yscrollcommand=scrollbar.set)

label = Label(scrollable_frame, image=image).grid(row = 2, column = 0, columnspan = 2, rowspan = 2, padx = 50, pady = 37)

lbscrollable_frameSearch = Label(scrollable_frame, text="Search ", font=('comic sans ms', 16, 'bold'))
lbscrollable_frameSearch.place(x = 80, y = 0)
variable = StringVar(scrollable_frame)
variable.set("\t\t\t\t")
w3 = OptionMenu(scrollable_frame,variable, "\t HbA1c \t",
 "\t Lipid Profile \t", "\t Vitamin D \t", "\t Vitamin Profile \t", "\t Liver Function scrollable_frame \t",
 "\t Lipase Serum \t", "\t Viral Fever \t")
w3.place(x = 180, y = 0)

btnscrollable_frameBack = Button(scrollable_frame, text="Back", font=('bold', 13),width = 8, command= f10)
btnscrollable_frameBack.place(x=0, y=0, anchor='nw')



photo1 = PhotoImage(file = r"ring.png")
photoimage1 = photo1.subsample(6, 6)
btnD = Button(scrollable_frame, text = 'Diabetes', image = photoimage1,compound = LEFT, width = 130,height = 70,command = l4)
btnD.grid(row = 4, column = 0, sticky = W, padx=0)

photo2 = PhotoImage(file = r"skin.png")
photoimage2 = photo2.subsample(5, 7)
btnS = Button(scrollable_frame, text = 'Skin', image = photoimage2,compound = LEFT, width = 130,height = 70,command = l5)
btnS.place(x=150,y=350)


photo3 = PhotoImage(file = r"dr.png")
photoimage3 = photo3.subsample(5, 6)
btnDr = Button(scrollable_frame, text = 'Fever', image = photoimage3,compound = LEFT, width = 130,height = 70,command = l6)
btnDr.place(x=300,y=350)

photo4 = PhotoImage(file = r"digestive.png")
photoimage4 = photo4.subsample(8, 8)
btnDi = Button(scrollable_frame, text = 'Digestive', image = photoimage4,compound = LEFT, width = 130,height = 70,command = l7)
btnDi.place(x=450,y=350)


lb3Name = Label(scrollable_frame, text = "Why book with us?", font = ('comic sans ms', 18, 'bold'))
lb3Name.grid(row = 5, column = 0, sticky = W, pady = 2)

lb4Name = Label(scrollable_frame, text = "1.Home sample collection for FREE", font = ('comic sans ms', 16, 'bold'))
lb4Name.grid(row = 6, column = 0, sticky = W, pady = 2)

lb5Name = Label(scrollable_frame, text = "A certified professional will collect your sample \n from a location of your preference ", font = ('comic sans ms', 14))
lb5Name.grid(row = 7, column = 0, sticky = W, pady = 2)

lb6Name = Label(scrollable_frame, text = "2.Practo Powered Labs", font = ('comic sans ms', 16, 'bold'))
lb6Name.grid(row = 8, column = 0, sticky = W, pady = 2)

lb7Name = Label(scrollable_frame, text = "Certified labs to ensure highest accuracy of your reports", font = ('comic sans ms', 14))
lb7Name.grid(row = 9, column = 0, sticky = W, pady = 2)

lb8Name = Label(scrollable_frame, text = "3.Digital reports", font = ('comic sans ms', 16, 'bold'))
lb8Name.grid(row = 10, column = 0, sticky = W, pady = 2)

lb9Name = Label(scrollable_frame, text = "Access your reports anytime on your Practo account.\n We will email you a copy", font = ('comic sans ms', 14))
lb9Name.grid(row = 11, column = 0, sticky = W, pady = 2)

lb10Name = Label(scrollable_frame, text = "4.Affordable prices", font = ('comic sans ms', 16, 'bold'))
lb10Name.grid(row = 12, column = 0, sticky = W, pady = 2)

lb11Name = Label(scrollable_frame, text = "Get great offers on tests and packages", font = ('comic sans ms', 14))
lb11Name.grid(row = 13, column = 0, sticky = W, pady = 2)

lb12Name = Label(scrollable_frame, text = "How it works?", font = ('comic sans ms', 16, 'bold'))
lb12Name.grid(row = 14, column = 0, sticky = W, pady = 2)

lb13Name = Label(scrollable_frame, text = "a.Search for test and packages and seamlessly book \n a home sample collection.", font = ('comic sans ms', 14))
lb13Name.grid(row = 15, column = 0, sticky = W, pady = 2)

lb14Name = Label(scrollable_frame, text = "--------------------------", font = ('comic sans ms', 22, 'bold'))
lb14Name.grid(row = 16, column = 0, sticky = E, pady = 2)

lb15Name = Label(scrollable_frame, text = "b.We will send a certified professional to your place to \n to assist you with the sample collection ", font = ('comic sans ms', 14))
lb15Name.grid(row = 17, column = 0, sticky = W, pady = 2)

lb16Name = Label(scrollable_frame, text = "--------------------------", font = ('comic sans ms', 22, 'bold'))
lb16Name.grid(row = 18, column = 0, sticky = E, pady = 2)

lb17Name = Label(scrollable_frame, text = "c.We will email you the reports.You can also access your reports \n within your account on the Practo app", font = ('comic sans ms', 14))
lb17Name.grid(row = 19, column = 0, sticky = W, pady = 2)

lb18Name = Label(scrollable_frame, text = "We do great", font = ('comic sans ms', 16, 'bold'))
lb18Name.grid(row = 20, column = 0, sticky = W, pady = 2)

lb19Name = Label(scrollable_frame, text = "a.Millions of users every month", font = ('comic sans ms', 15))
lb19Name.grid(row = 21, column = 0, sticky = W, pady = 2)

lb20Name = Label(scrollable_frame, text = "b.Trusted by many healthcare professionals", font = ('comic sans ms', 15))
#lb20Name.place(relx=0.0, rely=1.80, anchor='w')
lb20Name.grid(row = 22, column = 0, sticky = W, pady = 2)

lb21Name = Label(scrollable_frame, text = "c.We serve in many cities", font = ('comic sans ms', 15))
lb21Name.grid(row = 23, column = 0, sticky = W, pady = 2)


scrollbar.pack( side = RIGHT, fill = Y )
canvas.pack()

def labBook(Lid, testName, username):
	try:
		cursor.execute("INSERT INTO LabTest(Lid,testName,patientName) VALUES(?,?,?)",(Lid,testName,username))
		messagebox.showinfo("booking", "test booked")
		l8()
	except:
		messagebox.showerror("booking error", "test booking canceled")




#Diabetes page

diab = Toplevel(lab)
diab.title("Diabetes Checkup")
diab.geometry("750x600+300+00")
diab.withdraw()
canvas10 = Canvas(diab, width = 750, height = 600)
image10 = ImageTk.PhotoImage(Image.open("lab.jpg"))
canvas10.create_image(0,0,anchor = NW,image = image10)
canvas10.pack()

lb22Name = Label(diab, text = "Get Diabetic health checkups \nfrom the comfort of your home.", font = ('comic sans ms', 20, 'bold'), bg="ivory", fg = "blue") 
lb22Name.place(relx = 0.2, rely = 0.1, anchor = 'w')

lbDiab1 = Label(diab, text = "a.Free home sample pickup", font = ('comic sans ms', 16),bg = "light blue", fg= "Black") 
lbDiab1.place(relx = 0.0, rely = 0.25, anchor = 'w')

lbDiab2 = Label(diab, text = "b.Practo powered labs", font = ('comic sans ms', 16),bg = "light blue", fg= "Black") 
lbDiab2.place(relx = 0.55, rely = 0.25, anchor = 'w')

lbDiab3 = Label(diab, text = "c.E-Reports in 24-48 hours", font = ('comic sans ms', 16),bg = "light blue", fg= "Black")
lbDiab3.place(relx = 0.0, rely = 0.30, anchor = 'w')

lbDiab4 = Label(diab, text = "d.Free follow-up with a doctor", font = ('comic sans ms', 16), bg = "light blue", fg= "Black") 
lbDiab4.place(relx = 0.55, rely = 0.30, anchor = 'w')

lbDiab5 = Label(diab, text = "Diabetes Related Tests", font = ('comic sans ms', 20, 'bold'),  bg = 'white', fg = 'blue') 
lbDiab5.place(relx = 0.25, rely = 0.38, anchor = 'w')

lbDiab6 = Label(diab, text = "1.HbA1c", font = ('comic sans ms', 17, 'bold'),bg = "light blue", fg= "Black") 
lbDiab6.place(relx = 0.1, rely = 0.45, anchor = 'w')

lbDiab7 = Label(diab, text = "Known as Glycosylated \n Haemoglobin Blood  ", font = ('comic sans ms', 15),bg = "light blue", fg= "Black") 
lbDiab7.place(relx = 0.1, rely = 0.55, anchor = 'w')

lbDiab = Label(diab, text = "\u20B9 500", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbDiab.place(relx = 0.1, rely = 0.65, anchor = 'w')

btnDiab = Button(diab, text="Book", command= lambda : labBook(1,'HbA1c',username.get()), font = ('comic sans ms', 16, 'bold'),width = 15,bd = 8, bg = 'white', fg = 'blue')
btnDiab.place(relx = 0.1, rely = 0.75, anchor = 'w')

lbDiab8 = Label(diab, text = "2.Lipid Profile", font = ('comic sans ms', 17, 'bold'),bg = "light blue", fg= "Black") 
lbDiab8.place(relx = 0.59, rely = 0.45, anchor = 'w')

lbDiab9 = Label(diab, text = "Known as Glucose Fasting \n Blood ", font = ('comic sans ms', 15), bg = "light blue", fg= "Black") 
lbDiab9.place(relx = 0.59,rely = 0.55, anchor = 'w')

lbDiabb = Label(diab, text = "\u20B9 400", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbDiabb.place(relx = 0.59, rely = 0.65, anchor = 'w')

btnDiab1 = Button(diab, text="Book",command= lambda : labBook(2,'Lipid Profile',username.get()), font = ('comic sans ms', 16, 'bold'),width = 15, bd =8, bg = 'white', fg = 'blue')
btnDiab1.place(relx = 0.59, rely = 0.75, anchor = 'w')

btnDiabBack = Button(diab, text="Back", font=('comic sans ms', 16, 'bold'),width = 10, bd=8, command = l8)
btnDiabBack.place(x = 550, y = 520)

#Skin page

ski = Toplevel(lab)
ski.title("Skin Care")
ski.geometry("750x600+300+00")
ski.withdraw()
canvas11 = Canvas(ski, width = 750, height = 600)
image11 = ImageTk.PhotoImage(Image.open("lab.jpg"))
canvas11.create_image(0,0,anchor = NW,image = image11)
canvas11.pack()
lb23Name = Label(ski, text = "Get Skin Care checkups \nfrom the comfort of your home.", font = ('comic sans ms', 20, 'bold'), bg= "ivory", fg= 'blue') 
lb23Name.place(relx = 0.2, rely = 0.1, anchor = 'w')

lbski1 = Label(ski, text = "a.Free home sample pickup", font = ('comic sans ms', 16), bg = "light blue", fg= "Black") 
lbski1.place(relx = 0.0, rely = 0.25, anchor = 'w')

lbski2 = Label(ski, text = "b.Practo powered labs", font = ('comic sans ms', 16),bg = "light blue", fg= "Black") 
lbski2.place(relx = 0.55, rely = 0.25, anchor = 'w')

lbski3 = Label(ski, text = "c.E-Reports in 24-48 hours", font = ('comic sans ms', 16), bg = "light blue", fg= "Black")
lbski3.place(relx = 0.0, rely = 0.30, anchor = 'w')

lbski4 = Label(ski, text = "d.Free follow-up with a doctor", font = ('comic sans ms', 16), bg = "light blue", fg= "Black") 
lbski4.place(relx = 0.55, rely = 0.30, anchor = 'w')

lbski5 = Label(ski, text = "Skin Related Tests", font = ('comic sans ms', 20, 'bold'), bg = "ivory", fg= "Blue") 
lbski5.place(relx = 0.28, rely = 0.38, anchor = 'w')

lbski6 = Label(ski, text = "1.Vitamin D", font = ('comic sans ms', 17, 'bold'),bg = "light blue", fg= "Black") 
lbski6.place(relx = 0.1, rely = 0.45, anchor = 'w')

lbski7 = Label(ski, text = "Known as Viatmin D \n Profile Blood ", font = ('comic sans ms', 15), bg = "light blue", fg= "Black")
lbski7.place(relx = 0.1, rely = 0.55, anchor = 'w')

lbski = Label(ski, text = "\u20B9 1000", font = ('comic sans ms', 17, 'bold'),bg = "light blue", fg= "Black") 
lbski.place(relx = 0.1, rely = 0.65, anchor = 'w')

btnski = Button(ski, text="Book", command= lambda : labBook(3,'Vitamin D',username.get()),font = ('comic sans ms', 16, 'bold'),width = 15, bd = 8, bg = 'white', fg = 'blue')
btnski.place(relx = 0.1, rely = 0.75, anchor = 'w')

lbski8 = Label(ski, text = "2.Vitamin Profile", font = ('comic sans ms', 17, 'bold'),bg = "light blue", fg= "Black") 
lbski8.place(relx = 0.59, rely = 0.45, anchor = 'w')

lbski9 = Label(ski, text = "Known as Vitamin Profile \n Blood ", font = ('comic sans ms', 15), bg = "light blue", fg= "Black") 
lbski9.place(relx = 0.59, rely = 0.55, anchor = 'w')

lbskii = Label(ski, text = "\u20B9 1200", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbskii.place(relx = 0.59, rely = 0.65, anchor = 'w')

btnski1 = Button(ski, text="Book", command= lambda : labBook(4,'Viatmin Profile',username.get()), font = ('comic sans ms', 16, 'bold'),width = 15, bd=8, bg = 'white', fg = 'blue')
btnski1.place(relx = 0.59, rely = 0.75, anchor = 'w')

btnSkinBack = Button(ski, text="Back", font=('comic sans ms', 16, 'bold'),width = 10, bd =8, command = l9)
btnSkinBack.place(x = 550, y = 520)

#Fever page

fev = Toplevel(lab)
fev.title("Fever Checkup")
fev.geometry("750x600+300+00")
fev.withdraw()
canvas12 = Canvas(fev, width = 750, height = 600)
image12 = ImageTk.PhotoImage(Image.open("lab.jpg"))
canvas12.create_image(0,0,anchor = NW,image = image12)
canvas12.pack()

lb25Name = Label(fev, text = "Beat the fever before it beats you", font = ('comic sans ms', 20, 'bold'), bg= "ivory", fg='blue') 
lb25Name.place(relx = 0.2, rely = 0.1, anchor = 'w')

lbfev1 = Label(fev, text = "a.Free home sample pickup", font = ('comic sans ms', 16),  bg = "light blue", fg= "Black") 
lbfev1.place(relx = 0.0, rely = 0.25, anchor = 'w')

lbfev2 = Label(fev, text = "b.Practo powered labs", font = ('comic sans ms', 16),  bg = "light blue", fg= "Black") 
lbfev2.place(relx = 0.55, rely = 0.25, anchor = 'w')

lbfev3 = Label(fev, text = "c.E-Reports in 24-48 hours", font = ('comic sans ms', 16), bg = "light blue", fg= "Black")
lbfev3.place(relx = 0.0, rely = 0.30, anchor = 'w')

lbfev4 = Label(fev, text = "d.Free follow-up with a doctor", font = ('comic sans ms', 16),  bg = "light blue", fg= "Black") 
lbfev4.place(relx = 0.55, rely = 0.30, anchor = 'w')

lbfev5 = Label(fev, text = "Fever Related Tests", font = ('comic sans ms', 20, 'bold'), bg= "ivory", fg= 'blue') 
lbfev5.place(relx = 0.25, rely = 0.38, anchor = 'w')

lbfev6 = Label(fev, text = "1.Dengue NS1", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbfev6.place(relx = 0.1, rely = 0.45, anchor = 'w')

lbfev7 = Label(fev, text = "Known as Dengue Ns1 \n Antigen Pcr Blood ", font = ('comic sans ms', 15), bg = "light blue", fg= "Black") 
lbfev7.place(relx = 0.1, rely = 0.55, anchor = 'w')

lbfev = Label(fev, text = "\u20B9 500", font = ('comic sans ms', 17, 'bold'),bg = "light blue", fg= "Black") 
lbfev.place(relx = 0.1, rely = 0.65, anchor = 'w')

btnfev = Button(fev, text="Book", command= lambda : labBook(5,'Dengue Ns1',username.get()), font = ('comic sans ms', 16, 'bold'),width = 15, bd=8,  bg = 'white', fg = 'blue')
btnfev.place(relx = 0.1, rely = 0.75, anchor = 'w')

lbfev8 = Label(fev, text = "2.Dengue IgG", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbfev8.place(relx = 0.55, rely = 0.45, anchor = 'w')

lbfev9 = Label(fev, text = "Known as Dengue \n Antibodies Igg Elisa Blood", font = ('comic sans ms', 15), bg = "light blue", fg= "Black") 
lbfev9.place(relx = 0.55, rely = 0.55, anchor = 'w')

lbfevv = Label(fev, text = "\u20B9 500", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbfevv.place(relx = 0.55, rely = 0.65, anchor = 'w')

btnfev1 = Button(fev, text="Book",command= lambda : labBook(6,'Dengue IgG',username.get()), font = ('comic sans ms', 16, 'bold'),width = 15,bd=8,  bg = 'white', fg = 'blue')
btnfev1.place(relx = 0.55, rely = 0.75, anchor = 'w')

btnFevBack = Button(fev, text="Back", font=('comic sans ms', 16, 'bold'),width = 10,bd = 8, command = l10)
btnFevBack.place(x = 550, y = 520)

#Digestive page

dig = Toplevel(lab)
dig.title("Stomach and Diestion Checkup")
dig.geometry("750x600+300+00")
dig.withdraw()

canvas13 = Canvas(dig, width = 750, height = 600)
image13 = ImageTk.PhotoImage(Image.open("lab.jpg"))
canvas13.create_image(0,0,anchor = NW,image = image13)
canvas13.pack()

lb24Name = Label(dig, text = "Check your Digestive Health", font = ('comic sans ms', 20, 'bold'), bg= "ivory", fg = "blue") 
lb24Name.place(relx = 0.2, rely = 0.1, anchor = 'w')

lbdig1 = Label(dig, text = "a.Free home sample pickup", font = ('comic sans ms', 16),bg = "light blue", fg= "Black") 
lbdig1.place(relx = 0.0, rely = 0.25, anchor = 'w')

lbdig2 = Label(dig, text = "b.Practo powered labs", font = ('comic sans ms', 16),bg = "light blue", fg= "Black") 
lbdig2.place(relx = 0.55, rely = 0.25, anchor = 'w')

lbdig3 = Label(dig, text = "c.E-Reports in 24-48 hours", font = ('comic sans ms', 16), bg = "light blue", fg= "Black")
lbdig3.place(relx = 0.0, rely = 0.30, anchor = 'w')

lbdig4 = Label(dig, text = "d.Free follow-up with a doctor", font = ('comic sans ms', 16), bg = "light blue", fg= "Black") 
lbdig4.place(relx = 0.55, rely = 0.30, anchor = 'w')

lbdig5 = Label(dig, text = "Stomach and Digestion Related Tests", font = ('comic sans ms', 20, 'bold'), bg= "ivory", fg= "blue") 
lbdig5.place(relx = 0.11, rely = 0.38, anchor = 'w')

lbdig6 = Label(dig, text = "1.Liver Function Test", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbdig6.place(relx = 0.1, rely = 0.45, anchor = 'w')

lbdig7 = Label(dig, text = "Known as Liver Function \n Tests Blood ", font = ('comic sans ms', 15), bg = "light blue", fg= "Black") 
lbdig7.place(relx = 0.1, rely = 0.55, anchor = 'w')

lbdig = Label(dig, text = "\u20B9 400", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbdig.place(relx = 0.1, rely = 0.65, anchor = 'w')

btndig = Button(dig, text="Book",command= lambda : labBook(7,'Liver Function',username.get()), font = ('comic sans ms', 16, 'bold'),width = 15,bd=8, bg = 'white', fg = 'blue')
btndig.place(relx = 0.1, rely = 0.75, anchor = 'w')

lbdig8 = Label(dig, text = "2.Lipase Serum", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbdig8.place(relx = 0.55, rely = 0.45, anchor = 'w')

lbdig9 = Label(dig, text = "Known as Lipase Blood ", font = ('comic sans ms', 15), bg = "light blue", fg= "Black") 
lbdig9.place(relx = 0.55, rely = 0.55, anchor = 'w')

lbdigg = Label(dig, text = "\u20B9 400", font = ('comic sans ms', 17, 'bold'), bg = "light blue", fg= "Black") 
lbdigg.place(relx = 0.55, rely = 0.65, anchor = 'w')

btndig1 = Button(dig, text="Book",command= lambda : labBook(8,'Lipase Serum',username.get()), font = ('comic sans ms', 16, 'bold'),width = 15,bd=8, bg = 'white', fg = 'blue')
btndig1.place(relx = 0.55, rely = 0.75, anchor = 'w')

btnDigBack = Button(dig, text="Back", font=('comic sans ms', 16, 'bold'),width = 10,bd=8, command = l11)
btnDigBack.place(x = 550, y = 520)

#MEDICINES:
def m1():
	alpharoot.withdraw() 
	squareroot.deiconify()

def m2():
	alpharoot.withdraw()
	cuberoot.deiconify()

def m3():
	alpharoot.withdraw()
	teraroot.deiconify()

def m5():
	squareroot.withdraw()
	alpharoot.deiconify()

def m6():
	cuberoot.withdraw()
	alpharoot.deiconify()

def m7():
	teraroot.withdraw()
	alpharoot.deiconify()

alpharoot=Toplevel(home)
alpharoot.geometry("500x600+300+100")
alpharoot.title('medicines')
alpharoot.withdraw()

canvas14=Canvas(alpharoot,width=500,height=600)
image14=ImageTk.PhotoImage(Image.open("medicines1.png"))
canvas14.create_image(0,0,anchor=NW,image=image14)
canvas14.pack()


label31=Label(alpharoot,text="Types of medicines available ",font=("Bell MT",15,"bold"),width = 22, height = 1,bg="sandybrown",fg='black',bd=5)
label31.place(x=130,y=30)

btn31=Button(alpharoot,text="Tablets",font=("Inter ",18,"bold"), width=7, height= 1, bg="Black",fg="lime",bd=8,command=m1)
btn31.place(x=190,y=120)

btn32=Button(alpharoot,text="Capsules",font=("Inter ",18,"bold"),width=7, height= 1,bg="Black",fg="blue",bd=8,command=m2)
btn32.place(x=190,y=220)

btn33=Button(alpharoot,text="Injection",font=("Inter ",18,"bold"),width=7, height= 1,bg="Black",fg="yellow",bd=8,command=m3)
btn33.place(x=190,y=320)

btn34=Button(alpharoot,text="Back",font=("Inter ",18,"bold"), width=7, height= 1,bg="Black",fg="white",bd=8,command = f12)
btn34.place(x=190,y=450)

def orderMed(Mid, medName, username):
	try:
		cursor.execute("INSERT INTO MEDICINES(Mid,medName,patientName) VALUES(?,?,?)",(Mid,medName,username))
		messagebox.showinfo("booking", "medicines ordered")
		m6()
	except:
		messagebox.showerror("booking error", "medicines order canceled")



squareroot=Toplevel(alpharoot)
squareroot.title("tablets")
squareroot.geometry("500x500+300+100")
squareroot.withdraw()

canvas15=Canvas(squareroot,width=500,height=670)
image15=ImageTk.PhotoImage(Image.open("tablets-image.png"))
canvas15.create_image(0,0,anchor=NW,image=image15)
canvas15.pack()

btnback30=Button(squareroot,text="Back",font=("Inter ",12,"bold"),bg="Black",fg="lime",bd=8,command=m5)
btnback30.place(x=200,y=440)

label32=Label(squareroot,text="Metformin 500Mg \nIt is used for people who are overweight \n ₹250",font=("Bell MT",12,"bold"),bg="bisque",fg='red3',bd=2)
label32.place(x=10,y=30)

BtnBuy=Button(squareroot,text="Buy",command= lambda : orderMed(1,'Metformin',username.get()),font=("Inter",12,"bold"),height=1,bg="blue",fg="Black",bd=8)
BtnBuy.place(x=390,y=30)

label33=Label(squareroot,text="Imodium 250Mg \nfor Digestive issues \n₹180",font=("Bell MT",12,"bold"), width = 29, bg="bisque",fg='red3',bd=2)
label33.place(x=15,y=110)

BtnB1=Button(squareroot,text="Buy",command= lambda : orderMed(2,'Imodium',username.get()),font=("Inter",12,"bold"),bg="Blue",fg="Black",bd=8)
BtnB1.place(x=390,y=110)

label34=Label(squareroot,text="Levosiz 330Mg \nforSkin Disease. \n₹300",font=("Bell MT",12,"bold"), width= 29, bg="bisque",fg='red3',bd=2)
label34.place(x=15,y=190)

BtnB2=Button(squareroot,text="Buy",command= lambda : orderMed(3,'Levosiz',username.get()),font=("Inter",12,"bold"),bg="blue",fg="Black",bd=8)
BtnB2.place(x=390,y=200)

label35=Label(squareroot,text="Lamisil AT 320Mg \nfor Skin Fungus. \n₹440",font=("Bell MT",12,"bold"), width=29, bg="bisque",fg='red3',bd=2)
label35.place(x=15,y=280)

BtnB3=Button(squareroot,text="Buy",command= lambda : orderMed(4,'Lamisil',username.get()),font=("Inter",12,"bold"),bg="blue",fg="Black",bd=8)
BtnB3.place(x=390,y=280)

label36=Label(squareroot,text="cremaffin 180Mg \nfor Digestive. \n₹150",font=("Bell MT",12,"bold"), width=29, bg="bisque",fg='red3',bd=2)
label36.place(x=15,y=360)

BtnB4=Button(squareroot,text="Buy",command= lambda : orderMed(5,'cremaffin',username.get()),font=("Inter",12,"bold"),bg="blue",fg="Black",bd=8)
BtnB4.place(x=390,y=360)



cuberoot=Toplevel(alpharoot)
cuberoot.title("Capsules")
cuberoot.geometry("500x530+300+100")
cuberoot.withdraw()

canvas16=Canvas(cuberoot,width=500,height=530)
image16=ImageTk.PhotoImage(Image.open("capsules.jpg"))
canvas16.create_image(0,0,anchor=NW,image=image16)
canvas16.pack()

btnback80=Button(cuberoot,text="Back",font=("Inter ",12,"bold"),bg="black",fg="lime",bd=8,command=m6)
btnback80.place(x=200,y=460)

label37=Label(cuberoot,text="Erythromycin 250Mg \nfor Digestive issues. \n₹150",font=("Bell MT",12,"bold"), width=29, bg="snow",fg='red3',bd=2)
label37.place(x=20,y=30)

BtnB5=Button(cuberoot,text="Buy",command= lambda : orderMed(6,'Erythromycin',username.get()),font=("Inter",12,"bold"),bg="cyan",fg="Black",bd=8)
BtnB5.place(x=380,y=40)

label38=Label(cuberoot,text="amoxicillin 875Mg \nfor Skin Infection. \n₹480",font=("Bell MT",12,"bold"), width = 29, bg="snow",fg='red3',bd=2)
label38.place(x=20,y=110)

BtnB6=Button(cuberoot,text="Buy",command= lambda : orderMed(7,'amoxicillin',username.get()), font=("Inter",12,"bold"),bg="Cyan",fg="Black",bd=8)
BtnB6.place(x=380,y=110)

label39=Label(cuberoot,text="omez 750Mg \nfor Digestive. \n₹480",font=("Bell MT",12,"bold"), width=29, bg="snow",fg='red3',bd=2)
label39.place(x=20,y=190)

BtnB7=Button(cuberoot,text="Buy",command= lambda : orderMed(8,'omez',username.get()),font=("Inter",12,"bold"),bg="cyan",fg="Black",bd=8)
BtnB7.place(x=380,y=200)

label40=Label(cuberoot,text="Dazit 335Mg \nfor Diabetes \n₹500",font=("Bell MT",12,"bold"),width= 29, bg="snow",fg='red3',bd=2)
label40.place(x=20,y=270)

BtnB8=Button(cuberoot,text="Buy",command= lambda : orderMed(9,'Dazit',username.get()),font=("Inter",12,"bold"),bg="cyan",fg="Black",bd=8)
BtnB8.place(x=380,y=280)

label41=Label(cuberoot,text="Azifast 500Mg \nDiabetes. \n₹500",font=("Bell MT",12,"bold"),width=29,bg="snow",fg='red3',bd=2)
label41.place(x=20,y=350)

BtnB9=Button(cuberoot,text="Buy",command= lambda : orderMed(10,'Azifast',username.get()),font=("Inter",12,"bold"),bg="cyan",fg="Black",bd=8)
BtnB9.place(x=380,y=360)

teraroot=Toplevel(alpharoot)
teraroot.title("Injection")
teraroot.geometry("500x600+300+100")
teraroot.withdraw()

canvas17=Canvas(teraroot,width=500,height=600)
image17=ImageTk.PhotoImage(Image.open("injection1.jpg"))
canvas17.create_image(0,0,anchor=CENTER,image=image17)
canvas17.pack()

btnback81=Button(teraroot,text="Back",font=("Inter ",12,"bold"),bg="Black",fg="lime",bd=8,command=m7)
btnback81.place(x=170,y=500)

label42=Label(teraroot,text="Pramlintide 12ml \nfor Diabetes. \n₹320",font=("Inter",12,"bold"), width =29, bg="cyan",fg='Black',bd=2)
label42.place(x=20,y=30)

BtnB10=Button(teraroot,text="Buy",command= lambda : orderMed(11,'Pramlintide',username.get()),font=("Inter",12,"bold"),bg="black",fg="white",bd=8)
BtnB10.place(x=360,y=40)

label43=Label(teraroot,text="Epinephrine 15ml \nfor allergic. \n₹480",font=("Inter",12,"bold"), width =29, bg="cyan",fg='Black',bd=2)
label43.place(x=20,y=130)

BtnB11=Button(teraroot,text="Buy",command= lambda : orderMed(12,'Epinephrine',username.get()),font=("Inter",12,"bold"),bg="black",fg="white",bd=8)
BtnB11.place(x=360,y=130)

label44=Label(teraroot,text="Tetanus vaccine 15ml \n to prevent tetanus. \n₹480",font=("Inter",12,"bold"), width = 29, bg="cyan",fg='Black',bd=2)
label44.place(x=20,y=230)

BtnB12=Button(teraroot,text="Buy",command= lambda : orderMed(13,'Tetanus',username.get()),font=("Inter",12,"bold"),bg="black",fg="white",bd=8)
BtnB12.place(x=360,y=230)

label45=Label(teraroot,text="Herapin 15ml\nto prevent prevent blood clotting. \n₹480",font=("Inter",12,"bold"), width =29, bg="cyan",fg='Black',bd=2)
label45.place(x=20,y=330)

BtnB13=Button(teraroot,text="Buy",command= lambda : orderMed(14,'Herapin',username.get()),font=("Inter",12,"bold"),bg="black",fg="white",bd=8)
BtnB13.place(x=360,y=340)

def call():
    mail.deiconify()
    plan.withdraw()
def eplan():
    plan.deiconify()
    mail.withdraw()


def plans1(Pid, planName, username):
	try:
		cursor.execute("INSERT INTO buy(Pid,planName,patientName) VALUES(?,?,?)",(Pid,planName,username))
		messagebox.showinfo("booking", "plan booked")
		f13()
	except:
		messagebox.showerror("booking error", "plans order canceled")

def gmail():
    usermail = user_email.get()
    receivermail=receiver_email.get()           
    server=smtplib.SMTP('smtp.gmail.com:587')
    pass_word=password.get()
    subject=subj.get()
    #This allow you to include a subject by adding from, to and subject line
    main_message= """ You have Booked HealthCare Plan with Great Offers \n Thank You """
    Body="""From: Practo Team <usermail>
    To: receiver_email.get()
    Subject:%s 

    %s
    """ %(subject,main_message )


    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(usermail, pass_word  )
        server.sendmail(usermail,receivermail, Body )

        text.insert(1.0, 'message sent')
         #error handling
    except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
        text.insert(1.0, 'message not sent')
    finally:
        server.quit()

#PLANS:
plan=Toplevel(home)
plan.title("Practo Plans")
plan.geometry("500x750+300+30")
plan.withdraw()

canvas18 =Canvas(plan,width=500,height=750)
image18 =ImageTk.PhotoImage(Image.open("dna.jpg"))
canvas18.create_image(0,0,anchor=NW,image=image18)
canvas18.pack()


label46=Label(plan,text="Select a Practo Plus healthcare plan",font=("forte",20),bg="light grey")
label46.place(x=32, y=0) 

label47=Label(plan,text="ALL Plus plans are for 4 adults and 2 children" ,font=("Forte",17),bg="light grey")
label47.place(x=15, y=55)

label48=Label(plan,text="Basic Healthcare Plans",font=("Harlow Solid Italic",20),bg="white", fg="blue")
label48.place(x=120, y=110)

a = IntVar()
cb1 = Checkbutton(plan,text = "Unlimited consultations with any speciality",font= ("arial",15,"bold"),variable = a,bg="gainsboro")
a.set(1)
cb1.place(x=50, y=160)

b = IntVar()
cb2 = Checkbutton(plan,text = "20% OFF on presciption medicines",font= ("arial",15,"bold"),variable = b,bg="gainsboro")
b.set(1)
cb2.place(x=50, y=200)

c = IntVar()
cb3 = Checkbutton(plan,text = "20% OFF on tests & checkups",font= ("arial",15,"bold"),variable = c,bg="gainsboro")
c.set(1)
cb3.place(x=50, y=240)

label49=Label(plan,text="₹250/month\n₹2,999 billed yearly",font=("forte",18),bg="teal")
label49.place(x=5,y=300)

btn14=Button(plan,text="Buy Plan",command= call,font=("arial",18,"bold"),bd = 6, bg="black", fg= "white")
btn14.place(x=300,y=300)

label50=Label(plan,text="POPULAR",font=("algerian",20),bg="white", fg= "black")
label50.place(x=5,y=370)

label51=Label(plan,text="ADVANCED Healthcare Plans",font=("forte",22),bg="teal")
label51.place(x=5,y=420) 
	
d = IntVar()
cb4 = Checkbutton(plan,text = "Unlimited consultations with any speciality",font= ("arial",15,"bold"),variable = d,bg="light grey")
d.set(1)
cb4.place(x=40,y=460)

e = IntVar()
cb5 = Checkbutton(plan,text = "20% OFF on presciption medicines",font= ("arial",15,"bold"),variable = e,bg="light grey")
e.set(1)
cb5.place(x=40,y=490)

f = IntVar()
cb6 = Checkbutton(plan,text = "20% OFF on tests & checkups",font= ("arial",15,"bold"),variable = f,bg="light grey")
f.set(1)
cb6.place(x=40,y=525)

g=IntVar()
cb7 = Checkbutton(plan,text = "10 Free in-clinic Consultations",font= ("arial",15,"bold"),variable = g,bg="light grey")
g.set(1)
cb7.place(x=40,y=560)

label52=Label(plan,text="₹333/month\n₹3,999 billed yearly",font=("forte",18),bg="teal")
label52.place(x=5,y=600)

btn15=Button(plan,text="Buy Plan",command= call,font=("arial",18,"bold"), bd = 6, bg="black", fg= "white")
btn15.place(x=300,y=600)

btn16=Button(plan,text="Back",font=("arial",18,"bold"), bd = 6, bg="black", fg= "white", command=f14)
btn16.place(x=200,y=680)


#Mail

mail= Toplevel(plan)
mail.config(bg="brown", )
mail.withdraw()
#user mail
user_email = Label(mail, text="Enter your Gmail address:  ")
user_email.pack()
user_email.config(bg="black", fg="white")
user_email = Entry(mail, bd =8)
user_email.pack(fill=X)

#receiver email
receiver_email = Label(mail, text="Enter the recipient's email address: ")
receiver_email.pack( )
receiver_email.config(bg="black", fg="white")
receiver_email = Entry(mail, bd =8)
receiver_email.pack(fill=X)

#subject line
subj= Label(mail, text="Enter your subject here: ")
subj.pack( )
subj.config(bg="black", fg="white")
subj = Entry(mail, bd =8)
subj.pack(fill=X)

#password widget
password = Label(mail, text="Enter your Gmail password:  ")
password.pack()
password.config(bg="black", fg="white")

password= Entry(mail, show='*', bd =8)
password.pack(fill=X)

#submit button
submit_mail = Button(mail, bd =8, text="Click here to submit the mail",  
command=gmail)
submit_mail.pack(fill=X)

#feed back
text = Text(mail, font="Tahoma",  relief=SUNKEN , bd=8)
text.config(bg="pink",  height=2)
text.pack(fill=BOTH, expand=True)

back_button = Button(mail, text= "back", bd=8, command = eplan)
back_button.pack(fill=X)


root.mainloop()