def add(*args):
    sum = 0

    for n in args:
        sum += n

    return sum

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make=50, model=40)

print(my_car.make)