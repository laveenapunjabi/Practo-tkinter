from tkinter import *
import requests
import simplejson as json
import math
import random 

def f3():
	mi.withdraw()
	otp_valid.deiconify()


mi=Tk()
mi.geometry("300x200+50+60")
mi.title("OTP")
mi.configure(background="red")
label1=Label(mi,text="Enter your Mobile Number ",font=("Bell MT",15,"bold"),bg="Yellow",fg='Black',bd=5)
label1.place(x=10,y=10)


def f1():
	URL = 'https://www.sms4india.com/api/v1/sendCampaign'
	no=entry1.get()
	# get request
	def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
		req_params = {
		'apikey':apiKey,
		'secret':secretKey,
		'usetype':useType,
		'phone': phoneNo,
		'message':textMessage,
		'senderid':senderId
		}
		return requests.post(reqUrl, req_params)
	data="0123456789"
	leng=len(data)
	otp=""
		
	for i in range(6):
		otp +=data[math.floor(random.random()*leng)]
	# get response
	response = sendPostRequest(URL, 'HFQXBXPGQINU22J7GG77SMH4Q6QRTQT5', '1BQADUWCUIIQH9Z9', 'stage', no , 'Ramesh', 'your 6-digit otp is'+str(otp) )
	"""
	  Note:-
	    you must provide apikey, secretkey, usetype, mobile, senderid and message values
	    and then requst to api
	"""
	# print response if you want
	#print response.text
	#view rawsmsind_python_sendcampaign_post.py hosted with ❤ by GitHub'''


entry1=Entry(mi,bd=5,font=("arial",18,"bold"))
entry1.place(x=10,y=60)


btn1=Button(mi,text="Get OTP",font=("Inter",18,"bold"),bg="Black",fg="Yellow",bd=8,command=f1, command =f3)
btn1.place(x=50,y=120)

otp_valid = Toplevel(root)
otp_valid.geometry("500x400+300+100")
otp_valid.withdraw()

label1 = Label(otp_valid, text = "validation ",width=10 )
label1.pack()

btn1 = Button(otp_valid, text ="verified", width=10)
btn1.pack()

i=input(int(""






mi.mainloop()