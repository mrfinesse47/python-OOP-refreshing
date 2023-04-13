class Item:
    pay_rate = 0.8 # after 20% discount -- class attribute

    def __init__(self,name:str,price:float,quantity:int=0):
        #run validations on recieved arguments
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"


        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate  # can over ride pay rate this way
        #self.price = self.price * Item.pay_rate

item1 = Item( "phone",100,100) # creates an instance if a class

# print(item1.calculate_total_price(item1.price, item1.quantity))


# print(item2.calculate_total_price(item2.price, item2.quantity))

# print(item1.calculate_total_price(), item2.calculate_total_price())
item2 = Item("wallet",1000,6) # creates an instance if a class
item2.pay_rate = 0.00001 # a major discount for item 2, does this on instance level 

# print(Item.pay_rate) # able to access with out object instance
# print(item1.pay_rate) # able to access with object instance
# print(item2.pay_rate) # able to access with object instance

# Python tries to bring the attribute from the class level first, if it doesn't see
# it at class level it looks in instance level

# print(Item.__dict__) # returns all of the attributes of the class

item1.apply_discount()
print(item1.price)

item2.apply_discount()
print(item2.price)