list=[["bob",1],["sob",5],["dob",9]]
#for item, in list:
 #   print(item)
# for item,fog in list:
#      print(item,"uses",fog,"fog")
#
# dict1=dict(list)
# for item in dict1:
#         print(item)

list=[1,5,7,90,55,77,4,"rrg","gog"]
for item in list:
    if str(item).isnumeric() and item>6:
        print(item)