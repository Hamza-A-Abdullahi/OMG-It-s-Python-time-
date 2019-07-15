# story= {
#     'story_begenning : ' 'Once a ' ,
#     'story_middle :',
#     'story_end : '
# }

my_dict = dict()

key = input("Enter the title of  beginning chapter of your story: \n")
value = input("type the beginning of story: \n")

key_m = input("Enter the  title of  middle chapter of your story: \n")
value_m = input("type the middle of story: \n ")

key_end = input("Enter the title of end chapter of your story: \n")
value_end = input("type the end of story: \n ")

my_dict[key] = value # chapter 1 beginning

my_dict[key_m] = value_m  #chapter 2 middle

my_dict[key_end] = value_end  #chapter 3 the end

print(my_dict)