class Car:
    def __init__(self, brand, speed = 0):
        self.car_brand = brand
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

class Ferrari(Car): # en vez de tener una init function, lo que hace es ir a la funcion init de Car
    def make_cabrio(self):#specialization, is only in ferraris
        self.speed = 20
        self.music = "loud"
        return "Wow"


mycar = Car("Renault")
yourcar = Ferrari("Ferrari") #----> calls init method in Car
print(yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)

print(yourcar.make_cabrio(), "and music is", yourcar.music, "and speed is", yourcar.speed)