from main import DBHelper

def main():
    db = DBHelper()


    while True:
        print()
        print(50*"*")
        print()
        print ("Press 1 to insert new user")
        print ("Press 2 to display all user")
        print ("Press 3 to delete user")
        print ("Press 4 to update user")
        print ("Press 5 to exit program")
        print()

        try:
            choice = int(input())
            if(choice == 1):
                ids = input("Enter user id")
                name = input("Enter username")
                phone = input("Enter user phone")
                db.insert_user(ids,name,phone)
            elif choice == 2:
                db.fetch_data()
            elif choice == 3:
                ids = input("Enter id which you want to delete")
                db.delete_user(ids)
            elif choice == 4:
                ids = input("Enter user id which you want to update")
                name = input("Enter new username")
                phone = input("Enter new user phone")
                db.updata_data(ids,name,phone)
            elif choice == 5:
                break
            else:
                print("Invalid input ! try again ")
        except Exception as e:
            print(e)
            print("Invalid Detail ! Try again")        


if __name__ == "__main__":
    main()