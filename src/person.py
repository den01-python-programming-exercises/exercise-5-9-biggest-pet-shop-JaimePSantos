# from pet import Pet

class Person:

    def __init__(self,name,pet):
        self.name = name
        self.pet = pet

    # implement the __str__ method here
    def __str__(self):
      return "%s, has a friend called %s (%s)"%(self.name,self.pet.name,self.pet.breed)

if __name__ == 'main':
  from pet import Pet
else:
  from src.pet import Pet