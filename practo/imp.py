from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.geometry("750x600+300+00")
root.configure(bg="blue")

def f1():
	root.withdraw()
	log.deiconify()

canvas = Canvas(root, width = 750, height = 600)
scrollbar = Scrollbar(root,orient='vertical',command = canvas.yview)
image = ImageTk.PhotoImage(Image.open("test3.png"))

scrollable_frame = Frame(canvas)

scrollable_frame.bind(
'<Configure>',lambda e: canvas.configure(scrollregion = canvas.bbox('all','all')))

canvas.create_window((0,0),window = scrollable_frame,anchor='nw')

canvas.configure(yscrollcommand=scrollbar.set)

label = Label(scrollable_frame, image=image).grid(row = 0, column = 0, columnspan = 1, rowspan = 1, padx = 2, pady = 2)

lbscrollable_frameSearch = Label(scrollable_frame, text="Search ", font=('comic sans ms', 16, 'bold'))

variable = StringVar(scrollable_frame)
variable.set("\t\t\t\t")
w = OptionMenu(scrollable_frame,variable, "\t HbA1c \t",
 "\t Lipid Profile \t", "\t Vitamin D \t", "\t Vitamin Profile \t", "\t Liver Function scrollable_frame \t",
 "\t Lipase Serum \t", "\t Viral Fever \t")
# w.place(relx = 0.1, rely = 0.02, anchor = 'nw')

'''btnscrollable_frameBack = Button(scrollable_frame, text="Back", font=('comic sans ms', 16, 'bold'),width = 10, command = f3)
btnscrollable_frameBack.place(relx=0.55, rely=1.0, anchor='sw')'''



photo1 = PhotoImage(file = r"ring.png")
photoimage1 = photo1.subsample(6, 6)
btnD = Button(scrollable_frame, text = 'Diabetes', image = photoimage1,compound = LEFT, width = 130,height = 70, command = f1)
#btnD.place(x=10,y=400)
btnD.grid(row = 2, column = 0, sticky = W, padx=0)

photo2 = PhotoImage(file = r"skin.png")
photoimage2 = photo2.subsample(5, 7)
btnS = Button(scrollable_frame, text = 'Skin', image = photoimage2,compound = LEFT, width = 130,height = 70)
# #btnS.place(x=160,y=400)
btnS.grid(row= 2, column = 1,sticky = W+E, padx=2)

photo3 = PhotoImage(file = r"dr.png")
photoimage3 = photo3.subsample(5, 6)
btnDr = Button(scrollable_frame, text = 'Fever', image = photoimage3,compound = LEFT, width = 130,height = 70)
#btnDr.place(x=310,y=400)
btnDr.grid(row= 2, column = 2,sticky = W+E, columnspan = 4)

photo4 = PhotoImage(file = r"digestive.png")
photoimage4 = photo4.subsample(8, 8)
btnDi = Button(scrollable_frame, text = 'Digestive', image = photoimage4,compound = LEFT, width = 130,height = 70)
#btnDi.place(x=460,y=400)
btnDi.grid(row= 2, column = 3,sticky = W+E, columnspan = 4)

lb3Name = Label(scrollable_frame, text = "Why book with us?", font = ('comic sans ms', 18, 'bold'))
#lb3Name.place(relx=0.0, rely=0.85, anchor='w')
lb3Name.grid(row = 5, column = 0, sticky = W, pady = 2)

lb4Name = Label(scrollable_frame, text = "1.Home sample collection for FREE", font = ('comic sans ms', 16, 'bold'))
#lb4Name.place(relx=0.0, rely=0.9, anchor='w')
lb4Name.grid(row = 6, column = 0, sticky = W, pady = 2)

lb5Name = Label(scrollable_frame, text = "A certified professional will collect your sample \n from a location of your preference ", font = ('comic sans ms', 14))
#lb5Name.place(relx=0.0, rely=0.98, anchor='w')
lb5Name.grid(row = 7, column = 0, sticky = W, pady = 2)

lb6Name = Label(scrollable_frame, text = "2.Practo Powered Labs", font = ('comic sans ms', 16, 'bold'))
#lb6Name.place(relx=0.0, rely=1.0, anchor='w')
lb6Name.grid(row = 8, column = 0, sticky = W, pady = 2)

lb7Name = Label(scrollable_frame, text = "Certified labs to ensure highest accuracy of your reports", font = ('comic sans ms', 14))
#lb7Name.place(relx=0.0, rely=1.05, anchor='w')
lb7Name.grid(row = 9, column = 0, sticky = W, pady = 2)

lb8Name = Label(scrollable_frame, text = "3.Digital reports", font = ('comic sans ms', 16, 'bold'))
#lb8Name.place(relx=0.0, rely=1.10, anchor='w')
lb8Name.grid(row = 10, column = 0, sticky = W, pady = 2)

lb9Name = Label(scrollable_frame, text = "Access your reports anytime on your Practo account.\n We will email you a copy", font = ('comic sans ms', 14))
#lb9Name.place(relx=0.0, rely=1.15, anchor='w')
lb9Name.grid(row = 11, column = 0, sticky = W, pady = 2)

lb10Name = Label(scrollable_frame, text = "4.Affordable prices", font = ('comic sans ms', 16, 'bold'))
#lb10Name.place(relx=0.0, rely=1.20, anchor='w')
lb10Name.grid(row = 12, column = 0, sticky = W, pady = 2)

lb11Name = Label(scrollable_frame, text = "Get great offers on scrollable_frames", font = ('comic sans ms', 14))
#lb11Name.place(relx=0.0, rely=1.25, anchor='w')
lb11Name.grid(row = 13, column = 0, sticky = W, pady = 2)

lb12Name = Label(scrollable_frame, text = "How it works?", font = ('comic sans ms', 16, 'bold'))
#lb12Name.place(relx=0.0, rely=1.35, anchor='w')
lb12Name.grid(row = 14, column = 0, sticky = W, pady = 2)

lb13Name = Label(scrollable_frame, text = "a.Search for scrollable_frames and packages and seamlessly book \n a home sample collection.", font = ('comic sans ms', 14))
#lb13Name.place(relx=0.0, rely=1.40, anchor='w')
lb13Name.grid(row = 15, column = 0, sticky = W, pady = 2)

lb14Name = Label(scrollable_frame, text = "--------------------------", font = ('comic sans ms', 22, 'bold'))
#lb14Name.place(relx=0.0, rely=1.45, anchor='w')
lb14Name.grid(row = 16, column = 0, sticky = E, pady = 2)

lb15Name = Label(scrollable_frame, text = "b.We will send a certified professional to your place to \n to assist you with the sample collection ", font = ('comic sans ms', 14))
#lb15Name.place(relx=0.0, rely=1.55, anchor='w')
lb15Name.grid(row = 17, column = 0, sticky = W, pady = 2)

lb16Name = Label(scrollable_frame, text = "--------------------------", font = ('comic sans ms', 22, 'bold'))
#lb16Name.place(relx=0.0, rely=1.60, anchor='w')
lb16Name.grid(row = 18, column = 0, sticky = E, pady = 2)

lb17Name = Label(scrollable_frame, text = "c.We will email you the reports.You can also access your reports \n within your account on the Practo app", font = ('comic sans ms', 14))
#lb17Name.place(relx=0.0, rely=1.65, anchor='w')
lb17Name.grid(row = 19, column = 0, sticky = W, pady = 2)

lb18Name = Label(scrollable_frame, text = "We do great", font = ('comic sans ms', 16, 'bold'))
#lb18Name.place(relx=0.0, rely=1.70, anchor='w')
lb18Name.grid(row = 20, column = 0, sticky = W, pady = 2)

lb19Name = Label(scrollable_frame, text = "a.Millions of users every month", font = ('comic sans ms', 15))
#lb19Name.place(relx=0.0, rely=1.75, anchor='w')
lb19Name.grid(row = 21, column = 0, sticky = W, pady = 2)

lb20Name = Label(scrollable_frame, text = "b.Trusted by many healthcare professionals", font = ('comic sans ms', 15))
#lb20Name.place(relx=0.0, rely=1.80, anchor='w')
lb20Name.grid(row = 22, column = 0, sticky = W, pady = 2)

lb21Name = Label(scrollable_frame, text = "c.We serve in many cities", font = ('comic sans ms', 15))
#lb21Name.place(relx=0.0, rely=1.85, anchor='w')
lb21Name.grid(row = 23, column = 0, sticky = W, pady = 2)


scrollbar.pack( side = RIGHT, fill = Y )
canvas.pack()


log=Toplevel(root)
log.title("Login page")
log.geometry("500x400+300+100")
log.withdraw()

canvas2 = Canvas(log, width=500, height=400 , bg= "yellow")
#image20 = ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/dr.jpg"))
image20 = PhotoImage(file = r"log.png")
canvas2.create_image(0,0, anchor=NW, image=image20)
canvas2.pack()
image1 = image20.subsample(4,4)
# Label(log, image = image1).grid(row = 0, column = 0, columnspan = 1, rowspan = 1, padx = 2, pady = 2)
Label(log, image = image1).pack()

btn = Button(log,text="Login", bg= 'blue', fg = 'white', width="25", height = "2")
btn.place(x=160, y=100, anchor= 'nw')
#btn.grid(row = 1, column = 0, sticky = W, padx=0)

label_1 = Label(log, text="OR",width=10,bg= 'red', fg = 'yellow')
label_1.place(x=210,y=180)

btn1 = Button(log, text="Create New Account", bg= 'blue', fg= 'white', width="25", height = "2")
btn1.place(x=160, y=230, anchor= 'nw')

root.mainloop()