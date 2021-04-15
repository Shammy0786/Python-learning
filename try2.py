f=open("Shammy.txt")

try:
    f= open("fdf.txt")
    # f = open("Shammy.txt")

# except Exception as e:
except EOFError as e:
    print("eof error occur",e)
except IOError as e:
    print("io error occur",e)

else:
    print("This will run if except is not running")

finally:
    print("anyway")
    f.close()
print("important")
