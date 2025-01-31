





class Car:                                  # blueprint for making our object i.e car_1, car_2, car_3 # for defying functionality of our object and attributes 
    def __init__(self,color,company ,model): # __init__ function inside a class is a method --->'''constructor''' # and attributes 
       # instance variable 
        self.color = color                  # self used for calling/representing the objects 
        self.company = company
        self.model = model

car_1 = Car('Red','Ford','Mustang')         # object car_1
car_2 = Car('Blue','Toyota','Prius')        # object car_2
car_3 = Car('Green','Volkswagen','Golf')    # object car_3


# print(car_1) # this will only creates a model at the specific place on memory 
# print(car_1.model)







class IntellipaatClass:
    def __init__(self,a):
        self.a = "Welcome to Intellipaat"

IntellipaatClass = IntellipaatClass(5)

print(IntellipaatClass.a)