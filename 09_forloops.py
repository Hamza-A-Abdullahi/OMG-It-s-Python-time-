######## FOR LOOPS IN PYTHON

#Syntax
#for  <placeholder> in <list>:
# run block pof code

# x_crazy_landlord = ['cruella de vill',"Donald Duck","popeye the maltese"]
#
# counter =0
# for land_1 in x_crazy_landlord:
#     print("hello ")
#     print (land_1)
#     print(counter)
#     counter +=1
#

#exercise one
#print  the name of out landlord with nice formating
#listing them using numbers

# x_crazy_landlord = ['cruella de vill',"Donald Duck","popeye the maltese"]
#
# counter =1
#
# for land_lord in x_crazy_landlord:
#     print(counter,'-',land_lord)
#     counter +=1

#Further loops

# list_data = [1,2,3,4,5]
# embededd_list =[[1,2,3,],[6,7,8,9]]
#
#
# for number in embededd_list:
#     print (number)
#     for data in number:
#         print(data)


# spartans_name = ['hamza','shav','payal','nalia','danny boyyyyyyyy','ally', 'omid', 'Matthew ','adam',
# 'Mystery man', 'jojo','mo']
#
#
#
# for name in spartans_name:
#     print('This is:', name, "get to know him/her")

# list_scores = [1,6,8,9,4,6,1]
#
# for score in list_scores :
#     result_percent= score /10*100
#     print(result_percent)

list_embed_scores= [[10,5,2],[3,4,6]]

for ind_list in list_embed_scores:
    print(ind_list)
    for num in ind_list:
        print(num * 2)
