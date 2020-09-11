from tkinter import *
log = Tk()
log.title("Login page")
log.geometry("500x400+300+100")


canvas = Canvas(log, width=500, height=400 , bg= "yellow")
#image20 = ImageTk.PhotoImage(Image.open("C:/Users/HP/Desktop/dr.jpg"))
image20 = PhotoImage(file = r"log.png")
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()
image1 = image20.subsample(4,4)
Label(log, image = image1).pack()

btn = Button(log,text="Login", bg= 'blue', fg = 'white', width="25", height = "2")
btn.place(x=160, y=100, anchor= 'nw')
#btn.grid(row = 1, column = 0, sticky = W, padx=0)

label_1 = Label(log, text="OR",width=10,bg= 'red', fg = 'yellow')
label_1.place(x=210,y=180)

btn1 = Button(log, text="Create New Account", bg= 'blue', fg= 'white', width="25", height = "2")
btn1.place(x=160, y=230, anchor= 'nw')

log.mainloop()