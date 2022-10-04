class Product:
    def __init__(self, name,  amout, price):
        self.amout = amout
        self.price = price
        self.name = name

    def get_price(self, n):
            if n < 10 :
                return (self.price)
            if n>=10 and n<100:
                return (self.price*0.9)
            if n>=100:
                return (self.price*0.8)
    
    def make_purchase(self,m):
        if m < self.amout:
            self.amout -= m
            return (self.get_price(m) * m)

total = 0
orange= Product('orange', 16, 700)
cherry = Product('cherry', 25, 1100)
apple = Product('apple', 32, 600)
potato= Product('potato', 83,200)
print(orange.make_purchase(12))


