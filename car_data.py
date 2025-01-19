class Car:
    def __init__(self,make, model_name, car_num, rent, color, Fuel_type, num_of_seats, last_serviced, availability):
        self.make = make
        self.model = model_name
        self.c_num = car_num
        self.rent = rent
        self.color = color
        self.fuelType = Fuel_type
        self.seats = num_of_seats
        self.last_serviced = last_serviced
        self.availability = availability
    
    # delf.make}, {self.model}, {self.c_num}, {self.rent}, {self.color}, {self.fuelType}, {self.seats}, {self.last_serviced}, {self.availability}")


    def __str__(self):
        Car_data = f"{self.make}, {self.model}, {self.c_num}, {str(self.rent)}, {self.color}, {self.fuelType}, {str(self.seats)}, {self.last_serviced}, {str(self.availability)}"
        return Car_data