import psycopg2
def create():
    connection=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE student(ID SERIAL,NAME TEXT,ADD TEXT,AGE INT);''')
    print("table created")
    connection.commit()
    connection.close()

def insert_data():
    connection=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    cursor=connection.cursor()
    name=input("Enter Name: ")
    add=input("Enter Add: ")
    age=int(input("Enter Age: "))

    query='''INSERT INTO student(NAME,ADD,AGE) VALUES(%s,%s,%s);'''
    cursor.execute(query,(name,add,age))
    print("table data inserted")
    connection.commit()
    connection.close()
insert_data()