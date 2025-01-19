from car_management import Manage_Car
from user import User_operation
from admin_info import Admin
from user_data import UserData
def operationsMenu():
    print("X"*20 + "  Welcome To Car Rental System  " + "X"*20)
    admin = Admin()
    c_opr = Manage_Car()
    user_data = UserData()
    user = User_operation()
    while True:
        print("")
        print("*" * 15 + " HOME PAGE " + "*" * 15 )
        print("\t\t 1. Login as a Admin. \n\t\t 2. Login as a User. \n\t\t 3. Exit.")
        try:
            choose = int(input("Choose any one the above options:  "))
            if choose == 1:
                print("\n" + "X"*20 + "  Welcom to Car Rental Admin System  " + "X"*20 + "\n")
                # logged_in = None
                print("Please Login Here !!! ")

                
                
                if admin.login_admin():
                    while True:
                        print("*"*15 + " Admin Page " + "*"*15)
                        print("\t\t 1. Add Car.") 
                        print("\t\t 2. Delete Car.") 
                        print("\t\t 3. Update Car's data.")
                        print("\t\t 4. View All Cars.") 
                        print("\t\t 5. Search Car using car model.")
                        print("\t\t 6. Search Car using car Number.")
                        print("\t\t 7. View Booked Car.") 
                        print("\t\t 8. Go to Home Page.")
                        car_operation = int(input("Please type the number of the operation you want to choose:  "))
                        if car_operation == 1:
                            make = input("\n\t\t Enter Company of Car : ")
                            model = input("\t\t Enter car model : ")
                            car_num = input("\t\t Enter Car Number : ")
                            car_rent = float(input("\t\t Enter one day rent of car  : "))
                            car_aval = int(input("\t\t Enter Car Availability Status : "))  
                            color = input("\t\t Enter Car's Color : ")
                            Fuel_Type = input("\t\t Enter Fuel Type : ")
                            seats = int(input("\t\t Enter Total number of Seats Available in Car : "))
                            date_of_seviced = input("\t\t Enter Data of Last Serviced (DD/MM/YYYY) : ")
                            c_opr.add(make, model, car_num, car_rent, color, Fuel_Type, seats, date_of_seviced, car_aval)
                            print(f"Car details for {model} Successfully Added. ")

                        elif car_operation == 2:
                            print("Delete Car Details using Car Liecens number")
                            car_num = input("Enter Car Number : ")
                            c_opr.delete(car_num)

                        elif car_operation == 3:
                            print("Update Car Details using Car Liecens number")
                            car_num = input("Enter Car Number to Modify Car's Data : ")
                            c_opr.update_data(car_num)

                        elif car_operation == 4:
                            print("\t\t View all Cars Detail !!!")
                            c_opr.viewCar()
                            print("\n")

                        elif car_operation == 5:
                            print("Search Car using Cars Model ")
                            car_model = input("Enter Model : ")
                            c_opr.search_byModel(car_model)
                            print("\n")

                        elif car_operation == 6:
                            print("Search Car using Cars Number ")
                            car_model = input("Enter Model : ")
                            c_opr.search_byNum(car_model)
                            print("\n")
                        
                        elif car_operation == 7:
                            print("\t\tAll Customer's Data")
                            c_opr.viewall_BookingData()

                        elif car_operation == 8:
                            print("Thank you for managing the Car Rental System, Have a Good Day ")
                            break
                        else:
                            print("Invalid choice! Please enter a valid option (1-5)")
                else:
                    print("Username and password not matched")
            
            elif choose == 2:
            
                print("\nWelcome to our Car Rental Service! Ready to hit the road? Let's get started. " + "\n")
                login_option = input("Do you have an account? (yes/no): ").lower()

                if login_option == 'no' or login_option =='n':
                    user_data.register_user()
                elif login_option == 'yes' or login_option == 'y':
                    login = user_data.login_user()
                    
                    if login:
                        while True:
                            print("*"*15 + " User Page " + "*" *15)
                            print("\n\t\t 1. Book car. \n\t\t 2. Pickup Car. \n\t\t 3. Return The Car. \n\t\t 4. Go to Home page. ")
                            print("\n")
                            choice = int(input("Enter Your Choice: "))
                            if choice == 1:
                                u_username = user_data.logged_userName()
                                start_amt = float(input("Enter the starting amount of your budget (in Rupees ) : "))
                                end_amt = float(input("Enter the maximum amount you're willing to spend (in Rupees ): "))
                                user.bookCar(u_username,start_amt, end_amt)
                            elif choice == 2:
                                pickup_booking_id = input("Enter Car Booing ID : ")
                                user.pickCar(pickup_booking_id)
                            elif choice == 3:
                                return_booking_id = input("Enter car booking ID : ")
                                car_model = input("Enter Car model : ")
                                car_num = input("Enter Car number : ")
                                user.Return(return_booking_id, car_model, car_num)
                            elif choice == 4:
                                print("Thank you. ")
                                break
                            else:
                                print("Please choose correct option. (1 - 4)")

            elif choose == 3:
                print("Thank You !!!")
                break
            elif choose == 4:
                print("Invalid input.\nPlease Enter Valid number.. As shown in Menu.")
        except ValueError:
            print("Value Error : Please Enter Numeric Value/ number/ digit !")
                   
if __name__ == "__main__":
    operationsMenu()