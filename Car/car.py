class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = '15%'
        else:
            self.tax = '12%'

    def display_all(self):
        print('Price: ' + str(self.price) + '  Speed: ' + str(self.speed) + '  Fuel: ' +
              self.fuel + '  Mileage: ' + str(self.mileage) + '  Tax: ' + self.tax)
        return self


car1 = car(1000, 100, 'full', 10000)
car2 = car(9800, 100, 'full', 30000)
car3 = car(2291, 100, 'full', 50000)
car4 = car(125, 100, 'full', 70000)
car5 = car(5000, 100, 'full', 90000)
car6 = car(10000, 100, 'full', 100000)

print(car1.display_all())
print(car2.display_all())
print(car3.display_all())
print(car4.display_all())
print(car5.display_all())
print(car6.display_all())
