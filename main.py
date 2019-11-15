print('You are in my pet store')

#Function
def feed(pet):
  #Condition
  if pet['hungry'] == True:
    pet['weight']=pet['weight'] + 0.5
    pet['hungry']=False
  else:
    print ('Pet Not Hungry')

#Dictonary
cat={
  'name':"Fluffy",
  'age':5,  
  'weight':2.5,
  'hungry':True,
  'photo':'(=^0.0^=)',
}

mouse={
  'name':"Taily",
  'age':5,
  'weight':1.5,
  'hungry':False,
  'photo':'<:3=~~',
}

#List
pets = []
pets.append(cat)
pets.append(mouse)

#Accessing list by Index
newPet = pets[0]
print (newPet['name']) #Cat

newPet = pets[1]
print (newPet['name']) #Mouse

#Looping
for pet in pets:
  print (pet['name'], pet['hungry'], pet['weight'])

for pet in pets:
  feed(pet)

for pet in pets:
  print (pet['name'], pet['hungry'], pet['weight'])