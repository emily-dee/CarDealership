class Vehicle:

    def __init__(self, make: str, miles: float, price: float):
        self.make = make
        self.miles = miles
        self.price = price
        engine_on = False

    def start_engine(self):
        print("Starting engine...")
        engine_on = True

    def make_noise(self):
        print("Beep beep")

    def get_info(self) -> str:
        vehicle_info = f"Make: {self.make}, Miles: {self.miles}, Price: ${self.price}"
        return vehicle_info


class Truck(Vehicle):

    def __init__(self, make: str, miles: float, price: float):
        super().__init__(make, miles, price)
        cargo = False

    def load_cargo(self):
        print("Loading the truck bed...")
        cargo = True


class Motorcycle(Vehicle):

    def __init__(self, make: str, miles: float, price: float, top_speed: float):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("Vroom vroom!")

    def get_info(self) -> str:
        vehicle_info = f"Make: {self.make}, Miles: {self.miles}, Price: ${self.price}, Top Speed: {self.top_speed}"
        return vehicle_info
