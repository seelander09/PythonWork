class product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
        # if self.status = 'defective'
        #     self.price = 0:
        # if self.status = 'in box'
        #     self.status = 'forsale'

    def sell(self):
        self.status = 'sold'
        print('Status: ' + str(self.status))
        return self

    def addTax(self):
        self.price += .25
        print('Price after tax: ' + str(self.price))
        return self

    def returnItem(self, reason):
        print('Status: ' + str(self.status))


product1 = product(100, 'cheese', 20, 'brand', 'for sale')

print(product1.sell().addTax())
