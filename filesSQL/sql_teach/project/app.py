from tkinter import *
import tkinter
from tkinter import messagebox
import pymysql

window = tkinter.Tk()

window.geometry("900x450")

L = Label(window, text="Enter Student Id: ", font=('arial',30),fg='blue')
L.grid(row=0,column=0)
E =Entry(window,bd=5, width=50)
E.grid(row=0,column=1)


L1 = Label(window, text="Enter Student Name: ", font=('arial',30),fg='blue')
L1.grid(row=1,column=0)
E1 =Entry(window,bd=5, width=50)
E1.grid(row=1,column=1)


L2 = Label(window, text="Enter Student address: ", font=('arial',30),fg='blue')
L2.grid(row=2,column=0)
E2 =Entry(window,bd=5, width=50)
E2.grid(row=2,column=1)


def myButtonEvent(selection):
    print("Sudent id is : ",E.get())
    print("Sudent Name is : ",E1.get())
    print("Sudent Address is : ",E2.get())

    id = E.get()
    name= E1.get()
    address = E2.get()

    if selection in ("Insert"):
        con = pymysql.connect(host="localhost",user="root",password="user",database="test")
        cur = con.cursor()
        # cur.execute("Select version () ")
        # data = cur.fetchone()
        # print("Database create successfull",data)

        query = "create table if not exists student (id char(20) Not null , name char(20) , address char(20))"

        try:
            cur.execute(query)
            con.commit()
            print("table created Successfully")
        except Error as e:
            print("Error occur at database creation",e) 
            con.rollback()
            con.close()   

        insertQuery ="insert into student (id,name,address) values('%s','%s','%s')"%(id,name,address)

        try:
            cur.execute(insertQuery)
            con.commit()
            print("Student saved to Db table ",id,",",name,",",address)
            con.close()

        except Error as e:
            print("Error occur at database insertion",e) 
            con.rollback()
            con.close() 


    elif selection in ("Update"):
        try:
            con = pymysql.connect(host="localhost",user="root",password="user",database="test")
            cur = con.cursor()

            query = "update student set name='%s'"%(name)+", address='%s'"%(address)+" where id = '%s'"%(id)
            cur.execute(query)
            con.commit()
            con.close()
            print("student updated successfully ....",id)
        except Error as e:
            print("Error occur at database data update",e) 
            con.rollback()
            con.close() 

    elif selection in ("Delete"):
        try:
            con = pymysql.connect(host="localhost",user="root",password="user",database="test")
            cur = con.cursor()

            query = "delete from student where id = '%s'"%(id)
            cur.execute(query)
            con.commit()
            con.close()
            print("student delete successfully ....",id)

        except Error as e:
            print("Error occur at database data delete",e) 
            con.rollback()
            con.close()

    elif selection in ("Select"):
        try:
            con = pymysql.connect(host="localhost",user="root",password="user",database="test")
            cur = con.cursor()

            query = "select * from student where id = '%s'"%(id)
            cur.execute(query)
            rows = cur.fetchall()
            address1 = ''
            name1= ''
            id1 = ''
            for row in rows:
                id1 = row[0]
                name1 = row[1]
                address1=row[2]

            E.delete(0,END)
            E1.delete(0,END)
            E2.delete(0,END)
            
            E.insert(0,id1)
            E1.insert(0,name1)
            E2.insert(0,address1)

            con.close()
            print("student fetch successfully ....",id)

        except Error as e:
            print("Error occur at database data fetch",e)
            con.close()                 




BInsert = tkinter.Button(text='Insert',fg='black',bg='orange',font=('arail',20,'bold'),   command=lambda:myButtonEvent("Insert"))
BInsert.grid(row=5,column=0)

BUpdate = tkinter.Button(text='Update',fg='blue',bg='yellow',font=('arail',20,'bold'),command=lambda:myButtonEvent("Update"))
BUpdate.grid(row=5,column=1)

BDelete = tkinter.Button(text='Delete',fg='Red',bg='white',font=('arail',20,'bold'),   command=lambda:myButtonEvent("Delete"))
BDelete.grid(row=8,column=0)

BSelect = tkinter.Button(text='Select',fg='blue',bg='yellow',font=('arail',20,'bold'),   command=lambda:myButtonEvent("Select"))
BSelect.grid(row=8,column=1)




window.mainloop()
