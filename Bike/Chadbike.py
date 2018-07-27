class Chadbike():
    def __init__(self, price, max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed

    def displayinfo(self):
        print("Price is " + self.price)
        print("Speed is " + self.max_speed)
        print(self.miles)
        return self

    def ride(self):
        print("Riding...")
        self.miles = self.miles * 10
        return self

    def reverse(self):
        print("Reversing...")
        if (self.miles >= 5):
            self.miles -= 5  # depending on input miles could end up negative
        return self


Chadbike("$100", "85mph").ride().ride().ride().reverse().displayinfo()
Chadbike("$50", "30mph").ride().ride().reverse().reverse().displayinfo()
Chadbike("$15", "100mph").reverse().reverse().reverse().displayinfo()
