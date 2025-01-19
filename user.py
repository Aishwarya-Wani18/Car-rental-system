from datetime import datetime
from prettytable import PrettyTable
from car_management import Manage_Car
from car_rental_system_balance import Balance

class User_operation():
    def __init__(self):
        self.car_management = Manage_Car()
        self.balance = Balance()
    
    def bookCar(self, user_id, starting_amt, end_amt):
        car_found = False
        available_cars = []
        try:   
            table = PrettyTable()
            table.field_names = ["Car Company", "Car Model", "Car Rent", "Last Servicing Date"]
            
            with open("car_details.txt","r+") as file:
                for car in file:
                    carData = car.strip().split(", ") # Strip newline and split by comma.
                    car_rent = float(carData[3])
                    car_avail = int(carData[8])
                    
                    #Check Available car within User's range price.
                    if starting_amt <= car_rent <= end_amt and car_avail == 1:
                        table.add_row([carData[0], carData[1], carData[3], carData[7]])
                        available_cars.append(carData)
                        car_found = True
                if not car_found:
                    print("Car not found within your range. ")
                                 
                else:
                    print("Available Cars within your range.")
                    print(table)

                    ans = input("\t\t Do you want to book Car (type 'yes' or 'no'): ").title()
                    if ans == "Yes" or "Y":
                        model_input = input("\t\t Enter the car model you want to book : ")
                        selected_car = None
                        for car in available_cars:
                            if car[1] == model_input:
                                selected_car = car
                                break
                        else:
                            print("Car model not matched with available car data. ")
                    
                        if selected_car:
                            print(f"\t\t Selected Car : \n\t\t model - {selected_car[1]} \n\t\t Rent for one day : {selected_car[3]}")
                            print(f"\t\t Booking Successfully Done for - {user_id} \n\t\t Your user ID consider as as booking ID. ")
                            
                            # Take Dates from the user. 
                            pickup_date = input("Enter Pickup date (dd/mm/yyyy): ")
                            return_date = input("Enter Return Date (dd/mm/yyyy): ")

                            # Convert string in list
                            pickup_date = pickup_date.split("/")
                            return_date = return_date.split("/")

                            # Date time format
                            self.car_pickup_Date = datetime(int(pickup_date[2]),int(pickup_date[1]),int(pickup_date[0]))
                            self.car_return_Date = datetime(int(return_date[2]),int(return_date[1]),int(return_date[0]))

                            # Convert datetime to string
                            str_pickupDate = str(self.car_pickup_Date)
                            str_returnDate = str(self.car_return_Date)
                            # Calculate Total rental days.
                            rental_days = (self.car_return_Date - self.car_pickup_Date).days

                            if rental_days < 1:
                                print("Invalid dates. Return date must be after pickup date. ")
                                return
                            
                            self.total_rent = rental_days * float(selected_car[3])
                            selected_car[8] = "0"     # set availability 0 if car booked.
                            with open("car_details.txt", "r") as file:
                                lines = file.readlines()

                            with open("car_details.txt", "w") as file:
                                for car in lines:
                                    car_data = car.strip().split(", ")
                                    if car_data[2] == selected_car[2]:
                                        car_data[8] = "0"
                                    file.write(", ".join(car_data) + "\n")

                            car_booking_details = {
                                "user_id": user_id,
                                "car_company" : selected_car[0],
                                "car_model" : selected_car[1],
                                "car_rent" : selected_car[3],
                                "last_servicing_date" : selected_car[7],
                                "Pickup_date" : str_pickupDate,
                                "Return_date" : str_returnDate,
                                "Total_rent" : self.total_rent,
                                "Car_num":selected_car[2]
                            }
                            with open("Booked_car.txt","a") as carfile:
                                carfile.write(f"Booking ID : {user_id}, Car Company : {car_booking_details["car_company"]}, Car Model : {car_booking_details["car_model"]}, Pickup date : {car_booking_details["Pickup_date"]}, Return date : {car_booking_details["Return_date"]}, Total Rent : {car_booking_details["Total_rent"]}, One Day rent : {car_booking_details["car_rent"]}, Car Number : {car_booking_details["Car_num"]}\n")
                                
                            print("Car Booked Successfully. ")  
                            print("*"* 20  + "  Booking datails.  " + "*"*20)
                            print((f"Booking ID : {user_id}, \nCar Company : {car_booking_details["car_company"]}, \nCar Model : {car_booking_details["car_model"]}, \nRent : {car_booking_details["car_rent"]}, \nLast Servicing Date : {car_booking_details["last_servicing_date"]}, \nCar number : {car_booking_details['Car_num']} "))
   
                    elif ans == "No" or ans == "N":
                        print("That's okay! Feel free to explore other options or contact us if you need help. ")                                                       
                    else:
                        print("Invalid Input ! Please Type 'Yes' or 'No' to proceed. ")
        except FileNotFoundError:
            print("File not Exist. ")
    def pickCar(self,booking_id):
        account = 0
        try:
            with open("Booked_car.txt", "r") as carfile:
                booking = carfile.readlines()
                car_found = False

                for i,car in enumerate(booking):
                    if f"Booking ID : {booking_id}" in car:
                        booking_details = car.strip().split(", ")
                        total_rent = 0
                        car_model = None
                        Car_num = None
                        for data in booking_details:
                            if "Car Model" in data:
                                car_model = data.split(":")[1].split()
                                print(f"Car Model : {car_model}")
                            if "Car Number" in data:
                                Car_num = data.split(":")[1].split()
                                print(f"Car Number : {Car_num}")
                            if "Total Rent" in data:
                                total_rent = float(data.split(":")[1].strip())
                                print(f"Total Rent to be paid: {total_rent}")
                                break
                            
                        payment = float(input("Make Payment here: "))          
                        if payment == total_rent:
                            print(f"Payment of {payment} Rs. done Successfully. ")
                            account += payment
                            booking[i] = car.strip() + f", payment: {payment}\n"
                            car_found = True
                        else:
                            print(f"Please pay the remaining amount : {total_rent-payment}")
                            return            
                        break
                if not car_found:
                    print("Booking ID not found. ")
                    return
            with open("Booked_car.txt", 'w') as carfile:
                carfile.writelines(booking)                    
        except FileNotFoundError:
            print("File not exist. ")
   
    def Return(self, booking_id, model, car_num):
        try:

            with open("Booked_car.txt", 'r') as Carfile:
                bookings = Carfile.readlines()          
            car_found = False
            for i,car in enumerate(bookings):
                if f"Booking ID : {booking_id}" in car:
                    car_details = car.strip().split(", ")
                    pickup_date = None 
                    return_date = None
                    paid_amount = 0
                    car_rent = 0

                    for data in car_details:
                        # print(data)
                        if "Pickup date" in data:
                            pickup_date = data.split(":")[1].strip("00").strip()
                        if "Return date" in data:
                            return_date = data.split(":")[1].strip("00").strip()
                        if "payment" in data:
                            paid_amount = float(data.split(":")[1].strip())
                        if "One Day rent" in data:
                            car_rent = float(data.split(":")[1].strip())
                    
                    actual_return_Date_input = input("Enter Return Date in format (dd/mm/yyyy) : ")
                    try:
                        actual_return_Date = datetime.strptime(actual_return_Date_input, "%d/%m/%Y")
                        car_return = datetime.strptime(return_date, "%Y-%m-%d") if return_date else None
                        car_pickup = datetime.strptime(pickup_date, "%Y-%m-%d") if pickup_date else None   
                    except:
                        print("Invalid Date !. please enter valid Date in the format (dd/mm/yyyy)")
                        return
                            
                    if car_pickup and actual_return_Date:
                        days_rent = (actual_return_Date - car_pickup).days
                        total_rent = days_rent * car_rent
                    
                    print(f"Total Rent for {days_rent} days: {total_rent}Rs.")
                    if total_rent == paid_amount:
                        print("Your Booking Has been Updates. ")
                        bookings.pop(i)
                        with open("Booked_car.txt",'w') as CarFile:
                                CarFile.writelines(bookings)
                        with open("car_details.txt", 'r') as Carfile:
                            lines = Carfile.readlines()

                            with open("car_details.txt", 'w') as carfile:
                                for line in lines:
                                    car_data = line.strip().split(", ")
                                    if car_data[2] == car_num and car_data[1] == model:
                                        car_data[8] = '1'
                                    carfile.write(", ".join(car_data) + "\n")

                    elif total_rent > paid_amount:
                        remaining_amt = total_rent - paid_amount
                        payment = float(input(f"Please Pay the remaining amount of {remaining_amt}Rs.: "))

                        if payment == remaining_amt:
                            print("Payment Successful. Your booking has been updated. ")
                            
                            # After payment. remove the user's data from "Booked_car.txt"
                            bookings.pop(i)

                            # Update "Booked_car.txt" file to remove the booking.
                            with open("Booked_car.txt",'w') as CarFile:
                                CarFile.writelines(bookings)
                            
                            with open("car_details.txt", 'r') as Carfile:
                                lines = Carfile.readlines()

                            with open("car_details.txt", 'w') as carfile:
                                for line in lines:
                                    car_data = line.strip().split(", ")
                                    if car_data[2] == car_num and car_data[1] == model:
                                        car_data[8] = '1'
                                    carfile.write(", ".join(car_data) + "\n")
                    print("Car Returned Successfully")
                    car_found = True
                    break

            if not car_found:
                print(f"Booking ID: {booking_id} not found. ")
        except FileNotFoundError:
            print("Error. Booked Car File not Found. ")

