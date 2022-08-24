class SuperMarket(object):
    """docstring for SuperMarket."""

    def __init__(self,name,price,discount):
        self.name=name
        self.price=price
        self.discount=discount

product1=SuperMarket('Soap',20,4)
product2=SuperMarket('Sap',56,2)

print(product1.name)
