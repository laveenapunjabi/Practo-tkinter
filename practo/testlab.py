from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("location.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

def f1():
	root.withdraw()
	sel.deiconify()

def f2():
	sel.withdraw()
	root.deiconify()

def f3():
	test.withdraw()
	root.deiconify()

def f4():
	test.withdraw()
	diab.deiconify()

def f5():
	test.withdraw()
	ski.deiconify()	

def f6():
	test.withdraw()
	fev.deiconify()	

def f7():
	test.withdraw()
	dig.deiconify()	

def f8():
	diab.withdraw()
	test.deiconify()

def f9():
	ski.withdraw()
	test.deiconify()

def f10():
	fev.withdraw()
	test.deiconify()

def f11():
	dig.withdraw()
	test.deiconify()


#Location page


#Lab test page

root = Tk()
app = Window(root)
root.geometry("750x600+300+00")
root.title("test lab")
canvas = Canvas(root, width = 1000, height = 1000)
scrollbar = Scrollbar(root,orient='vertical',command = canvas.yview)
image = ImageTk.PhotoImage(Image.open("test3.png"))

scrollable_frame = Frame(canvas)

scrollable_frame.bind(
'<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox('all','all')))

canvas.create_window((0,0),window = scrollable_frame,anchor='nw')

canvas.configure(yscrollcommand=scrollbar.set)

label = Label(scrollable_frame, image=image).grid(row = 2, column = 0, columnspan = 2, rowspan = 2, padx = 50, pady = 37)

lbscrollable_frameSearch = Label(scrollable_frame, text="Search ", font=('comic sans ms', 16, 'bold'))
lbscrollable_frameSearch.place(x = 20, y = 0)
variable = StringVar(scrollable_frame)
variable.set("\t\t\t\t")
w = OptionMenu(scrollable_frame,variable, "\t HbA1c \t",
 "\t Lipid Profile \t", "\t Vitamin D \t", "\t Vitamin Profile \t", "\t Liver Function scrollable_frame \t",
 "\t Lipase Serum \t", "\t Viral Fever \t")
w.place(x = 120, y = 0)

'''btnscrollable_frameBack = Button(scrollable_frame, text="Back", font=('comic sans ms', 16, 'bold'),width = 10, command = f3)
btnscrollable_frameBack.place(relx=0.55, rely=1.0, anchor='sw')'''



photo1 = PhotoImage(file = r"ring.png")
photoimage1 = photo1.subsample(6, 6)
btnD = Button(scrollable_frame, text = 'Diabetes', image = photoimage1,compound = LEFT, width = 130,height = 70,command = f4)
btnD.grid(row = 4, column = 0, sticky = W, padx=0)

photo2 = PhotoImage(file = r"skin.png")
photoimage2 = photo2.subsample(5, 7)
btnS = Button(scrollable_frame, text = 'Skin', image = photoimage2,compound = LEFT, width = 130,height = 70,command = f5)
btnS.place(x=150,y=350)


photo3 = PhotoImage(file = r"dr.png")
photoimage3 = photo3.subsample(5, 6)
btnDr = Button(scrollable_frame, text = 'Fever', image = photoimage3,compound = LEFT, width = 130,height = 70,command = f6)
btnDr.place(x=300,y=350)

photo4 = PhotoImage(file = r"digestive.png")
photoimage4 = photo4.subsample(8, 8)
btnDi = Button(scrollable_frame, text = 'Digestive', image = photoimage4,compound = LEFT, width = 130,height = 70,command = f7)
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


#Diabetes page

diab = Toplevel(root)
diab.title("Diabetes Checkup")
diab.geometry("750x600+300+00")
diab.configure(bg= "light coral")
lb22Name = Label(diab, text = "Get Diabetic health checkups \nfrom the comfort of your home.", font = ('comic sans ms', 20, 'bold'), bg="ivory") 
lb22Name.place(relx = 0.2, rely = 0.1, anchor = 'w')

lbDiab1 = Label(diab, text = "a.Free home sample pickup", font = ('comic sans ms', 16),bg = "ivory") 
lbDiab1.place(relx = 0.0, rely = 0.20, anchor = 'w')

lbDiab2 = Label(diab, text = "b.Practo powered labs", font = ('comic sans ms', 16),bg = "ivory") 
lbDiab2.place(relx = 0.5, rely = 0.20, anchor = 'w')

lbDiab3 = Label(diab, text = "c.E-Reports in 24-48 hours", font = ('comic sans ms', 16), bg ="ivory")
lbDiab3.place(relx = 0.0, rely = 0.25, anchor = 'w')

lbDiab4 = Label(diab, text = "d.Free follow-up with a doctor", font = ('comic sans ms', 16), bg= "ivory") 
lbDiab4.place(relx = 0.5, rely = 0.25, anchor = 'w')

lbDiab5 = Label(diab, text = "Diabetes Related Tests", font = ('comic sans ms', 20, 'bold'), bg= "ivory") 
lbDiab5.place(relx = 0.0, rely = 0.33, anchor = 'w')

lbDiab6 = Label(diab, text = "1.HbA1c", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbDiab6.place(relx = 0.0, rely = 0.42, anchor = 'w')

lbDiab7 = Label(diab, text = "Known as Glycosylated \n Haemoglobin Blood  ", font = ('comic sans ms', 15), bg= "ivory") 
lbDiab7.place(relx = 0.0, rely = 0.52, anchor = 'w')

lbDiab = Label(diab, text = "\u20B9 500", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbDiab.place(relx = 0.0, rely = 0.62, anchor = 'w')

btnDiab = Button(diab, text="Book", font = ('comic sans ms', 16, 'bold'),width = 15, bg = 'white', fg = 'blue')
btnDiab.place(relx = 0.0, rely = 0.70, anchor = 'w')

lbDiab8 = Label(diab, text = "2.Lipid Profile", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbDiab8.place(relx = 0.5, rely = 0.42, anchor = 'w')

lbDiab9 = Label(diab, text = "Known as Glucose Fasting \n Blood ", font = ('comic sans ms', 15), bg= "ivory") 
lbDiab9.place(relx = 0.5, rely = 0.52, anchor = 'w')

lbDiabb = Label(diab, text = "\u20B9 400", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbDiabb.place(relx = 0.5, rely = 0.62, anchor = 'w')

btnDiab1 = Button(diab, text="Book", font = ('comic sans ms', 16, 'bold'),width = 15, bg = 'white', fg = 'blue')
btnDiab1.place(relx = 0.5, rely = 0.70, anchor = 'w')

btnDiabBack = Button(diab, text="Back", font=('comic sans ms', 16, 'bold'),width = 10,command = f8)
btnDiabBack.place(x = 550, y = 520)


#Skin page

ski = Toplevel(root)
ski.title("Skin Care")
ski.geometry("750x600+300+00")
ski.configure(bg = "light coral")
lb23Name = Label(ski, text = "Get Skin Care checkups \nfrom the comfort of your home.", font = ('comic sans ms', 20, 'bold'), bg= "ivory") 
lb23Name.place(relx = 0.0, rely = 0.1, anchor = 'w')

lbski1 = Label(ski, text = "a.Free home sample pickup", font = ('comic sans ms', 16), bg= "ivory") 
lbski1.place(relx = 0.0, rely = 0.20, anchor = 'w')

lbski2 = Label(ski, text = "b.Practo powered labs", font = ('comic sans ms', 16), bg= "ivory") 
lbski2.place(relx = 0.5, rely = 0.20, anchor = 'w')

lbski3 = Label(ski, text = "c.E-Reports in 24-48 hours", font = ('comic sans ms', 16), bg= "ivory")
lbski3.place(relx = 0.0, rely = 0.25, anchor = 'w')

lbski4 = Label(ski, text = "d.Free follow-up with a doctor", font = ('comic sans ms', 16), bg= "ivory") 
lbski4.place(relx = 0.5, rely = 0.25, anchor = 'w')

lbski5 = Label(ski, text = "Skin Related Tests", font = ('comic sans ms', 20, 'bold'), bg= "ivory") 
lbski5.place(relx = 0.0, rely = 0.33, anchor = 'w')

lbski6 = Label(ski, text = "1.Vitamin D", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbski6.place(relx = 0.0, rely = 0.42, anchor = 'w')

lbski7 = Label(ski, text = "Known as Viatmin D \n Profile Blood ", font = ('comic sans ms', 15), bg= "ivory") 
lbski7.place(relx = 0.0, rely = 0.52, anchor = 'w')

lbski = Label(ski, text = "\u20B9 1000", font = ('comic sans ms', 17, 'bold')) 
lbski.place(relx = 0.0, rely = 0.62, anchor = 'w')

btnski = Button(ski, text="Book", font = ('comic sans ms', 16, 'bold'),width = 15, bg = 'white', fg = 'blue')
btnski.place(relx = 0.0, rely = 0.70, anchor = 'w')

lbski8 = Label(ski, text = "2.Vitamin Profile", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbski8.place(relx = 0.5, rely = 0.42, anchor = 'w')

lbski9 = Label(ski, text = "Known as Vitamin Profile \n Blood ", font = ('comic sans ms', 15), bg= "ivory") 
lbski9.place(relx = 0.5, rely = 0.52, anchor = 'w')

lbskii = Label(ski, text = "\u20B9 1200", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbskii.place(relx = 0.5, rely = 0.62, anchor = 'w')

btnski1 = Button(ski, text="Book", font = ('comic sans ms', 16, 'bold'),width = 15, bg = 'white', fg = 'blue')
btnski1.place(relx = 0.5, rely = 0.70, anchor = 'w')

btnSkinBack = Button(ski, text="Back", font=('comic sans ms', 16, 'bold'),width = 10,command = f9)
btnSkinBack.place(x = 550, y = 520)



#Fever page

fev = Toplevel(root)
fev.title("Fever Checkup")
fev.geometry("750x600+300+00")
fev.configure(bg = "light coral")
lb25Name = Label(fev, text = "Beat the fever before it beats you", font = ('comic sans ms', 20, 'bold'), bg= "ivory") 
lb25Name.place(relx = 0.0, rely = 0.1, anchor = 'w')

lbfev1 = Label(fev, text = "a.Free home sample pickup", font = ('comic sans ms', 16), bg= "ivory") 
lbfev1.place(relx = 0.0, rely = 0.20, anchor = 'w')

lbfev2 = Label(fev, text = "b.Practo powered labs", font = ('comic sans ms', 16), bg= "ivory") 
lbfev2.place(relx = 0.5, rely = 0.20, anchor = 'w')

lbfev3 = Label(fev, text = "c.E-Reports in 24-48 hours", font = ('comic sans ms', 16), bg= "ivory")
lbfev3.place(relx = 0.0, rely = 0.25, anchor = 'w')

lbfev4 = Label(fev, text = "d.Free follow-up with a doctor", font = ('comic sans ms', 16), bg= "ivory") 
lbfev4.place(relx = 0.5, rely = 0.25, anchor = 'w')

lbfev5 = Label(fev, text = "Fever Related Tests", font = ('comic sans ms', 20, 'bold'), bg= "ivory") 
lbfev5.place(relx = 0.0, rely = 0.33, anchor = 'w')

lbfev6 = Label(fev, text = "1.Dengue NS1", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbfev6.place(relx = 0.0, rely = 0.42, anchor = 'w')

lbfev7 = Label(fev, text = "Known as Dengue Ns1 \n Antigen Pcr Blood ", font = ('comic sans ms', 15), bg= "ivory") 
lbfev7.place(relx = 0.0, rely = 0.52, anchor = 'w')

lbfev = Label(fev, text = "\u20B9 500", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbfev.place(relx = 0.0, rely = 0.62, anchor = 'w')

btnfev = Button(fev, text="Book", font = ('comic sans ms', 16, 'bold'),width = 15, bg = 'white', fg = 'blue')
btnfev.place(relx = 0.0, rely = 0.70, anchor = 'w')

lbfev8 = Label(fev, text = "2.Dengue IgG", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbfev8.place(relx = 0.5, rely = 0.42, anchor = 'w')

lbfev9 = Label(fev, text = "Known as Dengue \n Antibodies Igg Elisa Blood", font = ('comic sans ms', 15), bg= "ivory") 
lbfev9.place(relx = 0.5, rely = 0.52, anchor = 'w')

lbfevv = Label(fev, text = "\u20B9 500", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbfevv.place(relx = 0.5, rely = 0.62, anchor = 'w')

btnfev1 = Button(fev, text="Book", font = ('comic sans ms', 16, 'bold'),width = 15, bg = 'white', fg = 'blue')
btnfev1.place(relx = 0.5, rely = 0.70, anchor = 'w')

btnFevBack = Button(fev, text="Back", font=('comic sans ms', 16, 'bold'),width = 10,command = f10)
btnFevBack.place(x = 550, y = 520)



#Digestive page

dig = Toplevel(root)
dig.title("Stomach and Diestion Checkup")
dig.geometry("750x600+300+00")
dig.configure(bg = "light coral")
lb24Name = Label(dig, text = "Check your Digestive Health", font = ('comic sans ms', 20, 'bold'), bg= "ivory") 
lb24Name.place(relx = 0.0, rely = 0.1, anchor = 'w')

lbdig1 = Label(dig, text = "a.Free home sample pickup", font = ('comic sans ms', 16), bg= "ivory") 
lbdig1.place(relx = 0.0, rely = 0.20, anchor = 'w')

lbdig2 = Label(dig, text = "b.Practo powered labs", font = ('comic sans ms', 16), bg= "ivory") 
lbdig2.place(relx = 0.5, rely = 0.20, anchor = 'w')

lbdig3 = Label(dig, text = "c.E-Reports in 24-48 hours", font = ('comic sans ms', 16), bg= "ivory")
lbdig3.place(relx = 0.0, rely = 0.25, anchor = 'w')

lbdig4 = Label(dig, text = "d.Free follow-up with a doctor", font = ('comic sans ms', 16), bg= "ivory") 
lbdig4.place(relx = 0.5, rely = 0.25, anchor = 'w')

lbdig5 = Label(dig, text = "Stomach and Digestion Related Tests", font = ('comic sans ms', 20, 'bold'), bg= "ivory") 
lbdig5.place(relx = 0.0, rely = 0.33, anchor = 'w')

lbdig6 = Label(dig, text = "1.Liver Function Test", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbdig6.place(relx = 0.0, rely = 0.42, anchor = 'w')

lbdig7 = Label(dig, text = "Known as Liver Function \n Tests Blood ", font = ('comic sans ms', 15), bg= "ivory") 
lbdig7.place(relx = 0.0, rely = 0.52, anchor = 'w')

lbdig = Label(dig, text = "\u20B9 400", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbdig.place(relx = 0.0, rely = 0.62, anchor = 'w')

btndig = Button(dig, text="Book", font = ('comic sans ms', 16, 'bold'),width = 15, bg = 'white', fg = 'blue')
btndig.place(relx = 0.0, rely = 0.70, anchor = 'w')

lbdig8 = Label(dig, text = "2.Lipase Serum", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbdig8.place(relx = 0.5, rely = 0.42, anchor = 'w')

lbdig9 = Label(dig, text = "Known as Lipase Blood ", font = ('comic sans ms', 15), bg= "ivory") 
lbdig9.place(relx = 0.5, rely = 0.52, anchor = 'w')

lbdigg = Label(dig, text = "\u20B9 400", font = ('comic sans ms', 17, 'bold'), bg= "ivory") 
lbdigg.place(relx = 0.5, rely = 0.62, anchor = 'w')

btndig1 = Button(dig, text="Book", font = ('comic sans ms', 16, 'bold'),width = 15, bg = 'white', fg = 'blue')
btndig1.place(relx = 0.5, rely = 0.70, anchor = 'w')

btnDigBack = Button(dig, text="Back", font=('comic sans ms', 16, 'bold'),width = 10,command = f11)
btnDigBack.place(x = 550, y = 520)




root.mainloop()