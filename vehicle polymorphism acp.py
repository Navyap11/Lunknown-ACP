class BMW:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"{self.model} BMW engine started!")

    def drive(self):
        print(f"{self.model} BMW is driving smoothly.")

class Ferrari:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        print(f"{self.model} Ferrari engine roars to life!")

    def drive(self):
        print(f"{self.model} Ferrari is racing fast!")

def car_action(car):
    car.start_engine()
    car.drive()

bmw_car = BMW("X5")
ferrari_car = Ferrari("F8 Tributo")

car_action(bmw_car)
car_action(ferrari_car)