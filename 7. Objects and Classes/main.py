# class has data attributes and methds
# we then craete isntance of it

class Car:
    speed = 110

    def __init__(self, make, model, color, speed = 0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, acceleration):
        if self.speed + self.acceleration <= Car.speed:
            self.speed += self.acceleration
        else:
            self.speed = Car.speed

    def get_speed(self):
        return self.speed

car1 = Car("Toyota","Innova","Red")
car1 = Car("Tata","corrola","blue")

car1.accelerate(29)

print(f"{car1.make} {car1.model} is currently at {car1.get_speed} per hour")


        
