# # WEEK 5 CH1:

# class Animal():
#   pass #placeholder for future methods/attributes

# # WEEK 5 CH2:
# class Animal():
#   dog = Animal()
#   lizard = Animal()
#   whale = Animal()
#   crab = Animal()
#   d = "doggo"
#   l = 24
#   is_whale = True
#   crabby = 5.8
  

# # WEEK 5 CH3:
# print(type(Animal.dog))
# print(type(Animal.lizard))
# print(type(Animal.whale))

# # WEEK 5 CH4:

# print(type(Animal.d))
# print(type(Animal.l))
# print(type(Animal.is_whale))
# print(type(Animal.crabby))


# # WEEK 5 CH5-CH7:
# class Animal():
#   def __init__(self,lifespan,name,kingdom,blood_type,limbs,habitat):
#     self.lifespan = 0
#     self.name = ""
#     self.kindgom = "" # I am thinking of biological 'classes', but I don't want to confuse myself
#     self.blood_type = ""
#     self.limbs = 0
#     self.habitat = ""
    
# dog = Animal(12,"Canis","Mammalia","warm-blooded",4,"land")

# lizard = Animal(30,"Lacertilia","Repltilia","cold-blooded",4,"land")

# whale = Animal(100,"Cetacea","Mammalia","warm-blooded",2,"water")

# crab = Animal(3,"Callinectes","Crustacea","cold-blooded",10,"water")
# # dog = Animal()
# # lizard = Animal()
# # whale = Animal()
# # crab = Animal()
#  ###################################################-------------------------------------###########################################

# WEEK 5 CH5-CH7:
class Animal():
  lifespan = 0
  # name = ""
  kindgom = "" 
  # Not scientifically accurate
  blood_type = ""
  limbs = 0
  habitat = ""
  
  def __init__(self):
    self.name = ""

  def print_name(self):
    print(self.name)
    
dog = Animal()
whale = Animal()

dog.name = "Canis"
whale.name = "Cetacea"

dog.print_name()
whale.print_name()