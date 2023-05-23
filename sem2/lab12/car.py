class Car(object):

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_car(self):
        print("Автомобиль заведен")

    def stop_car(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color


car = Car("red", "crossover", 1999)
car.start_car()

car.set_color("white")
car.set_type("coupe")
car.set_year(2000)
print(car.color, car.type, car.year)

car.stop_car()
