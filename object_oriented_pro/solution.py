class Car:
    def __init__(self,userbrand , usermodel):
        self.brand = userbrand
        self.model = usermodel
    def fullname(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, userbrand, usermodel, battery_size):
        super().__init__(userbrand, usermodel)
        self.battery_size = battery_size



my_car = Car("Toyota", "Corolla")
print(my_car.brand) 
print(my_car.fullname())