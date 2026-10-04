from functools import lru_cache
@lru_cache(maxsize = 1024)
def fibbonaci(n):
    if n in [0,1]:
        return 1
    else:
        return fibbonaci(n-1)  + fibbonaci(n-2)

print(fibbonaci(int(input("enter num"))))