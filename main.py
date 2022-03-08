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

# # # WEEK 5 CH16:
# class SKU():
#   def __init__(self,part_number,make,color="",price=0,model="",grade=""):
#     self.part_number = part_number
#     self.color = color
#     self.price = price
#     self.make = make
#     self.model = model
#     self.grade = grade

#   def print_stats(self):
#     print(self.part_number,self.color,self.price,self.make,self.model,self.grade)
    
# # confused about Challenge # 17 --> solution: set defaults for non-essential paramenters!

# ring = SKU("RIN123","VanCleef","puce",25000,"Etoile","18k")
# television = SKU("TEL158","Sony","puce",589.98,"4KCoolness","New")
# stuffed_animal = SKU("CUTE459","Squishmallows","puce",19.99,"WildlifeSeries","New")
# bowl = SKU("BOWL47","L'Objet","puce",350,"Eternity","Vintage")
# potted_plant = SKU("TREE83","Takahashi Bonsai","puce",4850,"Miyoko_Cedar","Matured")
# lotion = SKU("NIV783","Nivea","puce",12.99,"Tropical","New")
# lip_balm = SKU("EOS001","EOS","puce",3.99,"Toasted_Marshmallow_Sphere","New")
# water = SKU("WAT901","BoxedWater","puce",5,"Unflavored","New")
# shoes = SKU("SHU102","Casadei","puce",150,"Blade_Runner","Used")
# fountain_pen = SKU("WRI535","Kaweco","puce",75,"Steel","Used")


# # WEEK 5 CH18 & 19:
# skus = [ring,television,stuffed_animal,bowl,potted_plant,lotion,lip_balm,water,shoes,fountain_pen]

# # print(skus)--> prints location of the list
# for s in skus:
#   print(s.part_number) # --> "name" variable was not declared, so use what you *did* declare

# print(lotion.print_stats())

# # # WEEK 5 CH20:
# colors = ["void", "infrared", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "ultraviolet"]

# import random

# for sku in skus:
#   sku.color = random.choice(colors)
#   print(sku.color)
  
# # # WEEK 5 CH21:'

# '''NOT RECURSIVE'''
# ask = True

# while ask == True:
#   number = input("Enter an integer, or 'x' to stop. ")
#   if number.isdigit():
#     number = int(number)
#     if number == 0:
#       print("Try a higher number. ")
#     if number > 0 and number < 101:
#       for r in range(100, number, -1):
#         print(r)
#       for r in range(number,-1,-1):
#         print(r)
#     if number >= 101:
#       print("Try again. ")
#   elif number == "x" or number == "X":
#     ask = False
#   else:
#     print("Try again. ")

# '''RECURSIVE,UNBOUND'''
# def print_all(num):
#   if num == 0:
#     print(num) # to include 0 in the print
#     return
#   print(num)
#   print_all(num-1)

# num = int(input("Enter an integer. "))
# print_all(num)

# # # WEEK 5 CH22:

# list = [1,3,5,6,8,9,10,14,16,18, 22,24,25,26,28,30,31,32,45,46,67,70,71,72,73,74,75,88]

# print(list)
# print(len(list))

# midpoint = int(len(list) / 2)
# endpoint = len(list) #no need to create an endpoint variable
# print(midpoint)
# print(list[midpoint])

# first_half = list[0 : midpoint+1]
# print(first_half)
# second_half = list[midpoint+1 : endpoint]
# print(second_half)

# print(first_half + second_half)
# # second_half = range(list[midpoint+1],list[-1]) --> actual range, NOT corresponding list

# # WEEK 5 CH23:

list = [1,3,5,6,8,9,10,14,16,18,22,24,25,26,28,30,31,32,45,46,67,70,71,72,73,74,75,88]

def find_number(list,target):
  midpoint = len(list)//2
  if list[midpoint] == target:
    return True 
  elif target < list[midpoint]:
    return find_number(list[:midpoint],target)
  elif target > list[midpoint]:
    return find_number(list[midpoint+1:],target)
  else:
    return False
    

print(find_number(list,74))
print(find_number(list,3))
print(find_number(list,22))
print(find_number(list,88))

# # WEEK 5 CH24:

try: 
  find_number(list,81)
except IndexError: 
  print("False")


class Artist():
  def __init__(self,name,genre,best_song_ever = "",total_sales = 0, record_label = ""):
    self.name = name
    self.genre = genre
    self.best_song_ever = best_song_ever
    self.total_sales = total_sales
    self.record_label = record_label

  def print_genre(genre):
    for art in artists:
      if art.genre == genre:
        print(self.name,self.genre)
  # WRONG def print_genre(self,genre):
  #   for art in Artists():
  #     if art.genre == genre: <--- Do not do this
  #       print(self.name,self.genre)

Ella = Artist("Ella Fitzgerald","jazz","Dream a Little Dream",10000,"Vintage Records")
Frank = Artist("Frank Sinatra","jazz","Mac the Knife",10002,"Ravioli Records")
Onika = Artist("Nicki M.","hip-hop","Anaconda",200000,"Barbie and Ken Records")
BOC = Artist("Blue Oyster Cult","rock","Don't Fear The Reaper",50000,"Starlight Records")
Pisk = Artist("P!sK","electro swing","Black Coffee",60053,"Vintage Records")
Britney = Artist("Britney Jean Spears","pop","Piece of Me",7002580,"Futura Records")
Bey = Artist("Beyonce","hip-hop","Single Ladies",15300058,"Park Ivy Records")    
Dre = Artist("Dr. Dre","rap","Keep Their Heads Ringing",200052, "Death Row Records")
Apa = Artist("Apashe","alternative","No Twerk",20000,"Indie Records")
MsGraves = Artist("Denyce Graves","opera","Samson et Dalila, Act 2",30008,"Libre Records")
Johnny = Artist("Johnny Clarke","rasta","Declaration of Rights",56000,"Irie Records")
Persona = Artist("Some Japanese Person","jazz","Layer Cake",15000,"Persona Five")
Rosetta = Artist("Sister Rosetta Tharpe","blues","Didn't It Rain?",10000,"Oldtimer Records")
Fela = Artist("Fela Kuti","jazz","O.D.O.O",90100,"Wahala Records")

artists = [Ella, Frank, Onika, BOC, Pisk, Britney, Bey, Dre, Apa, MsGraves, Johnny, Persona, Rosetta, Fela]

def print_genre(genre):
  for art in artists:
    if art.genre == genre:
      print(art.name)

print_genre("jazz")

