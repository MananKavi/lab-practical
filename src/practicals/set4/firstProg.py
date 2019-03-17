from abc import ABC, abstractclassmethod


class Car(ABC):

    @abstractclassmethod
    def set_color(self, color):
        pass

    @abstractclassmethod
    def set_price(self, price):
        pass


class Maruti(Car):
    def set_color(self, color):
        self.color = color
        print("color =", self.color)

    def set_price(self, price):
        self.price = price
        print("price =", self.price, "Lacs")


class Santro(Car):
    def set_color(self, color):
        self.color = color
        print("color =", self.color)

    def set_price(self, price):
        self.price = price
        print("price =", self.price, "Lacs")


c = Maruti()
print("This is Maruti class ")
c.set_color("Blue")
c.set_price(14)
c = Santro()
print("\nThis is Santro class")
c.set_color("Red")
c.set_price(12.7)
