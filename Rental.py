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
        print(f"Rental Price Per Day: ${self.__rental_price_per_day}/day")

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
car2 = Car("Honda", "Civic", 2018, 60, 5)
bike2 = Bike("Suzuki", "GSX-R1000", 2021, 99, 999.8)
car3 = Car("Porsche", "911", 2022, 100, 2)
bike3 = Bike("Kawasaki", "Ninja H2R", 2020, 150, 998)

#Calling the show_vehicle_info function to display the information of the vehicles
print("Vehicle Information: ")
print("=====================")
show_vehicle_info(car1)
print("=====================")
show_vehicle_info(car2)
print("=====================")
show_vehicle_info(car3)
print("=====================")
show_vehicle_info(bike1)
print("=====================")
show_vehicle_info(bike2)
print("=====================")
show_vehicle_info(bike3)
print("=====================")

#Calling the calculate_rental_cost method to calculate the rental cost of the vehicles
print("Rental Costs: ")
print("=====================")
print(f"Rental Cost for Toyota Corolla for 3 days: {car1.calculate_rental_cost(3)}$")
print("=====================")
print(f"Rental Cost for Honda Civic for 5 days: {car2.calculate_rental_cost(5)}$")
print("=====================")
print(f"Rental Cost for Porsche 911 for 2 days: {car3.calculate_rental_cost(2)}$")
print("=====================")
print(f"Rental Cost for Yamaha R1 for 5 days: {bike1.calculate_rental_cost(5)}$")
print("=====================")
print(f"Rental Cost for Suzuki GSX-R1000 for 7 days: {bike2.calculate_rental_cost(7)}$")
print("=====================")
print(f"Rental Cost for Kawasaki Ninja H2R for 4 days: {bike3.calculate_rental_cost(4)}$")
print("=====================")

#Updating the rental price per day of the vehicles using the setter method
car1.set_rental_price_per_day(55)
bike1.set_rental_price_per_day(33)
car2.set_rental_price_per_day(54)
bike2.set_rental_price_per_day(111)
car3.set_rental_price_per_day(125)
bike3.set_rental_price_per_day(133)

#Displaying the updated rental price per day of the vehicles using the getter method
print("Updated Rental Prices Per Day:")
print("=====================")
print(f"Updated Rental Price Per Day for Toyota Corolla: ${car1.get_rental_price_per_day()}/day")
print("=====================")
print(f"Updated Rental Price Per Day for Honda Civic: ${car2.get_rental_price_per_day()}/day")
print("=====================")
print(f"Updated Rental Price Per Day for Porsche 911: ${car3.get_rental_price_per_day()}/day")
print("=====================")
print(f"Updated Rental Price Per Day for Yamaha R1: ${bike1.get_rental_price_per_day()}/day")
print("=====================")
print(f"Updated Rental Price Per Day for Suzuki GSX-R1000: ${bike2.get_rental_price_per_day()}/day")
print("=====================")
print(f"Updated Rental Price Per Day for Kawasaki Ninja H2R: ${bike3.get_rental_price_per_day()}/day")
print("=====================")