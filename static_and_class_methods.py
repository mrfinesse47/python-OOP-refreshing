import csv

class Item:
    pay_rate = 0.8 # -- class attribute
    all = [] # useful to keep track of all instances

    def __init__(self,name:str,price:float,quantity:int=0):

        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate  # can over ride pay rate this way

    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv','r') as f:
             reader = csv.DictReader(f)
             items = list(reader)
        for item in items:
            print("item:",item)
            Item(
                name=item.get('name'),
                price= float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            #considers 0.00 or 10.000
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False





    def __repr__(self):# used to represent object, similar to str
        return f'("{self.name}", {self.price}, {self.quantity})'




Item.instanciate_from_csv()

print(Item.is_integer(67))
print(Item.is_integer(7))
print(Item.is_integer("hi"))