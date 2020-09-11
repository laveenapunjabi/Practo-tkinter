'''
from tkinter import *
from tkinter import ttk

import smtplib
import webbrowser

def sendemail():
    try:
        
        sender = account.get()
        recepient = [receiver.get()]
        sub = subject.get()
        pswrd = password.get()
        msg = msgbody.get('1.0','end')
        msgtosend = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (sender, recepient, sub, msg)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.starttls()
        mail.login(sender, pswrd)
        mail.sendmail(sender, recepient, msgtosend)
        mail.close()
        
        ttk.Label(mainframe, text="Email sent successfully").grid(column=4,row=9,sticky=W)

    except Exception as e:
        ttk.Label(mainframe, text=str(e)).grid(column=4,row=9,sticky=W)

def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")
    
        
root = Tk()
root.title("Send an Email via Gmail !!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

account = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
msgbody = StringVar()

a = Label(mainframe, text="To use this app turn this setting ON for your account", fg="blue", cursor="hand2")
a.grid(columnspan=2,column=3, row=0, sticky=W)
a.bind("<Button-1>", setup)


ttk.Label(mainframe, text="Your Email Account: ").grid(column=0, row=1, sticky=W)
account_entry = ttk.Entry(mainframe, width=30, textvariable=account)
account_entry.grid(column=4, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Your Password: ").grid(column=0, row=2, sticky=W)
password_entry = ttk.Entry(mainframe, show="*", width=30, textvariable=password)
password_entry.grid(column=4, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Recepient's Email Account: ").grid(column=0, row=3, sticky=W)
receiver_entry = ttk.Entry(mainframe, width=30, textvariable=receiver)
receiver_entry.grid(column=4, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Let's Compose").grid(column=2, row=5, sticky=W)

ttk.Label(mainframe, text="Subject: ").grid(column=0, row=6, sticky=W)
subject_entry = ttk.Entry(mainframe, width=30, textvariable=subject)
subject_entry.grid(column=4, row=6, sticky=(W, E))

ttk.Label(mainframe, text="Message Body: ").grid(column=0, row=7, sticky=W)
msgbody = Text(mainframe, width=30, height=10)
msgbody.grid(column=4, row=7, sticky=(W, E))

ttk.Button(mainframe, text="Send Email", command=sendemail).grid(column=4,row=8,sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

account_entry.focus()

root.mainloop()
'''

import smtplib

from smtplib import SMTPException
from tkinter import*

#this app sends email  via gmail
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





#Gui interface



mail= Toplevel()
root.config(bg="brown", )

#user mail
user_email = Label(root, text="Enter your Gmail address:  ")
user_email.pack()
user_email.config(bg="black", fg="white")

user_email = Entry(root, bd =8)
user_email.pack(fill=X)


#receiver email
receiver_email = Label(root, text="Enter the recipient's email address: ")
receiver_email.pack( )
receiver_email.config(bg="black", fg="white")


receiver_email = Entry(root, bd =8)
receiver_email.pack(fill=X)

#subject line
subj= Label(root, text="Enter your subject here: ")
subj.pack( )
subj.config(bg="black", fg="white")


subj = Entry(root, bd =8)
subj.pack(fill=X)







#Body of the message
body = Text(root, font="Tahoma",  relief=SUNKEN , bd=8)
body.config(bg="pink", height=15)
body.pack(fill=BOTH, expand=True)

#password widget
password = Label(root, text="Enter your Gmail password:  ")
password.pack()
password.config(bg="black", fg="white")

password= Entry(root, show='*', bd =8)
password.pack(fill=X)

#submit button
submit_mail = Button(root, bd =8, text="Click here to submit the mail",  
command=gmail)
submit_mail.pack(fill=X)

#feed back
text = Text(root, font="Tahoma",  relief=SUNKEN , bd=8)
text.config(bg="pink",  height=2)
text.pack(fill=BOTH, expand=True)



root.mainloop()

