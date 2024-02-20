class Car:
    def __init__(self, brand, speed = 0): #method called for the first time, we must have it (it converts the class to an object)
        self.car_brand = brand
        self.speed = speed
        self.value = 0
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):#when we have a method, the first parameter inside has to be self
        return self.speed

    def get_brand_nationality(self):
        if self.car_brand == "Renault":
            return "France"
        elif self.car_brand == "Ferrari":
            return "Italy"
    def set_age(self, age):
        self.age = age

    def set_value(self, value):
        self.value = value

mycar = Car("Renault", 30)
print(mycar.get_speed())
mycar.set_speed(80) #we dont need to put mycar.speed(mycar), because it is implied when we wrote self, so doing mycar.smthg, makes it talk about the object itself
print(mycar.get_speed())
print(mycar.get_brand_nationality())
yourcar = Car("Ferrari", 250) #we can call the same class several times
print(yourcar.speed) #this line and the next one are the same
print(yourcar.get_speed())
