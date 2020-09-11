from tkinter import *
from tkinter import messagebox as ms
import sqlite3


with sqlite3.connect('laveena.db') as db:
    cursor = db.cursor()

'''

q1 = ('create table patient(name text NOT NULL, email Varchar(20),gender varchar(1),phn_no int primary key,age int,bloodgroup varchar(5),usename varchar(20),password  varchar(20))' )

q2 = ( 'create table doctor(id int primary key, name varchar(20),specialist varchar(20))' );

q3 = ('create table lab_test(Lid int primary key,Lname varchar(20), cost int)');

q4 = ('create table Medicine(M_id int primary key,M_type varchar(20),M_name varchar(20),cost int)');


q5 = ('create table lab_appointment (la_id int primary key, phone_no int,  FOREIGN KEY(phone_no) REFERENCES patient(phn_no) , FOREIGN KEY(la_id) REFERENCES lab_test(Lid))');


q6 = ('create table MEdicine_booking(mid int primary key, phone_no int,  FOREIGN KEY(phone_no) REFERENCES patient(phn_no),FOREIGN KEY(mid) REFERENCES Medicine(M_id))');


q7 = ('create table appointment(id int primary key, phone_no int,  FOREIGN KEY(phone_no) REFERENCES patient(phn_no),FOREIGN KEY(id) REFERENCES doctor(id))');

q8 =('ALTER TABLE patient ADD Lab_appointment int,FOREIGN KEY(Lab_appointment) REFERENCES lab_test(lid);)')
'''

q1 = ('insert  into Appointment1(id,docName,patientName) values(1,"Shubashree","lavi" )');
cursor.execute(q1)

q2 = ('insert  into buy(Pid,planName,patientName) values(2,"popular","lavi" )');
cursor.execute(q2)

q3 = ('insert  into Appointment1(id,docName,patientName) values(6,"Smita","lavi" )');
cursor.execute(q3)

q4 = ('insert  into LabTest(Lid,testName,patientName) values(1,"HbA1c","lavi" )');
cursor.execute(q4)

q5 = ('insert  into LabTest(Lid,testName,patientName) values(7,"Liver Function","lavi" )');
cursor.execute(q5)

q6 = ('insert  into Medicines(Mid,medName,patientName) values(3,"Levosiz","lavi" )');
cursor.execute(q6)

q7 = ('insert  into Medicines(Mid,medName,patientName) values(8,"omez","lavi" )');
cursor.execute(q7)

q8 = ('insert  into Medicines(Mid,medName,patientName) values(14,"Herapin","lavi" )');
cursor.execute(q8)


db.commit()
db.close()