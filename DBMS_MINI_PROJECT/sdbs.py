from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

root=Tk()
root.title("SMS")
root.geometry('600x400+400+150')

frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack(side=TOP,fill=X)  # side='top' is default
frame2.pack(side='top',fill=X)

def f1():
	#global sonal
	#if sonal==True:
		print("hello")
		root.withdraw()
		addEmp.deiconify()
		entEid.focus()
		print(addEmp.deiconify())
		
		print("yes")
		print("helo")
		#collectEid=addEmp.register(checkEid)
		#entEid.config(validate="key",validatecommand=(collectEid,'%P'))
		
	


def entEidOp():
	if  (eid.isdigit()):
		messagebox.showerror("ValueError","Please Enter Positive Number") 
		entEid.delete(0,END)	
		entEid.focus()
	else :
		entEname.focus()
		

def btnViewOp():
	import cx_Oracle
	con=None
	cursor=None

	try:
		con=cx_Oracle.connect("system/abc123")
		print("U R Connected")
		cursor=con.cursor()
		sql='select eid,ename,emarks from sms'
		cursor.execute(sql)
		data=cursor.fetchall()
		mdata='' ''
		for d in data:
			mdata=mdata+str(d[0])+" "+d[1]+ " "+str(d[2])+"\n"
		st.insert(INSERT,mdata)
	except cx_OracleDatabaseError as e:
		print("Issue :",e )
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
	viewEmp.deiconify()
	root.withdraw()

def btnUpdateOp():
	root.withdraw()
	updateEmp.deiconify()
	entEid2.focus()

def btnDeleteOp():
	deleteEmp.deiconify()
	root.withdraw()
	entEid3.focus()

def btnGraphOp():
	graphEmp.deiconify()
	root.withdraw()


#sonal=True
btnAdd=Button(frame1,text="Add",width=20,command=f1)
btnView=Button(frame1,text="View",width=20,command=btnViewOp)
btnUpdate=Button(frame1,text="Update",width=20, command=btnUpdateOp)
btnDelete=Button(frame1,text="Delete",width=20, command=btnDeleteOp)
btnGraph=Button(frame1,text="Graph",width=20,command=btnGraphOp)
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)

import socket
import requests
try:
	city="Mumbai"
	socket.create_connection(("www.google.com",80))
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address=a1+a2+a3
	res1=requests.get(api_address)
	j1=res1.json()
	d1=j1['main']
	temp=d1['temp']
	lblTemp=Label(frame1,text="Temperature = ")
	lblTemp.pack(side=LEFT)
	#lblTemp.grid(row=30,column=0)
	lblTempAns=Label(frame1,text=temp)
	lblTempAns.pack(side=LEFT)
	#lblTempAns.grid(row=30,column=1)
except OSError:
	print("Check network")

import random

msg=["Love not Hate","Laughter is bets medicine","Never stop looking up","Vow to stop worring and start learning"]
r=random.randrange(len(msg))

quote=Label(frame2,text="Quote = ")
quote.pack(side=LEFT,pady=10)
quotemsg=Label(frame2,text=msg[r])
quotemsg.pack(side=LEFT)

addEmp=Toplevel(root)
addEmp.title("Add S")
addEmp.geometry('600x400+400+150')
addEmp.withdraw()
lblEid=Label(addEmp,text='Enter Roll no.')
lblEid.pack(pady=10)
def checkEid(empeid):
	if empeid.isdigit():
		print(empeid)
		return True
	elif empeid is "" :
		print(empeid)
		return True
	else :
		print(empeid)
		messagebox.showerror("ValueError","You Entered :"+" "+str(empeid)+"\n"+"Please Enter Integer")
		entEid.config(validate="none")
		entEid.delete(0,END)
		entEid.config(validate="key")
		entEid.focus()
		return False	
entEid=Entry(addEmp,bd=5)
entEid.focus()
entEid.pack(pady=10)
collectEid1=addEmp.register(checkEid)
entEid.config(validate="key",validatecommand=(collectEid1,'%P'))

def checkEname(empename):
	whatineid=entEid.get()
	if whatineid=="":
		messagebox.showerror("Empty","Student id Should not be Empty")
		entEid.focus()
		return False
	elif empename.isalpha() :
		print(empename)
		return True
	elif empename is "" :
		print(empename)
		return True
	else :
		print(empename)
		messagebox.showerror("ValueError","You Entered :"+" "+empename+"\n"+"Please Enter String")
		entEname.config(validate="none")
		entEname.delete(0,END)
		entEname.config(validate="key")
		entEname.focus()
		return False
	
	
			
			
	
lblEname=Label(addEmp,text="Enter Name")
entEname=Entry(addEmp,bd=5)
collectEname=addEmp.register(checkEname)
entEname.config(validate="key",validatecommand=(collectEname,'%P'))

def checkMarks(empmarks):
	lenEname=entEname.get()
	try:
		em=int(empmarks)
	except ValueError:
		print()
	if len(lenEname)<2:	
		messagebox.showerror("Length","Length of Student Name is less than 2")
		entEname.focus()
		return False
	
	elif empmarks.isdigit() and (em>=0 and em<=100) :
		print(empmarks)
		return True
	elif empmarks is "" :
		print(empmarks)
		return True
	else :

		print(empmarks)
		messagebox.showerror("ValueError","You Entered :"+" "+str(empmarks)+"\n"+"Please Enter Digits Between 0-100")
		entMarks.config(validate="none")
		entMarks.delete(0,END)
		entMarks.config(validate="key")
		entMarks.focus()
		return False	

	
	
	
lblMarks=Label(addEmp,text="Enter Marks")
entMarks=Entry(addEmp,bd=5)
collectMarks=addEmp.register(checkMarks)
entMarks.config(validate="key",validatecommand=(collectMarks,"%P"))

lblEname.pack(pady=10)
entEname.pack(pady=10)
lblMarks.pack(pady=10)
entMarks.pack(pady=10)
	
def SaveOp():
	import cx_Oracle
	con=None
	cursor=None
	
	try:
			
		con=cx_Oracle.connect("system/abc123")
		print("U R Connectd")
		cursor=con.cursor()
		sql="insert into sms values('%d','%s','%d')"	
		try:	
			eid1= int(entEid.get())
		except ValueError:
			messagebox.showerror("Empty","Student id Field is Empty")
			entEid.focus()
		try:		
			ename1=entEname.get()
		except ValueError:
			messagebox.showerror("Empty","Student name Field is Empty")
		try:	
			emarks1=int(entMarks.get())
		except ValueError:
			messagebox.showerror("Empty","Student marks Field is Empty")
			entMarks.focus()
		args=(eid1,ename1,emarks1)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"Records Inserted"
		messagebox.showinfo("Success", msg)
		entEid.config(validate="none")
		entEid.delete(0,END)
		entEid.config(validate="key")
		entEname.config(validate="none")
		entMarks.config(validate='none')	
		entEname.delete(0,END)
		entEname.config(validate="key")		
		entMarks.config(validate='key')
		entMarks.config(validate="none")		
		entMarks.delete(0,END)
		entMarks.config(validate="key")
		entEid.focus()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure","There are 2 possibilities :"+"\n"+"please Correct it "+"\n"+"Student id is already exist or Student name Field is empty")
		entEname.focus()
	except UnboundLocalError as e:
		print()
		#messagebox.showerror("Failure",e)
	except cx_Oracle.IntegrityError as e:
		messagebox.showerror("Failure","Student name Field is empty")		
	
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def addBackOp():
	entEid.config(validate="none")
	entEid.delete(0,END)
	entEid.config(validate="key")
	entEname.config(validate="none")
	entEname.delete(0,END)
	entEname.config(validate="key")
	entMarks.config(validate="none")
	entMarks.delete(0,END)
	entMarks.config(validate="key")
	root.deiconify()
	addEmp.withdraw()
		

btnSave=Button(addEmp,text='Save',command=SaveOp)
btnBack=Button(addEmp,text='Back', command=addBackOp)

btnSave.pack(pady=10)
btnBack.pack(pady=10)

viewEmp=Toplevel(root)
viewEmp.title("View S")
viewEmp.geometry('600x400+400+150')
viewEmp.withdraw()



def viewBackOp():
	st.delete('1.0',END)
	viewEmp.withdraw()
	root.deiconify()

st=scrolledtext.ScrolledText(viewEmp,width=30,height=5)
btnViewBack=Button(viewEmp,text="Back",command=viewBackOp)

st.pack(pady=10)
btnViewBack.pack(pady=10)

updateEmp=Toplevel(root)
updateEmp.title("Update S")
updateEmp.geometry('600x400+400+150')
updateEmp.withdraw()
lblEid2=Label(updateEmp,text='Enter Roll no.')
lblEid2.pack(pady=10)
def checkEid2(empeid2):
	if empeid2.isdigit():
		print(empeid2)
		return True
	elif empeid2 is "" :
		print(empeid2)
		return True
	else :
		print(empeid2)
		messagebox.showerror("ValueError","You Entered :"+" "+str(empeid2)+"\n"+"Please Enter String")
		entEid2.config(validate="none")
		entEid2.delete(0,END)
		entEid2.config(validate="key")
		entEid2.focus()
		return False	
entEid2=Entry(updateEmp,bd=5)
entEid2.focus()
entEid2.pack(pady=10)
collectEid2=updateEmp.register(checkEid2)
entEid2.config(validate="key",validatecommand=(collectEid2,'%P'))

def checkEname2(empename2):
	whatineid=entEid2.get()
	if whatineid=="":
		messagebox.showerror("Empty","Student id Should not be Empty")
		entEid2.focus()
		return False
	elif empename2.isalpha() :
		print(empename2)
		return True
	elif empename2 is "" :
		print(empename2)
		return True
	else :
		print(empename2)
		messagebox.showerror("ValueError","You Entered :"+" "+empename2+"\n"+"Please Enter String")
		entEname2.config(validate="none")
		entEname2.delete(0,END)
		entEname2.config(validate="key")
		entEname2.focus()
		return False
	
	
			
			
	
lblEname2=Label(updateEmp,text="Enter Name")
entEname2=Entry(updateEmp,bd=5)
collectEname2=updateEmp.register(checkEname2)
entEname2.config(validate="key",validatecommand=(collectEname2,'%P'))

def checkMarks2(empmarks2):
	lenEname2=entEname2.get()
	try:
		em2=int(empmarks2)
	except ValueError:
		print()
	if len(lenEname2)<2:	
		messagebox.showerror("Length","Length of Student Name is less than 2")
		entEname2.focus()
		return False
	
	elif empmarks2.isdigit() and (em2>=0 and em2<=100) :
		print(empmarks2)
		return True
	elif empmarks2 is "" :
		print(empmarks2)
		return True
	else :

		print(empmarks2)
		messagebox.showerror("ValueError","You Entered :"+" "+str(empmarks2)+"\n"+"Please Enter Digits Between 0-100")
		entMarks2.config(validate="none")
		entMarks2.delete(0,END)
		entMarks2.config(validate="key")
		entMarks2.focus()
		return False	

	
	
	
lblMarks2=Label(updateEmp,text="Enter Marks")
entMarks2=Entry(updateEmp,bd=5)
collectMarks2=updateEmp.register(checkMarks2)
entMarks2.config(validate="key",validatecommand=(collectMarks2,"%P"))

lblEname2.pack(pady=10)
entEname2.pack(pady=10)
lblMarks2.pack(pady=10)
entMarks2.pack(pady=10)
	
def updateSaveOp():
	import cx_Oracle
	con=None
	cursor=None
	
	try:
		con=cx_Oracle.connect("system/abc123")
		print("U R Connectd")
		cursor=con.cursor()
		sql="update sms set ename='%s' , emarks='%d' where eid='%d' "
		
		try:
			eid=int(entEid2.get())
		except ValueError:
			messagebox.showerror("Empty","Student id Field is Empty")
			entEid2.focus()
		ename=entEname2.get()
		try:
			emarks=int(entMarks2.get())
		except ValueError:
			messagebox.showerror("Empty","Student marks Field is Empty")
			entMarks2.focus()
		args=(ename,emarks,eid)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"Records Updated"
		messagebox.showinfo("Success", msg)
		entEid2.config(validate="none")
		entEid2.delete(0,END)
		entEid2.config(validate="key")
		entEname2.config(validate="none")
		entMarks2.config(validate='none')
		entEname2.delete(0,END)
		entEname2.config(validate="key")
		entMarks2.config(validate='key')	
		entMarks2.config(validate="none")
		entMarks2.delete(0,END)
		entMarks2.config(validate="key")
		entEid2.focus()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure","Student name Field is Empty")
		entEname2.focus()
	except UnboundLocalError as e:
		print()
		#messagebox.showerror("Failure",e)
		
	
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def updateBackOp():
	entEid2.config(validate="none")
	entEid2.delete(0,END)
	entEid2.config(validate="key")
	entEname2.config(validate="none")
	entMarks2.config(validate='none')
	entEname2.delete(0,END)
	entEname2.config(validate="key")
	entMarks2.config(validate='key')
	entMarks2.config(validate="none")
	entMarks2.delete(0,END)
	entMarks2.config(validate="key")
	root.deiconify()
	updateEmp.withdraw()
		

btnSave2=Button(updateEmp,text='Save',command=updateSaveOp)
btnBack2=Button(updateEmp,text='Back', command=updateBackOp)

btnSave2.pack(pady=10)
btnBack2.pack(pady=10)

deleteEmp=Toplevel(root)
deleteEmp.title("Delete S")
deleteEmp.geometry('600x400+400+150')
deleteEmp.withdraw()
lblEid3=Label(deleteEmp,text='Enter Roll no.')
lblEid3.pack(pady=10)
def checkEid3(empeid3):
	if empeid3.isdigit():
		print(empeid3)
		return True
	elif empeid3 is "" :
		print(empeid3)
		return True
	else :
		print(empeid3)
		messagebox.showerror("ValueError","You Entered :"+" "+str(empeid3)+"\n"+"Please Enter String")
		entEid3.config(validate="none")
		entEid3.delete(0,END)
		entEid3.config(validate="key")
		entEid3.focus()
		return False	
entEid3=Entry(deleteEmp,bd=5)
entEid3.focus()
entEid3.pack(pady=10)
collectEid3=updateEmp.register(checkEid3)
entEid3.config(validate="key",validatecommand=(collectEid3,'%P'))


def deleteSaveOp():
	import cx_Oracle
	con=None
	cursor=None
	
	try:
		con=cx_Oracle.connect("system/abc123")
		print("U R Connectd")
		cursor=con.cursor()
		sql="delete from sms where eid='%d' "
		
		try:
			eid=int(entEid3.get())
		except ValueError:
			messagebox.showerror("Empty","Student id Field is Empty")
			entEid3.focus()
			
		args=(eid)
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"Records Deleted"
		messagebox.showinfo("Success", msg)
		entEid3.config(validate="none")
		entEid3.delete(0,END)
		entEid3.config(validate="key")
		entEid3.focus()
	except cx_Oracle.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Failure",e)
	except UnboundLocalError as e:
		print()
		
	
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
def deleteBackOp():
	entEid3.config(validate="none")
	entEid3.delete(0,END)
	entEid3.config(validate="key")
	root.deiconify()
	deleteEmp.withdraw()

btnSave3=Button(deleteEmp,text='Save',command=deleteSaveOp)
btnBack3=Button(deleteEmp,text='Back', command=deleteBackOp)

btnSave3.pack(pady=10)
btnBack3.pack(pady=10)

graphEmp=Toplevel(root)
graphEmp.title("Graph M")
graphEmp.geometry('600x400+400+150')
graphEmp.withdraw()

def graphLineOp():
	import cx_Oracle
	con=None
	cursor=None

	try:
		con=cx_Oracle.connect("system/abc123")
		print("U R Connected")
		cursor=con.cursor()
		sql='select eid,ename,emarks from sms'
		cursor.execute(sql)
		data=cursor.fetchall()
		ename=[]
		emark1=[]
		print("Total number of row count :",cursor.rowcount)
		for d in data:
			ename.append(d[1])
			emark1.append(d[2])
		print(ename)
		print(emark1)	
	except cx_OracleDatabaseError as e:
		print("Issue :",e )
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()
	

	from matplotlib import pyplot as plt
	plt.plot(ename,emark1,label="Mark")
	plt.title("Exam Score")
	plt.xlabel("Students Name")
	plt.ylabel("Marks")
	#plt.legend(loc="upper right",shadow=True)
	plt.grid()
	plt.show()

def graphBarOp():
	import cx_Oracle
	con=None
	cursor=None

	try:
		con=cx_Oracle.connect("system/abc123")
		print("U R Connected")
		cursor=con.cursor()
		sql='select eid,ename,emarks from sms'
		cursor.execute(sql)
		data=cursor.fetchall()
		ename1=[]
		emark1=[]
		print("Total number of row count :",cursor.rowcount)
		for d in data:
			ename1.append(d[1])
			emark1.append(d[2])
		print(ename1)
		print(emark1)	
	except cx_OracleDatabaseError as e:
		print("Issue :",e )
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()


	import matplotlib.pyplot as plt
	import numpy as np
	x=np.arange(len(ename1))
	emark2=[10,25,32,67,32,55,80,43,21,77,32]
	plt.bar(x,emark1,label="Mark",color='y') #alpha=0.8
	plt.xticks(x,ename1,fontsize=5)
	plt.title("Exam Score")
	plt.xlabel("Students Name",fontsize=15)
	plt.ylabel("Marks",fontsize=15)
	#plt.legend(loc="upper right",shadow=True)
	plt.grid()
	plt.show()

def graphBackOp():
	root.deiconify()
	graphEmp.withdraw()
	

btnLine=Button(graphEmp,text='Line',command=graphLineOp)
btnBar=Button(graphEmp,text='Bar', command=graphBarOp)
btnGraphBack=Button(graphEmp,text='Back',command=graphBackOp)

btnLine.pack(ipadx=10,ipady=5,pady=15)
btnBar.pack(ipadx=12,ipady=5)
btnGraphBack.pack(ipadx=10,ipady=5,pady=15)

root.mainloop()
