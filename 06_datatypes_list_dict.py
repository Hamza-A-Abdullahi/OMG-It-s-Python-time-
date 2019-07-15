#some time we just need to list our crazy x-pokemons :)
#because we don't want to work there

crazy_pokemons = ['snorlax','mew','Articuno','Kartana','pikachu','Charmander']
# print('here is pokemons: ',crazy_pokemons)


#list are organised using index

# print('the length of the pokemon list is: ',len(crazy_pokemons))
# # print(crazy_pokemons[3])

#if you want to print the last in a list
#you have two option

# print(crazy_pokemons[len(crazy_pokemons)-3])

# re-assigning the value in a list

# crazy_pokemons [3] = 'Kecleon'
# print (crazy_pokemons)

# appending a new pokemon
#we caught 	Quilava

# crazy_pokemons.append('Quilava')
# print(crazy_pokemons)

#Dictionaries  AKA hashes
#work with key: value paris

#declaring a hash / dictionary
pika= {}

#dictinary work with keys : values

pika= {
    'name': 'Derik',
    'pokemon': 'pikachu',
    'age':17,
    'personality': 'grumpy'
}



print (pika['age'])

#adding a key: value pair

pika['colour']= 'yellowish'
print(pika)

#re-assigning

pika ['age'] = 18
print(pika)