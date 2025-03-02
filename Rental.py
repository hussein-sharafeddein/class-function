class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

        #Added display_info method to display the information of the vehicle
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Rental Price Per Day: {self.__rental_price_per_day}$/day")

    def calculate_rental_cost(self, days):
        return self.__rental_price_per_day * days

        #Added setter method for rental_price_per_day
    def set_rental_price_per_day(self, price):
        self.__rental_price_per_day = price

        #Added getter method for rental_price_per_day
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seat_capacity): #Added additional attribute: seating_capacity for Car class
        self.seat_capacity = seat_capacity
        super().__init__(brand, model, year, rental_price_per_day)

        #Overriding the display_info method to display the information of the car
    def display_info(self):
        super().display_info()
        print(f"Seating Capacity: {self.seat_capacity}")

class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity): #Added additional attribute: engine_capacity for Bike class
        self.engine_capacity = engine_capacity
        super().__init__(brand, model, year, rental_price_per_day)

        #Overriding the display_info method to display the information of the bike
    def display_info(self):
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity}cc")


#Demonstrating polymorphism.
def show_vehicle_info(vehicle):
    vehicle.display_info()

#Creating instances of Car and Bike classes
car1 = Car("Toyota", "Corolla", 2020, 50, 5)
bike1 = Bike("Yamaha", "R1", 2019, 30, 998)

#Calling the show_vehicle_info function to display the information of the car and bike
show_vehicle_info(car1)
print("=====================")
show_vehicle_info(bike1)
print("=====================")