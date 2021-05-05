class Car:
    def __init__(self, make, model_name, top_speed, color, current_speed):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color
       self.current_speed = current_speed
       # Variables
       #self._current_speed = 0
       
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name} {self.current_speed}'
 
"""
    def set_current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")
"""
class Truck(Car):
    def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load
    
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name} {self.current_speed}'

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")



car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red", current_speed=100)
car.current_speed 
print(car)

#truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
truck = Truck(make="Mercedes", model_name="Actros", color="black", top_speed=90, current_speed=60, max_load=1200)
truck.current_speed
print(truck)