
def print_name():
    list_a = [1,2,3]

    for i in list_a:

        yield i

gen = print_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

