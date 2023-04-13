class Item:
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

item1 = Item( "phone",100,100) # creates an instance if a class

# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("wallet",1000,6) # creates an instance if a class

# print(item2.calculate_total_price(item2.price, item2.quantity))


print(item1.calculate_total_price(), item2.calculate_total_price())