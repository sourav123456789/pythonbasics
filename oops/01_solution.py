class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def car_details(self):
        return "car name is " + self.model + " "+ "car brand is " + self.__brand

    def get_brand(self):
        return self.__brand

class ElectricCar(Car):

    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size


    def car_details(self):
        return "car name is " + self.model + " "+ "car brand is " + self.__brand +" " + "battery :" + self.battery_size



my_car = Car("Toyota", "Innova")
print(my_car.car_details())

my_electric_car = ElectricCar("100W" , "TATA" , "nano" )
print(my_electric_car.car_details())
