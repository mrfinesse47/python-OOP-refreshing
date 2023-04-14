from item import Item
from phone import Phone

# Item.instanciate_from_csv()

# print(Item.all)

item1 = Item("suitcase",100,100) # creates an instance if a class
item1.name = "test" # accomplished by using setter

# item1.__name = "test" # will fail

print(item1)

