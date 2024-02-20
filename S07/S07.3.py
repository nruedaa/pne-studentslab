class Car:
    def __init__(self, brand, speed = 0):
        self.car_brand = brand
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

class Ferrari(Car): # en vez de tener una init function, lo que hace es ir a la funcion init de Car
    def __init__(self):
        #We need to call the init of the mother class Car para asi tener la informacion de speed y de brand
        super().__init__("Ferrari") #la funcion super llama a la funcion init de arriba para obtener esa informacion a la que vamos a printear debajo
        self.music = "Classic"
    def make_cabrio(self):#specialization, is only in ferraris
        self.speed = 20
        self.music = "loud"
        return "Wow"


mycar = Car("Renault")
yourcar = Ferrari() #----> calls init method in FERRARI
print(yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)

print(yourcar.make_cabrio(), "and music is", yourcar.music, "and speed is", yourcar.speed)
