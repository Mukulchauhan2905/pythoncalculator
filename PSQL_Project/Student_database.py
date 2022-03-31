from tkinter import *
import tkinter as tk
import psycopg2

 
root=Tk()

def get_data(name,add,age):
    connection=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    cursor=connection.cursor()
    query='''INSERT INTO student(NAME,ADD,AGE) VALUES(%s,%s,%s);'''
    cursor.execute(query,(name,add,age))
    print("Data inserted!!")
    connection.commit()
    connection.close()
    display_all()

def search(id):
    connection=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    cursor=connection.cursor()
    query='''SELECT * FROM student WHERE id=%s;'''
    cursor.execute(query,(id))
    row=cursor.fetchone()
    # print(row)
    display_search(row)
    connection.commit()
    connection.close()

def display_search(row):
    button=Button(frame,text="Drop",command=lambda:drop(id_search.get()))
    button.grid(row=9,column=2)
    listbox=Listbox(frame,width=20,height=1)
    listbox.grid(row=9,column=1)
    listbox.insert(END,row)

def display_all():
    connection=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    cursor=connection.cursor()
    query='''SELECT * FROM student;'''
    cursor.execute(query)
    row=cursor.fetchall()
    listbox=Listbox(frame,width=20,height=5)
    listbox.grid(row=10,column=1)
    for x in row:
        listbox.insert(END,x)

def drop(id):                                                                                                   # new feature added by me:-)
    connection=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    cursor=connection.cursor()
    query='''DELETE FROM student WHERE id=%s;'''
    cursor.execute(query,(id))
    connection.commit()
    connection.close()
    display_all()


canvas=Canvas(root,height=480,width=900)
canvas.pack()

frame=Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

label=Label(frame,text="Add data")  #we can also add some attributes for text like style font size
label.grid(row=0,column=1)

label=Label(frame,text="Name")  #we can also add some attributes for text like style font size
label.grid(row=1,column=0)

entry_name=Entry(frame) 
entry_name.grid(row=1,column=1)

label=Label(frame,text="Address")  #we can also add some attributes for text like style font size
label.grid(row=2,column=0)

entry_add=Entry(frame)
entry_add.grid(row=2,column=1)

label=Label(frame,text="Age")  #we can also add some attributes for text like style font size
label.grid(row=3,column=0)

entry_age=Entry(frame)
entry_age.grid(row=3,column=1)

button=Button(frame,text="Submit",command=lambda:get_data(entry_name.get(),entry_add.get(),entry_age.get()))
button.grid(row=4,column=1)

label=Label(frame,text="Search Data")
label.grid(row=5,column=1)

label=Label(frame,text="Search by Id")
label.grid(row=6,column=0)

id_search=Entry(frame)
id_search.grid(row=6,column=1)

button=Button(frame,text="Search",command=lambda:search(id_search.get()))
button.grid(row=6,column=2)
display_all()


root.mainloop()
