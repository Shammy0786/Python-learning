# f=open("shammy.txt","w") # write mode replacing the content
# # f=open("shammy.txt","a") #apend mode addup with existing content
# # f.write("shammy is also good nature boy\n")
# a=f.write("shammy is also good nature boy\n")
# print(a)
# f.close()

# handle read and write both
f=open("shammy.txt","r+")
print(f.read())
f.write("thnaks")
# f=open("shammy.txt","a") # write mode replacing the content
# # f=open("shammy.txt","a") #apend mode addup with existing content
# # f.write("shammy is also good nature boy\n")
# a=f.write("shammy is also good nature boy\n")
# print(a)
# f.close()