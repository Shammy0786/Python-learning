import time
# initial = time.time()
#
# k=0
# while(k<45):
#     print("shammy haider")
#     time.sleep(2) #this will gives you output every 2 sec
#     k+=1
# print("while loop time",time.time()-initial,"sec")
#
# initial1=time.time()
# for i in range(45):
#     print("shammy haider")
# print("for loop time",time.time()-initial1)


localtime = time.asctime(time.localtime(time.time())) # our present time
print(localtime)


