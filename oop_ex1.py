

# create a laptop class with attributes like brand, model name and price 
# create two objects/instance of your laptop 


class Laptop:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + ' ' + model_name  # we can create more instances irrespective of attributes 
    def apply_discount(self,discount):
        off_price =  self.price*(discount/100)
        discounted_price = self.price - off_price
        return discounted_price



laptop_1 = Laptop('hp', 't800', 34000)
laptop_2 = Laptop('Dell','Alienware',100000)

# print(laptop_1)  # create a object
# print(laptop_1.name)
# print(laptop_2.price)``
# print(laptop_1.laptop_name)
# print(laptop_1.apply_discount(40))











# def get_total(x,y):
#     return x + y

# print(get_total(2,4))



# ENCAPSULATION
class Calculator:               # PROPERTIES AND FUNCTIONALITY TOGETHER 
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        print(self.x+self.y)
    def sub(self):
        print(self.x-self.y)
    def mul(self):
        print(self.x*self.y)
    def div(self):
        print(self.x/self.y)



calc = Calculator(2,5)
# print(calc.x)
# print(calc.y)
# calc.add()
# calc.sub()
# calc.mul()
# calc.div()



# Piggy bank
class Piggy:
    value = 0
    def addMoney(self,amount):
        self.value = self.value + amount
        print(self.value)

myPiggy = Piggy()
# myPiggy.addMoney(100)
# print(myPiggy.value)



# class Dog:
#     hungry = True 
#     def eat(self):
#         self.hungry = False

# dog = Dog()
# dog.eat()
# print(dog.hungry)



# eyes = green 
# age =7

class Parents:              # INHERITANCE--> PROPERTIES AND FUNCTIONALITY FROM ANOTHER CLASS WITH ITS OWN ALSO
    def __init__(self):
        self.eyes = "green"
class Child(Parents):
    def __init__(self):
        super().__init__()
        self.age = 7

child = Child()
# print(child.age)
# print(child.eyes)



class Greetings:
    def greet(self):
        print("Hi!")
class Person(Greetings):
    name = "George"

p = Person()
# print(p.name)
# p.greet()



# def getArea(b,h):
#     print (b*h)

# base = 3
# height = 4 

# getArea(3,4)

class Rectangle:
    base = 3 
    height = 4
    def getArea(self):
        return self.base*self.height

rect = Rectangle()
# print(rect.getArea())



# INHERITANCE
class Car:                                     
    def start_car(self):
        print("Starting the Car")
class Gas(Car):                         # inherit property of Car class # it will use method from car
    def fuel(self):
        print("Uses Petrol")
class Electric(Car):
    def fuel(self):
        print("uses Electricity")
class Hybrid(Car):
    def fuel(self):
        print("uses electricity and fuel")

# g = Gas()
# g.start_car()
# g.fuel()
# e = Electric()
# e.start_car()
# e.fuel()
# h = Hybrid()
# h.start_car()
# h.fuel()




class RedCar():
    def drive(self):
        print("Vroom!")
    def brake(self):
        print("Breaking...!")
class BlueCar(RedCar):
    def reverse(self):
        print("Reversing...!")

# b = BlueCar()
# b.drive()
# b.brake()
# b.reverse()



class Circle:
    pi = 3.14
    def area(self,radius):
        return self.pi*radius**2

c = Circle()
print(c.area(2))
