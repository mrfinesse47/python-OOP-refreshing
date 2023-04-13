
str1 = str("4ghvgvg") # <class '__main__.Item'>

print(str1.upper()) #4GHVGVG


class Item:
    def __init__(self):
        print("I am Created")
    def calculate_total_price(self, x, y):
        return x*y

item1 = Item() # creates an instance if a class
item1.name = "phone"
item1.price = 100
item1.quantity = 4

# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item() # creates an instance if a class
item2.name = "wallet"
item2.price = 1000
item2.quantity = 2

# print(item2.calculate_total_price(item2.price, item2.quantity))



