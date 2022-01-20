from tkinter import *
from tkinter.messagebox import *
import requests
import pandas as pd
import requests
import bs4
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt 

try:
	a1 = "https://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + "kalyan"
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	wa = a1 + a2 + a3
	res = requests.get(wa)
	print(res)
	data = res.json()
	temp = data['main']['temp']
except Exception as e:
	print("issue", e)

res = requests.get('https://ipinfo.io/')
data = res.json()


location = data['city']

try:
	wa = "https://www.brainyquote.com/quote_of_the_day"
	res = requests.get(wa)
	print(res)
	data = bs4.BeautifulSoup(res.text, "html.parser")
	info = data.find('img', {"class":"p-qotd"})
	quote = info['alt']
except Exception as e:
	print("issue ",e)

main_window = Tk()
main_window.title("S.M.S")
main_window.geometry("900x600+280+50")

def f1():
	add_window.deiconify()#yeh window aayega
	main_window.withdraw()#yeh window drop
def f2():
	main_window.deiconify()
	add_window.withdraw()
def f3():


	view_window_st_data.delete(1.0, END)
	view_window.deiconify()
	main_window.withdraw()
	info = ""
	try:
		con = connect("project.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		con.commit()
		data = cursor.fetchall()
		for d in data:
			info = info + "rno= " + str(d[0]) + " name = " + str(d[1]) + " marks = " + str(d[2]) + "\n"
		view_window_st_data.insert(INSERT, info)
		
	except Exception as e:
		showerror("Issue ",e)
	finally:
		if con is not None:
			con.close()


def f4():
	update_window.deiconify()
	main_window.withdraw()


def f5():
	con = None
	
	try:
		con = connect("project.db")
		cursor = con.cursor()
		
		sql = "insert into student values('%d', '%s', '%d')"
		rno = int(add_window_ent_rno.get())
		name = add_window_ent_name.get()
		marks = int(add_window_ent_marks.get())
		
		try:
			if (len(name)) >= 2 and (marks >= 0) and (marks <=100):
				cursor.execute(sql % (rno, name, marks))
				print("executed")
				if (cursor.rowcount == 1) and (len(name) >= 2 ): #(second condition of name can be removed too)
					showinfo("Success","Record added")
				add_window_ent_rno.delete(0,END)
				add_window_ent_name.delete(0,END)
				add_window_ent_marks.delete(0,END)
				add_window_ent_rno.focus()
				print("commited")
				con.commit()
				print("commited")
			else:
				if len(name) < 2:
					showerror("Oops","Name invalid")
				elif (marks<0) or (marks > 100):
					showerror("Oops","Marks Invalid")
				else:
					print("Cursor rowcount error") 
				
		except:
			showerror("Oops","Roll number already exists")
			con.rollback()
			
	except Exception as e:
		showinfo("Oops","Please enter required information")
		print(e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
def f6():
	main_window.deiconify()
	view_window.withdraw()
def f7():
	main_window.deiconify()
	update_window.withdraw()

def f8():
	con = None
	

	try:
		con = connect("project.db")
		print("database created / opened")
		cursor = con.cursor()
		#data = cursor.fetchall()
		sql = "update student set marks = '%d' , name = '%s' where rno = '%d' "
		rno = int(update_window_ent_rno.get())
		name = update_window_ent_name.get()
		marks = int(update_window_ent_marks.get())
		#cursor.execute(sql % (marks, name, rno))
		if (len(name) >= 2) and (marks >= 0) and (marks <= 100):
			
			cursor.execute(sql % (marks, name, rno))
			print("executed")
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Success","RECORD UPDATED")
				update_window_ent_rno.delete(0,END)
				update_window_ent_name.delete(0,END)
				update_window_ent_marks.delete(0,END)
				update_window_ent_rno.focus()					
			else:
				showerror("Oops","Roll number does not exists")
		else:
			if len(name) < 2:
				showinfo("Oops","Invalid Name")
			elif (marks<0) or (marks > 100):
				showinfo("Oops","Marks Invalid")
			else:
				print("Cursor rowcount error") 	 
	except Exception as e:
			
		showinfo("Oops","Please enter required information")
		con.rollback()
	finally:
		if con is not None:
			con.close()
			#print("closed")
def f9():
	con = None

	try:
		con = connect("project.db")
		print("database created / opened")
		cursor = con.cursor()
		sql = "delete from student where rno = '%d' "
		rno = int(delete_window_ent_rno.get())
		
		cursor.execute(sql % (rno))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success","record deleted")
			delete_window_ent_rno.delete(0,END)
			
		else:
			showinfo("Oops","Rno does not exists ")
			delete_window_ent_rno.delete(0,END)
	except Exception as e:
		showerror("issue", "Please enter the required information")
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("closed")
def f10():
	delete_window.deiconify()#yeh window aayega
	main_window.withdraw()#yeh window drop

def f11():
	main_window.deiconify()#yeh window aayega
	delete_window.withdraw()#yeh window drop
def f12():
	con = None

	try:
		con = connect("project.db")
		print("database created / opened")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		marks=[]
		name = []
		for d in data:
			marks.append(d[2])
		print(marks)
		
		for n in data:
			name.append(n[1])
		print(name)	
		plt.bar(name, marks,color=['red', 'blue', 'purple', 'green', 'lavender'])
		plt.title("Batch Performance")
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.grid()
		plt.show()
	except Exception as e:
		print("issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("closed")


f= ("Arial", 20 ,'bold')
main_window_btn_add = Button(main_window, text= "Add", width=10, font=f, command=f1)
main_window_btn_view = Button(main_window, text="View", width=10,font=f, command=f3)
main_window_btn_update = Button(main_window, text="Update", width=10,font=f, command=f4)
main_window_btn_delete = Button(main_window, text="Delete", width=10,font=f, command=f10)
main_window_btn_chart = Button(main_window, text="Chart", width=10,font=f, command=f12)

main_window_btn_add.grid(padx=(0,400), pady=5)
main_window_btn_view.grid(padx=(0,400) ,pady=5)
main_window_btn_update.grid(padx=(0,400),pady=5)
main_window_btn_delete.grid(padx=(0,400) ,pady=5)
main_window_btn_chart.grid(padx=(0,400), pady=5)

fo = ("Arial", 12, 'bold')
main_window_lbl_location = Label(main_window, text="Location:" + str(location), font=fo) 
main_window_lbl_temp = Label(main_window, text="Temp:" + str(temp)+ "\u00B0" + "C", font=fo)
main_window_lbl_qotd = Label(main_window, text="QOTD:" + str(quote), font=fo)

main_window_lbl_location.grid(pady=10, padx=(0,1090))
main_window_lbl_temp.grid(row=5,padx=(200,0))
main_window_lbl_qotd.grid(row=7, padx=(0,485))


add_window = Toplevel(main_window)
add_window.title("ADD Student")
add_window.geometry("500x500+400+100")


add_window_lbl_rno = Label(add_window, text="Enter Rno.", font=f)
add_window_ent_rno = Entry(add_window, bd=5, font=f)
add_window_lbl_name = Label(add_window, text="Enter Name", font=f)
add_window_ent_name = Entry(add_window, bd=5, font=f)
add_window_btn_save = Button(add_window, text="Save", font=f, command=f5)
add_window_btn_back = Button(add_window, text="Back", font=f,  command=f2)
add_window_lbl_marks = Label(add_window, text="Marks", font=f)
add_window_ent_marks = Entry(add_window, bd=5, font=f)


add_window_lbl_rno.grid(padx = 150, pady=10)
add_window_ent_rno.grid()
add_window_lbl_name.grid(padx = 150, pady=10)
add_window_ent_name.grid()
add_window_lbl_marks.grid(padx=150, pady=10)
add_window_ent_marks.grid()
add_window_btn_save.grid(padx = 150, pady=10)
add_window_btn_back.grid(padx = 150, pady=10)

add_window.withdraw()

view_window = Toplevel(main_window)
view_window.title("View Student")
view_window.geometry("500x500+400+100")

view_window_st_data = ScrolledText(view_window, width = 30, height=10, font=f) # scroll button
view_window_btn_back = Button(view_window, text = "Back", font= f, command=f6)
view_window_st_data.grid(pady=10)
view_window_btn_back.grid(pady=10)
view_window.withdraw()


update_window = Toplevel(main_window)
update_window.title("Update Student")
update_window.geometry("500x500+400+100")

update_window_lbl_rno = Label(update_window, text="enter rno:", font=f)
update_window_ent_rno = Entry(update_window, bd=5, font=f)
update_window_lbl_name = Label(update_window, text="enter name:", font=f)
update_window_ent_name = Entry(update_window, bd=5, font=f)
update_window_lbl_marks = Label(update_window, text="enter marks:", font=f)
update_window_ent_marks = Entry(update_window, bd=5, font=f)
update_window_btn_save = Button(update_window, text="Save", font=f, command=f8)
update_window_btn_back = Button(update_window, text="Back", font=f, command=f7)


update_window_lbl_rno.grid(padx = 150, pady=10)
update_window_ent_rno.grid()
update_window_lbl_name.grid(padx = 150, pady=10)
update_window_ent_name.grid()
update_window_lbl_marks.grid(padx=150, pady=10)
update_window_ent_marks.grid()
update_window_btn_save.grid(padx = 150, pady=10)
update_window_btn_back.grid(padx = 150, pady=10)
update_window.withdraw()

delete_window = Toplevel(main_window)
delete_window.title("Delete Student")
delete_window.geometry("500x500+400+100")

delete_window_lbl_rno = Label(delete_window, text="Enter rollno to delete", font=f)
delete_window_ent_rno = Entry(delete_window, bd=5, font=f)
delete_window_btn_save = Button(delete_window, width= 10, text="Save", font=f, command=f9)
delete_window_btn_back = Button(delete_window, width=10, text="Back", font=f, command=f11)

delete_window_lbl_rno.grid(padx=150, pady=10)
delete_window_ent_rno.grid()
delete_window_btn_save.grid(padx=150, pady=10)
delete_window_btn_back.grid(padx=150, pady= 10)
delete_window.withdraw()

main_window.mainloop()  