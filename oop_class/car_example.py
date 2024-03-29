class Car:
  
  def __init__(self, name, age,color,model):
    self.name = name
    self.age = age
    self.color=color
    self.model=model

  def price_car(model,age):
    if age>2:
      return 500
    elif age >0 and age <2:
      return 1500



mycar=Car('BMW',2,'White','X4')
old_car=Car('PK',45,'Gray','1350')

print(mycar.name)
print(old_car.name)










  # def myfunc(self):
  #   print("Hello my name is " + self.name)

















# p1 = Car("BMW", 36)
# p1.myfunc()
# print(p1.name)
# print(p1.age)

# p1.age = 40

# del p1.age
# del p1