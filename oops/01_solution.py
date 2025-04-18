class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def car_details(self):
        return "car name is " + self.model + " "+ "car brand is " + self.__brand

    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "Petrol or diesel"

#     creating a static method
    @staticmethod
    def car_description():
        return "Cars are the mode of Transport"


class ElectricCar(Car):

    def __init__(self, battery_size, brand, model):
        super().__init__(brand, model)
        self.battery_size = battery_size


    def car_details(self):
        return "car name is " + self.model + " " + " " + "battery :" + self.battery_size

    def fuel_type(self):
        return "Fuel is not required."



my_car = Car("Toyota", "Innova")
print(my_car.car_details())
print(my_car.fuel_type())
my_car1 = Car("Toyota", "Innova")
print(Car.total_car)
print("---------------------------------------")
my_electric_car = ElectricCar("100W" , "TATA" , "nano" )
print(my_electric_car.car_details())
print(my_electric_car.fuel_type())
print("car description is: " + Car.car_description())
