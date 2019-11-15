print('You are in my pet store')

def feed(pet):
  if pet['hungry'] == True:
    pet['weight']=pet['weight'] + 0.5
    pet['hungry']=False
  else:
    print ('Pet Not Hungry')

cat={
  'name':'Fluffy',
  'age':5,
  'weight':2.5,
  'hungry':True,
  'photo':'(=^0.0^=)',
}

mouse={
  'name':'Taily',
  'age':5,
  'weight':1.5,
  'hungry':False,
  'photo':'<:3=~~',
}

pets = [cat, mouse]

for pet in pets:
  print (pet['hungry'], pet['weight'])

for pet in pets:
  feed(pet)

for pet in pets:
  print (pet['hungry'], pet['weight'])