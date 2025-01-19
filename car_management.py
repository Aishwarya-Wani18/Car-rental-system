from car_data import Car
from prettytable import PrettyTable
from datetime import datetime
class Manage_Car:
    def __init__(self):
        self.car_details_file = 'car_details.txt'
    
    def get_available_cars(self, starting_amt, end_amt):
        available_car = []
        try:
            with open(self.car_details_file, 'r') as carfile:
                for car in carfile:
                    car_data = car.strip().split(", ")
                    car_rent = float(car_data[3])
                    car_avail = int(car_data[8])

                    # Check whether the car is available or not in customer's range and also check availability - 1 or 0
                    if starting_amt <= car_rent <= end_amt and car_avail == 1:
                        available_car.append(car_data)
        except FileNotFoundError:
            print("Car Details file not Found. ")

        return available_car
    

    def update_car_avail(self, car_model, availability):
        try:
            with open(self.car_details_file, 'r') as carfile:
                lines = carfile.readlines()
            
            with open(self.car_details_file, 'w') as carfile:
                for line in lines:
                    car_data = line.strip().split(", ")
                    if car_data[1] == car_model:
                        car_data[8] = availability  # update availability.
                    carfile.write(", ".join(car_data) + '\n')
        
        except FileNotFoundError:
            print("Car Details File not found. ")


    def add(self,make, model, car_num, car_rent, color, Fuel_type, seats, date_of_serviced, car_aval):
        self.make = make
        self.model = model
        self.car_num = car_num
        self.car_rent = car_rent
        self.color = color
        self.Fuel_type = Fuel_type
        self.seats = seats
        self.date_of_serviced = date_of_serviced
        self.car_aval = car_aval
        with open("car_details.txt", "a") as file:
            file.write(f"{self.make}, {self.model}, {self.car_num}, {self.car_rent}, {self.color}, {self.Fuel_type}, {self.seats}, {self.date_of_serviced}, {self.car_aval}\n")
          

    def delete(self, c_num):
        car_list = []
        car_found = False
        string = ""
        with open("car_details.txt","r") as file:
            for car in file:
                car = car.split(", ")
                if c_num != car[2]:
                    car_list.append(car)
                    # string = f"{self.make}, {self.model}, {self.car_num}, {self.car_rent}, {self.color}, {self.Fuel_type}, {self.seats}, {self.date_of_serviced}, {self.car_aval}\n"
            else:           
                car_found = True
                print("Data Deleted")
        if car_found:
            with open("car_details.txt","w") as file:
                # file.write(string)
                for car in car_list:
                    file.write(", ".join(car)) 
        else:
            print(f"{c_num} Car number not found. ")
            
    
    def viewCar(self):
        try:
            with open("car_details.txt", "r") as file:
                # Create a table using Prettytable Class for displaying data
                table = PrettyTable()
                table.field_names = ["Company of Car", "Model", "Car Number", "Rent Amount", "Colour", "Fuel Type", "Seats", "Last serviced Data", "Availability Status"]
                for line in file:
                    line = line.strip().split(", ")
                    # print(len(line))
                    table.add_row(line)
                    
                print(table)
                # car_data = file.read()
                # print(car_data)
                # print("\n")
        except FileNotFoundError:
            print("File does not exist. ")

    def search_byModel(self, car_model):
        car_found = False
        try:
            with open("car_details.txt", "r") as file:
                table = PrettyTable()
                table.field_names = ["Company of Car", "Model", "Car Number", "Rent Amount", "Colour", "Fuel Type", "Seats", "Last serviced Data", "Availability Status"]

                for line in file:
                    line = line.split(", ")
                    if car_model == line[1]:
                        table.add_row(line)
                        car_found = True
                if car_found:
                    print(table)                    
                else:
                    print(f"{car_model} is not Available. ")
        except:
            print("File Does not Exist. ")
    
    def search_byNum(self, car_Num):
        car_found = False
        try:
            with open("car_details.txt", "r") as file:
                table = PrettyTable()
                table.field_names = ["Company of Car", "Model", "Car Number", "Rent Amount", "Colour", "Fuel Type", "Seats", "Last serviced Data", "Availability Status"]

                for line in file:
                    line = line.split(", ")
                    if car_Num == line[2]:
                        table.add_row(line)
                        car_found = True
                if car_found:
                    print(table)                    
                else:
                    print(f"{car_Num} is not Available. ")
        except:
            print("File Does not Exist. ")
    
    def update_data(self,car_num):         
        car_list = []
        carNum_found = False
        try:
            with open("car_details.txt", "r") as file:
                for car in file:
                    car = car.split(", ")    # Convert Data into List. 
                    if car_num == car[2]:
                        carNum_found = True
                        new_rent= input("Do You want to update Rent Amount (Type 'yes' or 'No')").title()
                        if new_rent == "Yes" or new_rent == "Y":
                            try:
                                car[3] = (float(input("Enter new Rent : ")))
                            except ValueError:
                                print("Invalid rent Amount. please enter a valid number. ")

                        ser_date = input("Do You want to update Servicing Date. (type 'yes' or 'no') : ").title()
                        if ser_date == 'Yes' or ser_date == "Y":
                            car[7] = input("Enter New servicing Date (dd/mm/yyyy) : ")
                            # self.date_of_serviced = car_list
                        
                        # print(car)                  
                    car_list.append(car)
                # print(car_list(car))
            if carNum_found:
                with open("car_details.txt","w") as file:
                    # file.write(f"{car_list[0]}, {car_list[1]}, {car_list[2]}, {car_list[3]}, {car_list[4]}, {car_list[5]}, {car_list[6]}, {car_list[7]}, {car_list[8]}\n")
                    for car in car_list:
                        file.write(", ".join(map(str, car)))
            else:
                print("Car number not Found. ")
        except FileNotFoundError:
            print("File Does not Exist. ")
    
    def viewall_BookingData(self):
        try:
            with open("Booked_car.txt", "r") as file:
                # Create a table using Prettytable Class for displaying data
                table = PrettyTable()
                table.field_names = ["User ID", "Car Company", "Car Model", "Pickup Date", "Return Date", "Total Rent"]
                for line in file:
                    line = line.strip().split(", ")
                    # print(len(line))
                    table.add_row(line)
                    
                print(table)
                # car_data = file.read()
                # print(car_data)
                # print("\n")
        except FileNotFoundError:
            print("File does not exist. ")

    



