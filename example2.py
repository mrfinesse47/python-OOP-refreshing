class Item:
    def __init__(self,name,price,quantity=0):
        print(f"an instance created for:{name}")
        self.name = name
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item( "phone",100,4) # creates an instance if a class

# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("wallet",1000,1000) # creates an instance if a class

# print(item2.calculate_total_price(item2.price, item2.quantity))


print(item1.name, item2.name)