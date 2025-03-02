Class Vehicle:
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
        print(f"Rental Price Per Day: {self.__rental_price_per_day}")

    def calculate_rental_cost(self, days):
        return self.__rental_price_per_day * days

        #Added setter method for rental_price_per_day
    def set_rental_price_per_day(self, price):
        self.__rental_price_per_day = price

        #Added getter method for rental_price_per_day
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

Class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seat_capacity): #Added additional attribute: seating_capacity for Car class
        self.seat_capacity = seat_capacity
        super().__init__(brand, model, year, rental_price_per_day)

Class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity): #Added additional attribute: engine_capacity for Bike class
        self.engine_capacity = engine_capacity
        super().__init__(brand, model, year, rental_price_per_day)