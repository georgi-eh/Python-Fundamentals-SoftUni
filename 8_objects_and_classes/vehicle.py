class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if self.owner == None:
            if money >= self.price:
                change = money - self.price
                self.owner = owner
                return f"Successfully bought a {self.type}. Change: {change:.2f}"
            else:
                return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner == None:
            return "Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner == None:
            return f"{self.model} {self.type} is on sale: {self.price}"
        return f"{self.model} {self.type} is owned by: {self.owner}"
