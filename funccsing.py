import time

from functools import lru_cache
@lru_cache(maxsize=3) # providing only 3
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(2) # cash only these 3
    some_work(5) # "
    some_work(4) # "
    print("Done! calling again")
    some_work(3)
    print("called")