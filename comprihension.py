# ls=[]
# for i in range(39):
#     if i%3==0:
#         ls.append(i)

# ls=[i for i in range(45) if i%3==0]
# print(ls)

# dict1={i:f"item {i}" for i in range(65) if i%5==0}
# dict2={value:key for key,value in dict1.items()}
#
# print(dict1 ,"\n",dict2)

drs={drss for drss in ["d1","d2","d1","d2","d1","d2"]} #set it will print d1 and d2 onces
drs=[drss for drss in ["d1","d2","d1","d2","d1","d2"]] #list it will print all the item
print(drs)
print(type(drs))

evens=(i for i in range(50) if i%2==0)
print(evens.__next__())
print(evens.__next__())

for i in evens:
    print(i)