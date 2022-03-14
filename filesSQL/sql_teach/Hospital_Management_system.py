from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import tkinter

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        

        self.nameoftables=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftables=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowtoUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("times new roman",12,"bold"),text="patient information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE,bg='green')
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        

        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        ##############DataFrameLeft#######################

        lblNameTablet = Label(DataframeLeft,text="Name of Tables",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet = ttk.Combobox(DataframeLeft,textvariable=self.nameoftables,state="readonly",font=("times new roman",12,"bold"), width=33)
        comNametablet["values"] = ("Nice","Corona","Corona Vacine",'Acetaminophe',"Adderall","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref = Label(DataframeLeft,text="Referencr No.",font=("times new roman",12,"bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        textref = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.ref, width=35)
        textref.grid(row=1,column=1)

        
        lblDose = Label(DataframeLeft,text="Dose",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        texDose = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.Dose, width=35)
        texDose.grid(row=2,column=1)

        
        lblNoOftablets = Label(DataframeLeft,text="No. of tables",font=("times new roman",12,"bold"),padx=2)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        textNoOftablets = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.Numberoftables, width=35)
        textNoOftablets.grid(row=3,column=1)


        lbllot = Label(DataframeLeft,text="Lot.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbllot.grid(row=4,column=0,sticky=W)
        textLot = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.Lot, width=35)
        textLot.grid(row=4,column=1)

        lblissueDate = Label(DataframeLeft,text="Issue Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        textIssueDate = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.IssueDate, width=35)
        textIssueDate.grid(row=5,column=1)
        

        lblExpireDate = Label(DataframeLeft,text="Expire Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblExpireDate.grid(row=6,column=0,sticky=W)
        textExpireDate = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.ExpDate, width=35)
        textExpireDate.grid(row=6,column=1)

        lblDailydose = Label(DataframeLeft,text="Daily Dose",font=("times new roman",12,"bold"),padx=2,pady=4)
        lblDailydose.grid(row=7,column=0,sticky=W)
        textDailyDose = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.DailyDose, width=35)
        textDailyDose.grid(row=7,column=1)
        ##

        lblSideeffect = Label(DataframeLeft,text="Side Effect",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSideeffect.grid(row=8,column=0,sticky=W)
        textSideEffect = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.SideEffect, width=35)
        textSideEffect.grid(row=8,column=1)

        
        lblFurtherInfo = Label(DataframeLeft,text="Further Information",font=("times new roman",12,"bold"),padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        textFurtherInfo = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.FurtherInformation, width=35)
        textFurtherInfo.grid(row=0,column=3)

        lblDrivingMachine = Label(DataframeLeft,text="Blood Pressure",font=("times new roman",12,"bold"),padx=2)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        textDrivingMachine = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.DrivingUsingMachine, width=35)
        textDrivingMachine.grid(row=1,column=3)
        
        lblStorageAdvice = Label(DataframeLeft,text="Storage Advice: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblStorageAdvice.grid(row=2,column=2,sticky=W)
        textStorageAdvice = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.StorageAdvice, width=35)
        textStorageAdvice.grid(row=2,column=3)
        
        lblMedication = Label(DataframeLeft,text="Medication: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        textMedication = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.HowtoUseMedication, width=35)
        textMedication.grid(row=3,column=3)
        
        lblPatientId = Label(DataframeLeft,text="Patient Id: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        textPatientId = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.PatientId, width=35)
        textPatientId.grid(row=4,column=3)
        
        lblNHSnumber = Label(DataframeLeft,text="NHS Number.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNHSnumber.grid(row=5,column=2,sticky=W)
        textNHSNumber = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.nhsNumber, width=35)
        textNHSNumber.grid(row=5,column=3)

        
        lblPatientname = Label(DataframeLeft,text="Patient Name: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        textPatientname = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.PatientName, width=35)
        textPatientname.grid(row=6,column=3)
        
        lbldob = Label(DataframeLeft,text="Date of Birth: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbldob.grid(row=7,column=2,sticky=W)
        textdob = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.DateofBirth, width=35)
        textdob.grid(row=7,column=3)
        
        lblPatientAddress = Label(DataframeLeft,text="Patient Address.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        textPatientAddress = Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.PatientAddress, width=35)
        textPatientAddress.grid(row=8,column=3)

        ############################## Dataframe Right#######################################
        self.txtPrescription = Text(DataframeRight,font=("times new roman",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        ##############################Buttons##########################################

        btnPrescription = Button(Buttonframe,command = self.iPrectionription,text = "Red",bg='red',fg='blue',font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)


        btnPrescriptionData = Button(Buttonframe,command = self.iPrescriptionData,text="Prescription Data",bg='green',fg='white',font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6 )
        btnPrescriptionData.grid(row=0,column=1)
        
        btnUpdate = Button(Buttonframe,command = self.update,text="Update ",bg='green',fg='white',font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete = Button(Buttonframe,command = self.iDelete,text="Delete",bg='green',fg='white',font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)
        
        btnClear = Button(Buttonframe,command = self.clear,text="Clear",bg='green',fg='white',font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnClear.grid(row=0,column=4)
        
        btnExit = Button(Buttonframe,command = self.iExit,text="Exit",bg='green',fg='white',font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        ############################Table##########################################

        ###########################Scroll Bar######################################

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe,column=("nameoftables","ref","dose","nooftables","lot","issuedate",
        "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x =ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y =ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftables",text="Name of tablte")
        self.hospital_table.heading("ref",text="Refereance")
        self.hospital_table.heading("dose",text="Doses")
        self.hospital_table.heading("nooftables",text="Number of tablt")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue date")
        self.hospital_table.heading("expdate",text="Expire date")
        self.hospital_table.heading("dailydose",text="Daily Doses")
        self.hospital_table.heading("storage",text="Storages")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table['show'] = "headings"
        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.column("nameoftables",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftables",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fatch_data()


        ############################# Functionality Declaration########################
        

    def iPrescriptionData(self):
        if self.Numberoftables.get() == "" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="user",database="mydata")
            my_cursor = conn.cursor()    
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.nameoftables.get(),
                                                                                                        self.ref.get(),
                                                                                                        self.Dose.get(),
                                                                                                        self.Numberoftables.get(),
                                                                                                        self.Lot.get(),
                                                                                                        self.IssueDate.get(),
                                                                                                        self.ExpDate.get(),
                                                                                                        self.DailyDose.get(),
                                                                                                        self.StorageAdvice.get(),
                                                                                                        self.nhsNumber.get(),
                                                                                                        self.PatientName.get(),
                                                                                                        self.DateofBirth.get(),
                                                                                                        self.PatientAddress.get()
                                                                                                        ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")       

    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="user",database="mydata")
        my_cursor = conn.cursor() 
        my_cursor.execute("update hospital set Nameoftablets=%s, dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s,  expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s where Reference_No=%s",(
                                                                                                        self.nameoftables.get(),
                                                                                                        self.Dose.get(),
                                                                                                        self.Numberoftables.get(),
                                                                                                        self.Lot.get(),
                                                                                                        self.IssueDate.get(),
                                                                                                        self.ExpDate.get(),
                                                                                                        self.DailyDose.get(),
                                                                                                        self.StorageAdvice.get(),
                                                                                                        self.nhsNumber.get(),
                                                                                                        self.PatientName.get(),
                                                                                                        self.DateofBirth.get(),
                                                                                                        self.PatientAddress.get(),
                                                                                                        self.ref.get(),
                                                                                                        ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record has been Updated")                                                                                          
                                                                                






    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="user",database="mydata")
        my_cursor = conn.cursor() 
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()        

    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        content= self.hospital_table.item(cursor_row)
        row = content["values"]
        self.nameoftables.set(row[0]) 
        self.ref.set(row[1]) 
        self.Dose.set(row[2]) 
        self.Numberoftables.set(row[3]) 
        self.Lot.set(row[4]) 
        self.IssueDate.set(row[5]) 
        self.ExpDate.set(row[6]) 
        self.DailyDose.set(row[7]) 
        self.StorageAdvice.set(row[8]) 
        self.nhsNumber.set(row[9]) 
        self.PatientName.set(row[10]) 
        self.DateofBirth.set(row[11]) 
        self.PatientAddress.set(row[12])   

    def iPrectionription(self):
        self.txtPrescription.insert(END,"Name of Tablets: \t\t\t"+self.nameoftables.get() + "\n")  
        self.txtPrescription.insert(END,"Referance number: \t\t\t"+self.ref.get() + "\n")  
        self.txtPrescription.insert(END,"Dose: \t\t\t"+self.Dose.get() + "\n")  
        self.txtPrescription.insert(END,"Number of tablets : \t\t\t"+self.Numberoftables.get() + "\n")  
        self.txtPrescription.insert(END,"Lot: \t\t\t"+self.Lot.get() + "\n")  
        self.txtPrescription.insert(END,"Issue date: \t\t\t"+self.IssueDate.get() + "\n")  
        self.txtPrescription.insert(END,"Expire date: \t\t\t"+self.ExpDate.get() + "\n")  
        self.txtPrescription.insert(END,"daily Dose: \t\t\t"+self.DailyDose.get() + "\n")  
        self.txtPrescription.insert(END,"Side Effect: \t\t\t"+self.SideEffect.get() + "\n")  
        self.txtPrescription.insert(END,"Further Details.: \t\t\t"+self.FurtherInformation.get() + "\n")  
        self.txtPrescription.insert(END,"Storage Advice: \t\t\t"+self.StorageAdvice.get() + "\n")  
        self.txtPrescription.insert(END,"Driving Using Machine: \t\t\t"+self.DrivingUsingMachine.get() + "\n")  
        self.txtPrescription.insert(END,"Patient Id: \t\t\t"+self.PatientId.get() + "\n")  
        self.txtPrescription.insert(END,"NHS Number: \t\t\t"+self.nhsNumber.get() + "\n")  
        self.txtPrescription.insert(END,"Patient name: \t\t\t"+self.PatientName.get() + "\n")  
        self.txtPrescription.insert(END,"Date of Birth: \t\t\t"+self.DateofBirth.get() + "\n")  
        self.txtPrescription.insert(END,"Patient Address: \t\t\t"+self.PatientAddress.get() + "\n") 


    def iDelete(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="user",database="mydata")
        my_cursor = conn.cursor() 
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo("Delete","message has been deleted successfully")


    def clear(self):
        self.nameoftables.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Numberoftables.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowtoUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateofBirth.set("")
        self.PatientAddress.set("")


    def iExit(self):
        iExit=messagebox.askyesno("Hospital manegement system","Confirm you want to exit")
        if iExit >0:
            root.destroy()
            return



root = Tk()
ob = Hospital(root)
root.mainloop()