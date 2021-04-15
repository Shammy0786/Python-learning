def shm(str):
    return f"give this string {str}"

def add(n1,n2):
    return n1+n2+5

print("and the name is",__name__) # this will tell us the name
if __name__ == '__main__':  # this main used only for this exicution after import
    print(shm("shammy"))
    b=add(6,4)
    print(b)