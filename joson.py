import json

data ='{"n1":"sham","n2":"had"}'
# print(data['n1']) # here you can't do this

parsed = json.loads(data)
print(parsed['n1']) # here you can do becouse of json (java scriot open notation)
print(parsed)

data2={"vf":"gg","ff":"rg","car":['fg','ef'],
       "gk":('ef','gg'), "isbad": False }  #java script take small false

jcomp = json.dumps(data2) #that code in data makes for java script like false
print(jcomp)

# sort_keys_parameter in dumps