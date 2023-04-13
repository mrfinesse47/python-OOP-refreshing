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

    def __repr__(self):# used to represent object, similar to str
        return f'("{self.name}", {self.price}, {self.quantity})'



item1 = Item("phone",100,100) 
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",88,3)
item4 = Item("Mouse",10,5)
item5 = Item("Keyboard",1,9)

# for instance in Item.all:
#     print(instance.name)

print(Item.all)