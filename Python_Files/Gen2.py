#return an object but the execution is not started yet
a = my_gen()

# Iterating through the items using next().
next(a)
This is printed first

next(a)
This is printed second

next(a)
This is printed last

print(next(a))
print(next(a))
print(next(a))
print(next(a))
