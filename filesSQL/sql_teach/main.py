import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost",port="3306",user="root",password="user",database="pythontest")

        query = "create table if not exists user(userId int primary key , userName varchar(100) , phone varchar(12))"

        cur = self.con.cursor()
        cur.execute(query)
        # print("Created")

    # insert function
    def insert_user(self,userid,username,phone):
        query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to query")


    # fetch data from sql
    def fetch_data(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query) 
        for row in cur:
            print("User Id : ",row[0])   
            print("User Name : ",row[1])   
            print("User Phone : ",row[2])   
            print()

    def fetch_one_data(self,id):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query) 
        for row in cur:
            if row[0] == id:          
                print("User Id : ",row[0])   
                print("User Name : ",row[1])   
                print("User Phone : ",row[2])   
                print()        

    # delete a data

    def delete_user(self,userId):
        query = "delete from user where userId = {}".format(userId)
        cur = self.con.cursor()
        cur.execute(query) 
        self.con.commit()
        print("deleted")

    # update
    def updata_data(self,userId,newName,newphone):
        query ="update user set userName='{}',phone='{}' where userId ={}".format(newName,newphone,userId)
        cur = self.con.cursor()
        cur.execute(query) 
        self.con.commit()
        print("update")



# helper = DBHelper()        
# # helper.insert_user(128,"DeveshTri","1234567890")
# # helper.insert_user(124,"Ram","9305958149")
# # helper.insert_user(125,"Raj","9795984237")
# # helper.insert_user(126,"Sujai","8573916030")
# # helper.insert_user(127,"Vijay","8332759600")

# helper.updata_data(127,"Seema_Tripathi","234234234")
# helper.fetch_data()