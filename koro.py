def searcher(): # korotine
    import time
    book="this is that things and so on"
    time.sleep(3)

    while True:
        text=(yield )
        if text in book:
            print("found it")
        else:
            print("not found")

ser=searcher()
print("search started")
next(ser) #next method for korotine
print("next method run")
ser.send("this")
input("press any key")
ser.send("that")
input("press any key")
ser.send("those")
input("press any key")
ser.send("jif")

ser.close() # after close it will not take itration
ser.send("this")
input("press any key")
