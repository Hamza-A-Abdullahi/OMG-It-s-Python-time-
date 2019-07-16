#for loop-  using dictionaries/ hashes

#syntax
# for <placeholder> in <dict>
    #run block of code


# dict_data = {
#     'name': 'Bronson',
#     'moeny': 200
#
# }
#
# for key in dict_data:
#     print(key,dict_data[key])
#

embedded_data = {
     1: {
    'name': 'Bronson',
    'moeny': 200
     },
    2: {
    'name': 'Tania',
    'moeny': 312
    },
    3:{
    'name': 'tylor',
    'moeny':125
    }
}

for key in embedded_data:
    print(key,embedded_data[key])