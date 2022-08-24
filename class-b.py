class SuperMarket(object):


    def __init__(self, name,price,discount):

        self.name = name
        self.price = price
        self.discount = discount
    def product_details(self):
        return self.name, self.price, self.discount

product1= SuperMarket('Soap',10,5)
product2 = SuperMarket('Oil',60,5)

print(product1.product_details())
print(product2.product_details())
print(SuperMarket.product_details(product1))
