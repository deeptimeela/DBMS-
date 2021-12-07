from tkinter import *

import mysql.connector
import os
from time import sleep 


	
mydb = mysql.connector.connect(
  user="newuser",
  password="password",
  database="HMS"
)
if(mydb.is_connected()):
	print("connected")
c = mydb.cursor()

def get_doctor_id():
	query = "select id from Doctor;"
	c.execute(query)
	a = c.fetchall()
	for i in a:
		pass
	return i[0]+1 
	
def get_patient_id():
	query = "select id from Patient;"
	c.execute(query)
	a = c.fetchall()
	for i in a:
		pass
	return i[0]+1 

def get_data():
	query = "select * from Doctor;"
	c.execute(query)
	a = c.fetchall()
	for i in a:
		print(i)
def get_data_p():
	query = "select * from Patient;"
	c.execute(query)
	a = c.fetchall()
	for i in a:
		print(i)

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()
      

	

	
	


def login_doc_submit():
	d_id = doc_login_id.get()
	f=0 
	query = "select * from Doctor where id = " + str(d_id) + ";"
	c.execute(query)
	a = c.fetchall()
	if(len(a) == 0):
		print("WRONG ID")
		f=1 
		temp = "WRONG ID. QUITTING NOW" 
		label.config(text = temp, fg = "white",bg = "black",font = ("Times New Roman", 20, "bold")) 
		
	else:
		s = a[0] 
		your_id = s[0]
		your_email =  s[1]
		your_gender = s[2]
		your_password = s[3]
		your_name = s[4]
	def p_details():
		query1 = "select name from Patient where id in (select patient from PatientsFillHistory where history in (select history from DoctorViewsHistory where doctor = " + str(your_id) + "));" 
		print(query1) 
		c.execute(query1) 
		p_name = c.fetchall()
		print(p_name)
		
		
		
		query2 = "select concerns, symptoms from PatientsAttendAppointments where patient in (select patient from PatientsFillHistory where history in (select history from DoctorViewsHistory where doctor =" + str(your_id) + "))"; 
		c.execute(query2) 
		p_condition = c.fetchall()
		print(p_condition) 
		
		
		query3 = "select date, conditions, surgeries, medication from MedicalHistory where id in (select history from DoctorViewsHistory where doctor =" + str(your_id) + ");"
		c.execute(query3)
		p_history = c.fetchall()
		print(p_history)
		clear_frame()
		
		font_tuple = ("Times New Roman", 20, "bold")
		text = "YOUR PATIENT DETAILS" 
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 5,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		for i in range (len(p_name)) :
			
		
			text = "NAME: " + str(p_name[i][0]) 
			font_tuple = ("Times New Roman", 14)
			Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 5,font = font_tuple, fg = "white",bg = "#000000").pack()
			
			text = "PROBLEM:  " + p_condition[i][0] + "," + p_condition[i][1] 
			font_tuple = ("Times New Roman", 14)
			Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 5,font = font_tuple, fg = "white",bg = "#000000").pack()
			
			text = "MEDICAL HISTORY:"
			font_tuple = ("Times New Roman", 14)
			Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 5,font = font_tuple, fg = "white",bg = "#000000").pack()
			
			text = "DATE: " + str(p_history[i][0])
			font_tuple = ("Times New Roman", 14)
			Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 5,font = font_tuple, fg = "white",bg = "#000000").pack()
			
			text = "CONDITIONS: " + str(p_history[i][1])
			font_tuple = ("Times New Roman", 14)
			Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 5,font = font_tuple, fg = "white",bg = "#000000").pack()
			
			text = "MEDICATIONS: " + str(p_history[i][2])
			font_tuple = ("Times New Roman", 14)
			Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 5,font = font_tuple, fg = "white",bg = "#000000").pack()
			
			text = "********************************************************************"
			Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 5,font = font_tuple,fg = "white",bg = "#000000").pack()
					
	def schedule(): 
		query = 'select starttime, endtime, breaktime, day from Schedule where id in (select sched from DocsHaveSchedules where doctor = ' + str(your_id) + ')'  
		c.execute(query)
		a = c.fetchall()
		s = a[0] 
		print(str(s[0]))
		clear_frame() 
		
		font_tuple = ("Times New Roman", 20, "bold")
		text = "YOUR SCHEDULE, " + your_name
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		text = "Start time: " + str(s[0]) 
		font_tuple = ("Times New Roman", 18)
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		text = "End time: " + str(s[1]) 
		font_tuple = ("Times New Roman", 18)
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		text = "Break time: " + str(s[2]) 
		font_tuple = ("Times New Roman", 18)
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		text = "Day: " + str(s[3]) 
		font_tuple = ("Times New Roman", 18)
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		space = Label(frame, text = "", bg = "black" , pady = 30 )
		sub_btn=Button(frame,text = 'PATIENT DETAILS', command = p_details, bg = "green", fg="white").pack()
		
		
		
		
		
		
		
		
		
	clear_frame()		
	font_tuple = ("Times New Roman", 20, "bold")
	text = "HELLO, " + your_name 
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	text = "YOUR PERSONAL INFORMATION" 
	font_tuple = ("Times New Roman", 18, "bold")
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "ID: " + str(your_id) 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "EMAIL: " + your_email 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "GENDER: " + your_gender 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "PASSWORD: " + your_password 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "NAME: " + your_name 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	space = Label(frame, text = "", bg = "black" , pady = 30 )
	sub_btn=Button(frame,text = 'YOUR SCHEDULE', command = schedule, bg = "green", fg="white").pack()
	
	
      
def login_doctor():
	print("doctor ka login")
	clear_frame()
	font_tuple = ("Times New Roman", 20, "bold")
	Label (frame, text="WELCOME BACK DOCTOR" ,justify = CENTER,padx = 10 ,pady = 40,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	#id ENTRY 
	login_id_label = Label(frame, text = 'Please enter your ID ', font=('Times New Roman',18, 'bold') , fg= "white" ,bg = "black",pady = 20).pack()
	login_id_entry = Entry(frame,textvariable = doc_login_id, font=('calibre',14,'normal'),bg = "white", fg = "black").pack()
	
	#SUBMIT
	space = Label(frame, text = "", bg = "black" , pady = 10 )
	sub_btn=Button(frame,text = 'SUBMIT', command = login_doc_submit, bg = "green", fg="white").pack()
	
	
	
def login_p_submit():
	p_id = p_login_id.get()
	query = 'select * from Patient where id = ' + str(p_id); 
	c.execute(query)
	a = c.fetchall()
	if(len(a) == 0):
		print("WRONG ID")
		f=1 
		temp = "WRONG ID. QUITTING NOW" 
		label.config(text = temp, fg = "white",bg = "black",font = ("Times New Roman", 20, "bold")) 
	else:
		s = a[0]
		your_id = s[0]
		your_email = s[1] 
		your_password = s[2] 
		your_name = s[3] 
		your_address = s[4] 
		your_gender = s[5] 
	def next():
		clear_frame()
		query1 = "select name from Doctor where id in (select doctor from DoctorViewsHistory where history in  (select history from PatientsFillHistory where patient = " + str(your_id) + "));"
		c.execute(query1) 
		docname = c.fetchall()
		print(docname[0][0])
		
		query2 = "select starttime, endtime, status from Appointment where id in (select appt from PatientsAttendAppointments where patient = " + str(your_id) + ");"  
		c.execute(query2) 
		appt = c.fetchall()
		print(appt) 
		
		font_tuple = ("Times New Roman", 25, "bold")
		text = "YOUR APPOINTMENT DETAILS" 
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		text = "DOCTOR ATTENDING YOU: " + str(docname[0][0]) 
		font_tuple = ("Times New Roman", 20)
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		text = "START TIME: " + str(appt[0][0]) 
		font_tuple = ("Times New Roman", 20)
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		text = "END TIME: " + str(appt[0][1]) 
		font_tuple = ("Times New Roman", 20)
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
		
		text = "STATUS: " + str(appt[0][2]) 
		font_tuple = ("Times New Roman", 20)
		Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	clear_frame()		
	font_tuple = ("Times New Roman", 20, "bold")
	text = "HELLO, " + your_name 
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	text = "YOUR PERSONAL INFORMATION" 
	font_tuple = ("Times New Roman", 18, "bold")
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "ID: " + str(your_id) 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "EMAIL: " + your_email 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "GENDER: " + your_gender 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "ADDRESS: " + your_address 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "PASSWORD: " + your_password 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	text = "NAME: " + your_name 
	font_tuple = ("Times New Roman", 18)
	Label (frame, text=text ,justify = CENTER,padx = 10 ,pady = 10,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	space = Label(frame, text = "", bg = "black" , pady = 30 )
	sub_btn=Button(frame,text = 'next', command = next, bg = "green", fg="white").pack()	
		
def login_patient():
	clear_frame()
	font_tuple = ("Times New Roman", 20, "bold")
	Label (frame, text="WELCOME BACK !" ,justify = CENTER,padx = 10 ,pady = 40,font = font_tuple, fg = "white",bg = "#000000").pack()
	
	#id ENTRY 
	login_id_label = Label(frame, text = 'Please enter your ID ', font=('Times New Roman',18, 'bold') , fg= "white" ,bg = "black",pady = 20).pack()
	login_id_entry = Entry(frame,textvariable = p_login_id, font=('calibre',14,'normal'),bg = "white", fg = "black").pack()
	
	#SUBMIT
	space = Label(frame, text = "", bg = "black" , pady = 10 )
	sub_btn=Button(frame,text = 'SUBMIT', command = login_p_submit, bg = "green", fg="white").pack()
	
def p_reg_submit():
	p_id = get_patient_id() 
	email = p_reg_email.get()
	gender = p_reg_gender.get()
	password = p_reg_password.get()
	name = p_reg_name.get()
	address = p_reg_address.get()
	values =str(p_id) + ", '" + email + "' , '" +  password + "' , '" +  name + "' , '" +  address + "' , '" +  gender + "'" 
	query = "insert into Patient values ( " +  values + " )"  + ";" 
	p_reg_email.set("")
	p_reg_gender.set("")
	p_reg_password.set("")
	p_reg_name.set("")
	p_reg_address.set("") 
	print(query)
	c.execute(query) 
	value_id = "PLEASE REMEMBER YOUR ID. YOUR ID IS   " + str(p_id)
	label.config(text = value_id, fg = "white" ,bg = "black") 
	#space = Label(frame, text = "", bg = "black" , pady = 10 )
	#sub_btn=Button(root,text = 'ENTER MEDICAL HISTORY', command = doc_reg_submit, bg = "green", fg="white",font=("Times New Roman",14)).pack()
	
	
	get_data_p()
	
def doc_reg_submit():
	d_id = get_doctor_id() 
	email = doc_reg_email.get()
	gender = doc_reg_gender.get()
	password = doc_reg_password.get()
	name = doc_reg_name.get()
	values =str(d_id) + ", '" + email + "' , '" +  gender + "' , '" +  password + "' , '" +  name + "'" 
	query = "insert into Doctor values ( " +  values + " )"  + ";" 
	doc_reg_email.set("")
	doc_reg_gender.set("")
	doc_reg_password.set("")
	doc_reg_name.set("")
	print(query)
	c.execute(query) 
	value_id = "PLEASE REMEMBER YOUR ID. YOUR ID IS   " + str(d_id)
	label.config(text = value_id, fg = "white" ,bg = "black") 
	
	
	get_data()
	
	
def register_doctor():
	print("doctor ka register")
	clear_frame() 
	font_tuple = ("Times New Roman", 18, "bold")
	Label (frame, text="WE ARE GLAD TO HAVE YOU HERE" ,justify = CENTER,padx = 10 ,pady = 40,font = font_tuple, fg = "white",bg = "#000000").pack()
	#EMAIL
	email_label = Label(frame, text = 'Email', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = doc_reg_email, font=('calibre',14,'normal'),bg = "white", fg = "black").pack()
	
	#GENDER
	email_label = Label(frame, text = 'GENDER', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = doc_reg_gender, font=('calibre',14,'normal'),bg = "white",fg = "black" ).pack()
	
	#PASSWORD
	email_label = Label(frame, text = 'PASSWORD', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = doc_reg_password, font=('calibre',14,'normal'),bg = "white",fg = "black" ).pack()
	
	#NAME
	email_label = Label(frame, text = 'NAME', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = doc_reg_name, font=('calibre',14,'normal'),bg = "white",fg = "black" ).pack()
	
	#SUBMIT
	space = Label(frame, text = "", bg = "black" , pady = 10 )
	sub_btn=Button(root,text = 'SUBMIT', command = doc_reg_submit, bg = "green", fg="white",font=("Times New Roman",14)).pack()
	
def register_patient():
	clear_frame()
	font_tuple = ("Times New Roman", 18, "bold")
	Label (frame, text="WELCOME " ,justify = CENTER,padx = 10 ,pady = 20,font = font_tuple, fg = "white",bg = "#000000").pack()
	#EMAIL
	email_label = Label(frame, text = 'Email', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = p_reg_email, font=('calibre',14,'normal'),bg = "white", fg = "black").pack()
	
	#GENDER
	email_label = Label(frame, text = 'GENDER', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = p_reg_gender, font=('calibre',14,'normal'),bg = "white",fg = "black" ).pack()
	
	#PASSWORD
	email_label = Label(frame, text = 'PASSWORD', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = p_reg_password, font=('calibre',14,'normal'),bg = "white",fg = "black" ).pack()
	
	#NAME
	email_label = Label(frame, text = 'NAME', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = p_reg_name, font=('calibre',14,'normal'),bg = "white",fg = "black" ).pack()
	
	#ADDRESS
	email_label = Label(frame, text = 'ADDRESS', font=('Times New Roman',14, 'bold') , fg= "white" ,bg = "black",pady = 10).pack()
	email_entry = Entry(frame,textvariable = p_reg_address, font=('calibre',14,'normal'),bg = "white",fg = "black" ).pack()
	
	#SUBMIT
	space = Label(frame, text = "", bg = "black" , pady = 10 )
	sub_btn=Button(root,text = 'SUBMIT', command = p_reg_submit, bg = "green", fg="white",font=("Times New Roman",14)).pack()
	
	
	
	
def patient():
	print("doctor")
	clear_frame()	
	Label(frame, text="WELCOME" ,justify = CENTER,padx = 20,pady = 50,font = font_tuple, fg = "white",bg = "#000000").pack()
	login_doc = Radiobutton(frame, text="PATIENT LOGIN", variable=var, value=1,command=login_patient,font = font_tuple_radio,padx = 450,pady = 25,indicatoron = 0) 
	login_doc.pack( anchor = W )
	reg_doc = Radiobutton(frame, text="PATIENT REGISTER", variable=var, value=2,command=register_patient,font = font_tuple_radio,padx = 450,pady = 25,indicatoron = 0)
	reg_doc.pack( anchor = W )


def doctor():
	print("doctor")
	clear_frame()	
	Label(frame, text="WELCOME DOCTOR " ,justify = CENTER,padx = 20,pady = 50,font = font_tuple, fg = "white",bg = "#000000").pack()
	login_doc = Radiobutton(frame, text="DOCTOR LOGIN", variable=var, value=1,command=login_doctor,font = font_tuple_radio,padx = 450,pady = 25,indicatoron = 0) 
	login_doc.pack( anchor = W )
	reg_doc = Radiobutton(frame, text="DOCTOR REGISTER", variable=var, value=2,command=register_doctor,font = font_tuple_radio,padx = 450,pady = 25,indicatoron = 0)
	reg_doc.pack( anchor = W )
	
	


def sel():
   selection = "You selected the option " + str(var.get())
   if (str(var.get()) == "1"):
   	doctor()
   else:
   	patient()



root = Tk()
root.geometry("1000x500")
root.configure(bg='black')
frame = Frame(root,bg = 'black') 
frame.pack()

doc_reg_email = StringVar()
doc_reg_gender = StringVar()
doc_reg_password = StringVar()
doc_reg_name = StringVar()
doc_login_id = IntVar()
p_login_id = IntVar()

p_reg_email = StringVar()
p_reg_gender = StringVar()
p_reg_password = StringVar()
p_reg_name = StringVar()
p_reg_address = StringVar()
doc_login_id = IntVar()





font_tuple = ("Times New Roman", 50, "bold")
Label(frame, text="WELCOME, WHO ARE YOU? " ,justify = CENTER,padx = 20,pady = 50,font = font_tuple, fg = "white",bg = "#000000").pack()
var = IntVar()
font_tuple_radio = ("Times New Roman",30)
R1 = Radiobutton(frame, text="DOCTOR", variable=var, value=1,command=sel,font = font_tuple_radio,padx = 450,pady = 25 ,indicatoron = 0,bg = "#ADD8E6")
R1.pack( anchor = W )
R2 = Radiobutton(frame, text="PATIENT", variable=var, value=2,command=sel,font = font_tuple_radio,padx = 450,pady = 25 , indicatoron =0,bg = "#90ee90")
R2.pack( anchor = W )
label = Label(root)
label.pack()
root.mainloop()


