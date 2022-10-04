class Investment:
    def __init__(self, stavka, summa):
        self.stavka = stavka
        self.summa = summa
    
    def value_after(self,n):
        return self.summa + (self.stavka * 0.1)*self.summa

    def __str__(self):
        return f'Stavka is {self.stavka} and summa is {self.summa}'

deposit1 = Investment(10,2000)
print(deposit1.value_after(10))
print(deposit1)