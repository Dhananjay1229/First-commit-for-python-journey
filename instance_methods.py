


class Car:
    def __init__(self,color,company,model):
        self.color = color
        self.company = company
        self.model = model

    def full_disc(self):
        return f"{self.company} {self.model}"

    def liked(self):
        return self.color == 'Green'

    
car_1 = Car('Red','Ford','Mustang')         # object car_1
car_2 = Car('Blue','Toyota','Prius')        # object car_2
car_3 = Car('Green','Volkswagen','Golf') 

# print(car_1.full_disc())
# print(Car.full_disc(car_2))

# print(Car.liked(car_3))
print(car_3.liked())