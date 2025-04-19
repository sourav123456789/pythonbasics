class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def car_details(self):
        return "car name is " + self.__model + " " + "car brand is " + self.__brand

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
        return "battery :" + self.battery_size

    def fuel_type(self):
        return "Fuel is not required."


my_car = Car("Toyota", "Innova")
print(my_car.car_details())
print(my_car.fuel_type())
my_car1 = Car("Toyota", "Innova")
print(Car.total_car)
print("---------------------------------------")
my_electric_car = ElectricCar("100W", "TATA", "nano")
print(my_electric_car.car_details())
print(my_electric_car.fuel_type())
print("car description is: " + Car.car_description())
print(isinstance(my_electric_car, Car))
print(isinstance(my_electric_car, ElectricCar))


class Battery:
    def __init__(self , battery_type , battery_power):
        self.batteryType = battery_type
        self.battery_power = battery_power


    def battery_info(self):
        print("This is battery info")


class Engine:
    def engine_info(self):
        print("This is engine info")


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "model s")

print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())