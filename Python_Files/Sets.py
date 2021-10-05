my_set = {1, 5, 7, 3, 8, 2}
print(my_set)
my_bitch = set ([1, 4, 6])
print(my_bitch)
my_set.add(4)
print(my_set)
my_set.update([6, 9])
print(my_set)
my_set.discard(3)
print(my_set)
my_set.remove(7)
print(my_set)
my_set.discard(7)
print(my_set)
returned_value = my_set.pop()
print(my_set)
print(returned_value)
A = {'a', 'e', 'y', 'z', 'm'}
B = {'x', 'p', 'g', 'a', 'y'}
result = A | B
print(result)
result = B.union(A)
print(result)
intercars = A & B
print(intercars)
intercars = B.intersection(A)
diff = A - B
print(diff)
diff = B - A
print(diff)
diff = A.difference(B)
print(diff)
sdiff = A ^ B
print(sdiff)
sdiff = A.symmetric_difference(B)
print(sdiff)
for letters in my_set:
    print(letters)
my_dict = {1: 'apple', 2: 'ball'}
my_dick = dict({1:'apple', 2: 'ball'})
print(my_dick)
dick_name = my_dick[1]
print(dick_name)
dick_name = my_dick.get(1)
my_dick['fruit'] = 'peack'
my_dick[2] = "banana"
print(my_dick)
value = my_dick.pop(1)
del my_dict[1]
print(my_dict)
print(1 in my_dick)
print("sperms" in my_dict)
