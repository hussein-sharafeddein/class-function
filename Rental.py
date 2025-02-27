Class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Rental Price Per Day: {self.__rental_price_per_day}")

    def calculate_rental_cost(self, days):
        return self.__rental_price_per_day * days

    def set_rental_price_per_day(self, price):
        self.__rental_price_per_day = price

    def get_rental_price_per_day(self):
        return self.__rental_price_per_day