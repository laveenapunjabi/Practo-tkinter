from tkinter import *
from PIL import Image, ImageTk
import webbrowser

def next():
    current+=1
    if(current==len(frames)):
        current=0
        #frames[current].tkraise()

def Prev():
    current-=1
    if(current==len(frames)):
        current=3
        frames[current].tkraise()

def call_back():
    webbrowser.open_new(r"https://www.who.int/")




news = Tk()
news.geometry('650x750')
news.iconbitmap('')
news.title('Latest News')
l1 = Label(news, text = 'practo ', fg='blue',font = 'times 30 bold')
l1.pack()
l2 = Label(news, text='Precautions to be taken to amid \nCoronavirus outbreak!', font = "Helvetica 18 bold ")
l2.pack()

f1 = Frame(news, height=450, width=350)
f1.place(x=150, y=120)
f2 = Frame(news, height=450, width=350, bg='red')
f2.place(x=150, y=120)
f3 = Frame(news, height=450, width=350, bg='blue')
f3.place(x=150, y=120)
f4 = Frame(news, height=450, width=350, bg='green')
f4.place(x=150, y=120)
        
        

#Add frames here
frames = [f1,f2,f3,f4]
current=0

frames[current].tkraise()
        
raw_image = Image.open('img1.jpg')
        
raw_image = raw_image.resize((350, 450))
img1 = ImageTk.PhotoImage(raw_image)
l4 = Label(f1, image = img1)
l4.pack()

raw_image = Image.open('img2.jpg')
        
raw_image = raw_image.resize((350, 450))
img2 = ImageTk.PhotoImage(raw_image)
l5 = Label(f2, image = img2)
l5.pack()

raw_image = Image.open('img3.jpg')
raw_image = raw_image.resize((350, 450))
img3 = ImageTk.PhotoImage(raw_image)
l5 = Label(f3, image = img3)
l5.pack()

raw_image = Image.open('img4.jpg')
raw_image = raw_image.resize((350, 450))
img4 = ImageTk.PhotoImage(raw_image)
l5 = Label(f4, image = img4)
l5.pack()

        
l3=Label(news, height = 400, bg = 'yellow')
l3.pack(side=BOTTOM, fill = X)
b1 = Button(l3, bg = 'red', text = 'Learn More', font = 'times 18 bold',fg='white', relief = RIDGE, command=call_back)
b1.pack(pady=20)
b2 = Button(news, text='Next', bg = 'lightgrey', font = 'Helvetica 15 bold', width = 5, relief = RIDGE,command=next)
b2.place(x=500, y=600)
b3 = Button(news, text='Prev', bg = 'lightgrey', font = 'Helvetica 15 bold', width = 5, relief = RIDGE, command=Prev)
b3.place(x=100, y=600)



news.mainloop()