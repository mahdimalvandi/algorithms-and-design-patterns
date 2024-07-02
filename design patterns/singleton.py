class SingletonMetaClass(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class Test(metaclass=SingletonMetaClass):
    def __init__(self, name):
        self.name = name

    def moving(self):
        """test method"""
        print("moving "+self.name)

