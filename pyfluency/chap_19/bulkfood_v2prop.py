def quantity(storage_name):
    def get_weight(instance):
        return instance.__dict__[storage_name]

    
    def set_weight(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(get_weight, set_weight)


class LineItem:

    weight = quantity("weight")
    price = quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price