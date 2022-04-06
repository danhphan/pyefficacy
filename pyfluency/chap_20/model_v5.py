import abc

class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        self.storage_name = '{}#{}'.format(cls, cls.__counter)
        cls.__counter += 1


    def __get__(self, instance, owner):
        if isinstance is None:
            return self
        else:
            return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        pass

class Validated(AutoStorage):
    def __set__(self, instance, value):
        self.validate(instance, value)

    def validate(self, instance, value):
        pass


class Quantity(Validated):
    def validate(self, instance, value):
        pass