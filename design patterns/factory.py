from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, option, name):
        self.name = name
        self.option = option

    @abstractmethod
    def make(self):
        pass

    def call_make(self):
        a = self.make()
        result = a.work(self.name, self.option)
        return result

class BenzMake(Car):
    def make(self):
        return Benz()


class BmwMake(Car):
    def make(self):
        return BMW()


class Benz:
    def work(self,name, option):
        return f'benz car with name {name} with option {option}'


class BMW:
    def work(self, name, option):
        return f'bmw car with name {name} with option {option}'


def client(car, option, name):
    cars = {
        'bmw': BmwMake,
        'benz': BenzMake
    }
    result = cars[car](name=name, option=option)
    return result.call_make()


print(client("bmw", option='music', name='model 2020'))