from .item import Item

class Phone(Item):


    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):

        # call to super to access parent
        super().__init__(
            name,price,quantity
            )

        assert broken_phones >= 0, f"broken phones {broken_phones} is not greater than 0!"

        # assign to self object
        self.broken_phones = broken_phones
    

