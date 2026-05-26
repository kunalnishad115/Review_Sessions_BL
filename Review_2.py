## Task 1 - Create the decorator who calculate the mathmatical operations 


def decorator(func):
  def wrapper(*args):
    print("calculation")
    return func(*args)
  return wrapper

@decorator
def add(a,b):
  return a+b

@decorator
def sub(a,b):
  return a-b

@decorator
def avg(a,b):
  return (a+b)/2



print(add(2,3))
print(sub(2,3))
print(avg(2,3))


## Task 2 -
# kunal->Task 1 – E‑commerce Product Catalog
# Scenario
# Design an e‑commerce product catalog that supports multiple product types (e.g., Book, Electronics, Clothing) with different behavior and discount logic.
# OOP‑Covered
# Classes, objects, inheritance, polymorphism, abstraction, encapsulation
# Instructions
# Create an abstract base class Product with attributes like id, name, price and a method getFinalPrice().
# Create derived classes Book, Electronics, Clothing which implement getFinalPrice() with their own logic (e.g., books: 10% discount, electronics: 5% discount, clothing: no discount).
# In main:
# Create a list of Product objects with mixed types.
# Demonstrate polymorphism by calling getFinalPrice() on them without down‑casing.
# Add validation inside setters (e.g., price > 0).


from abc import ABC, abstractmethod

class Product(ABC):
  def __init__(self,id ,name , price):
    self.id=id
    self.name=name
    self.price=price

  @property
  def price(self):
    return self._price
  
  @price.setter
  def price(self, value):
    if value <= 0:
      raise ValueError("Price must be greater than 0.")
    self._price = value

  @abstractmethod
  def getFinalPrice(self):
    pass


class Book(Product):
  def getFinalPrice(self):
    return self.price*0.90
  
class Electronics(Product):
  def getFinalPrice(self):
    return self.price*0.95
  
class Clothing(Product):
  def getFinalPrice(self):
    return super().price
  

obj1=Book(1,'Book',100)
obj2=Electronics(2,'Electronics',200)
obj3=Clothing(3,'Clothing',300)

products_list=[obj1,obj2,obj3]

for p in products_list:
  print("Price after discount: ",p.getFinalPrice())


