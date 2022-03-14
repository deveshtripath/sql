from tkinter import *
from tkinter import ttk
import pymysql

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1520x800+0+0")
        side = TOP

        self.Roll_No_var = StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg='yellow',fg="red")
        title.pack(side=side,fill=X)

        Manage_Frame =Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        Manage_Frame.place(x=20,y=100,width=550,height=630)

        m_title=Label(Manage_Frame,text="Manage Student",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10,sticky=W,padx=20)

        lbl_Roll=Label(Manage_Frame,text="Roll no.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Roll.grid(row=1,column=0,pady=20,sticky=W,padx=20)

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),relief=GROOVE,bd=5)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        
        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=20,sticky=W,padx=20)

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),relief=GROOVE,bd=5)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

        
        lbl_Email=Label(Manage_Frame,text="Email id",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=20,sticky=W,padx=20)

        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),relief=GROOVE,bd=5)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky='w')

        
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,sticky=W,padx=20)

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",20,"bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)
        

        lbl_Contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,sticky=W,padx=20)

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),relief=GROOVE,bd=5)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky='w')
        
        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,sticky=W,padx=20)

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),relief=GROOVE,bd=5)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky='w')
        
        lbl_address=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,sticky=W,padx=20)

        self.txt_address=Text(Manage_Frame,font=("times new roman",15,"bold"),width=30,height=3)
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky='w')



        ####################################################################

        
        btn_Frame =Frame(Manage_Frame,bd=4,relief=RIDGE,bg='crimson')
        btn_Frame.place(x=15,y=550,width=450)

        Addbtn = Button(btn_Frame,command=self.add_students,text='Add',width=10).grid(row=0,column=0,padx=12,pady=10)
        updatebtn = Button(btn_Frame,command=self.update,text='Update',width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn = Button(btn_Frame,command=self.delete,text='Delete',width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn = Button(btn_Frame,command=self.clear,text='Clear',width=10).grid(row=0,column=3,padx=10,pady=10)


############################   Detail Frame   ######################################################
        
        Detail_Frame =Frame(self.root,bd=4,relief=RIDGE,bg='crimson')
        Detail_Frame.place(x=600,y=100,width=870,height=630)

        lbl_Search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,sticky=W,padx=20)

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",20,"bold"),state="readonly")
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),relief=GROOVE,bd=5)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')
        searchbtn = Button(Detail_Frame,command=self.search_data,text='Search',width=10).grid(row=0,column=3,padx=10,pady=10)
        showbtn = Button(Detail_Frame,command=self.fetch_data,text='Show',width=10).grid(row=0,column=4,padx=10,pady=10)
        
        ###################  Table frame ###########################################

        Table_Frame =Frame(Detail_Frame,bd=4,relief=RIDGE,bg='crimson')
        Table_Frame.place(x=10,y=70,width=830,height=540)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,column=("roll",'name','email','gender','contact','dob','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll no.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="Date of Birth")
        self.Student_table.heading("Address",text="Address ")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=120)
        self.Student_table.column("email",width=120)
        self.Student_table.column("gender",width=120)
        self.Student_table.column("contact",width=120)
        self.Student_table.column("dob",width=120)
        self.Student_table.column("Address",width=120)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.Student_table.bind('<ButtonRelease-1>',self.get_cursor)
    

    def add_students(self):
            con =pymysql.connect(host="localhost",user="root",password="user",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.Roll_No_var.get(),
                        self.name_var.get(),
                        self.email_var.get(),
                        self.gender_var.get(),
                        self.contact_var.get(),
                        self.dob_var.get(),
                        self.txt_address.get('1.0',END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()


    def fetch_data(self):
            con =pymysql.connect(host="localhost",user="root",password="user",database="stm")
            cur=con.cursor()
            cur.execute("select * from students")
            rows =cur.fetchall()
            if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                            self.Student_table.insert('',END,values=row)
                    con.commit()        
            con.close()        

    def clear(self):
            self.Roll_No_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_address.delete('1.0',END)

    def get_cursor(self,ev):
            cursor_row = self.Student_table.focus()
            contents=self.Student_table.item(cursor_row)
            row=contents['values']
            self.Roll_No_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.dob_var.set(row[5])
            self.txt_address.delete('1.0',END)
            self.txt_address.insert(END,row[6])

    def update(self):
            con =pymysql.connect(host="localhost",user="root",password="user",database="stm")
            cur=con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                                        self.name_var.get(),
                                                                                                                        self.email_var.get(),
                                                                                                                        self.gender_var.get(),
                                                                                                                        self.contact_var.get(),
                                                                                                                        self.dob_var.get(),
                                                                                                                        self.txt_address.get('1.0',END),
                                                                                                                        self.Roll_No_var.get()
                                                                                                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()

    def delete(self):
            con =pymysql.connect(host="localhost",user="root",password="user",database="stm")
            cur=con.cursor()
            cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()

    def search_data(self):
            con =pymysql.connect(host="localhost",user="root",password="user",database="stm")
            cur=con.cursor()
            cur.execute("select * from students where "+ str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
            rows =cur.fetchall()
            if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                            self.Student_table.insert('',END,values=row)
                    con.commit()        
            con.close()  




root =Tk()
ob = Student(root)        
root.mainloop()