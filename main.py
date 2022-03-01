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


# # # WEEK 5 CH5-CH7 FAILED ATTEMPT #1:
# class Animal():
#   def __init__(self,lifespan,name,kingdom,blood_type,limbs,habitat):
#     self.lifespan = 0
#     self.name = ""
#     self.kingdom = "" # I am thinking of biological 'classes', but I don't want to confuse myself
#     self.blood_type = ""
#     self.limbs = 0
#     self.habitat = ""
    
# dog = Animal(12,"Canis","Mammalia","warm-blooded",4,"land")

# lizard = Animal(30,"Lacertilia","Reptilia","cold-blooded",4,"land")

# whale = Animal(100,"Cetacea","Mammalia","warm-blooded",2,"water")

# crab = Animal(3,"Callinectes","Crustacea","cold-blooded",10,"water")
# dog = Animal()
# lizard = Animal()
# whale = Animal()
# crab = Animal()
#  ###################################################-------------------------------------###########################################

# # # WEEK 5 CH5-CH7 FAILED ATTEMPT #2:
# class Animal():
#   def __init__(self):
#     self.lifespan = lifespan
#     self.name = name
#     self.kingdom = kingdom   # Not scientifically accurate
#     self.blood_type = blood_type
#     self.limbs = limbs
#     self.habitat = habitat
#     self.magic_num = magic_num

#   def print_name(self):
#     print(self.name)
    
# dog = Animal()
# whale = Animal()

# dog.name = "Canis"
# whale.name = "Cetacea"

# dog.print_name()
# whale.print_name()
# print(lizard.name)
# print(crab.name)

# # # WEEK 5 CH8-CH14:

# class Animal():
#   def __init__(self,lifespan,name,kingdom,blood_type,limbs,habitat,magic_num):
#     self.lifespan = lifespan
#     self.name = name
#     self.kingdom = kingdom   # Not scientifically accurate
#     self.blood_type = blood_type
#     self.limbs = limbs
#     self.habitat = habitat
#     self.magic_num = magic_num

#   def print_all(self):
#     print(self.lifespan,self.name,self.kingdom,self.blood_type,self.limbs,self.habitat,self.magic_num) 


# dog = Animal(12,"Canis","Mammalia","warm-blooded",4,"land",94)

# lizard = Animal(30,"Lacertilia","Reptilia","cold-blooded",4,"land",1.5)

# whale = Animal(100,"Cetacea","Mammalia","warm-blooded",2,"water",3)

# crab = Animal(3,"Callinectes","Crustacea","cold-blooded",10,"water",-9)

# animals = [dog, lizard, whale, crab]

# print(dog.habitat)

# for a in animals:
#   print(a.lifespan)

# for a in animals:
#   print(a.magic_num)


# total = 0 
# for a in animals:
#   total = a.magic_num + total
# magic_average = total / len(animals)

# print(magic_average)

# print(dog.print_all())

# print(lizard.print_all())

# # # # WEEK 5 CH15:
# ask = True

# while ask == True:
#   user_number = input("Enter a number.")
#   if user_number.isnumeric():
#     ask = False
#   else:
#     print("Try again.")

# bunny = Animal(7,"Oryctolagus","Mammalia","warm-blooded",4,"land",magic_num = user_number)

# print(bunny.print_all())

# # WEEK 5 CH16:
# class SKU():
#   def __init__(self,part_number,color,price,make,model,grade):
#     self.part_number = part_number
#     self.color = color
#     self.price = price
#     self.make = make
#     self.model = model
#     self.grade = grade

#   def print_stats(self):
#     print(self.part_number,self.color,self.price,self.make,self.model,self.grade
    
# #confused about Challenge # 17

# ring = SKU("RIN123","puce",25000,"VanCleef","Etoile","18k")
# television = SKU("TEL158","puce",589.98,"Sony","4KCoolness","New")
# stuffed_animal = SKU("CUTE459","puce",19.99,"Squishmallows","Wildlife Series","New")
# bowl = SKU("BOWL47","puce",350,"L'Objet","Eternity","Malachite","Vintage")
# potted_plant = SKU("TREE83","puce",4850,"Takahashi Bonsai","Miyoko-Cedar","Matured")
# lotion = SKU("NIV783","puce",12.99,"Nivea","Tropical","New")
# lip_balm = SKU("EOS001","puce",3.99,"EOS","Toasted Marshmallow-Sphere","New")
# water = SKU("WAT901","puce",5,"Boxed Water","Unflavored","New")
# shoes = SKU("SHU102","puce",150,"Casadei","Blade Runner","Used")
# fountain_pen = SKU("WRI535","puce",75,"Kaweco","Sport Plus","Steel","Used")

# # WEEK 5 CH18 & 19:
# skus = [ring,television,stuffed_animal,bowl,potted_plant,lotion,lip_balm,water,shoes,fountain_pen]

# print(skus)

# print(lotion.print_stats())

# # WEEK 5 CH20 - INCOMPLETE:
# colors = ["void", "infrared", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "ultraviolet"]

# # WEEK 5 CH21:

ask = True

while ask == True:
  number = input("Enter an integer, or 'x' to stop. ")
  if number.isdigit():
    number = int(number)
    if number == 0:
      print("Try a higher number.")
    if number > 0 and number < 101:
      for r in range(100, number, -1):
        print(r)
      for r in range(number,-1,-1):
        print(r)
    if number >= 101:
      print("Try again.")
  elif number == "x" or number == "X":
    ask = False
  else:
    print("Try again")

# # WEEK 5 CH22:

list = [1,3,5,6,8,9,10,14,16,18, 22,24,25,26,28,30,31,32,45,46,67,70,71,72,73,74,75,88]

print(list)
print(len(list))

midpoint = int(len(list) / 2)
endpoint = len(list)
print(midpoint)
print(list[midpoint])

first_half = list[0 : midpoint+1]
print(first_half)
second_half = list[midpoint+1 : endpoint]
print(second_half)

print(first_half + second_half)
# second_half = range(list[midpoint+1],list[-1]) --> prints actual range.

# # WEEK 5 CH23:


