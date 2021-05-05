"""
class Car:
 def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color

class Truck(Car):
    def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load
    
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name} {self.current_speed}'

mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)


#truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
truck = Truck(make="Mercedes", model_name="Actros", color="black", top_speed=90, max_load=1200)


class DieselEngine:
   def tank(self, how_many=100):
       print(f"Adding {how_many} liters of Diesel")

class PetrolEngine:
   def tank(self, how_many=20):
       print(f"Adding {how_many} liters of Petrol")

class Truck(Car, DieselEngine):

   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

class SportCar(Car, PetrolEngine):
   pass


truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)
porsche = SportCar(make="Porsche", model_name="911", color="Red", top_speed=250)
truck.tank()
porsche.tank()
"""

# import this - "przykazania :)" 


def say_hello():
   greeting = "Hello stranger!"
   return greeting
"""
def say_louder(func):
   def wrapper():
       result = func()
       return result.upper()
   return wrapper

@say_louder
def say_hello():
   greeting = "Hello stranger!"
   return greeting
"""

say_hello()