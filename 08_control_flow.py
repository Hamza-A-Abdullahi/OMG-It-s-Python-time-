#### control flow - if statmentts


# age = 18
#
# if age >= 70:
#     print("relax you done well. enjoy you time with your grandchildern ")
# elif age >= 21:
#     print("you are a free man/woman " )
# elif age >= 18:
#     print("your age is above:", age, "you can join the army")
# else:
#     print("you are underage, jus relax ")

weather =  input("what is the weather like ").lower()

if 'rainy' in weather and 'stormy' in weather:
    print('take an umbrella and a jacket')
elif weather == 'sunny':
    print('take a sun glassess and suncream')
elif 'foggy' in weather:
    print("WHEN CLOUDS APPEAR LIKE TOWERS, THE EARTH IS REFRESHED BY FREQUENT SHOWERS." "\n Make sure take a umbrella")
else:
    print ('live you best life :D')

