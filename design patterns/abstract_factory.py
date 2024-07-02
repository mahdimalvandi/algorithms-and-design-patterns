from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def create_suv(self): ...

    @abstractmethod
    def create_coupe(self): ...


class Benz(Car):
    def create_suv(self):
        return Gla()

    def create_coupe(self):
        return Cls()


class Bmw(Car):
    def create_suv(self):
        return X1()

    def create_coupe(self):
        return M2()


class Gla:
    def run(self):
        print('running Benz suv : gla')


class X1:
    def run(self):
        print('running Bmw suv : x1')


class Cls:
    def run(self):
        print('running Benz coupe : cls')


class M2:
    def run(self):
        print('running Bmw coupe : m2')


brands = {
        'bmw': Bmw,
        "benz": Benz
}

def make_suv(brand):
    result = brands[brand]().create_suv()
    result.run()


def make_coupe(brand):
    result = brands[brand]().create_coupe()
    result.run()


models = {
    'x1': ["bmw", make_suv],
    'm2': ["bmw", make_coupe],
    'cls': ["benz", make_coupe],
    'gla': ["benz", make_suv],
}

def client(model):
    models[model][1](models[model][0])

client(input('Enter'))