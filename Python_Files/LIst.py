my_list = [ 'P', 'y', 't', 'h', 'o', 'n' ]
print(my_list[2:5])
print(my_list[3:])
print(my_list[:-5])
print(my_list[:])
my_list[4] = 'b'
print(my_list[4])
my_list[1:4] = [ 'g', 'r', 'w']
print(my_list[1:4])
my_list.append('z')
print(my_list)
my_list.extend([ 't', 'q', 'a' ])
print(my_list)
print(my_list + [ 'j', 'v' ])
my_list.insert(1, 3)
print(my_list)
del my_list[1:3]
print(my_list)
my_list.remove('w')
print(my_list)
print(my_list.pop())
print(my_list.pop(1))
your_list = my_list.copy()
my_list[0] = 'Benito The Software engineer'
print(my_list)
for letters in my_list:
    print("Letter", letters)
print('y' in my_list)
print('a' in my_list)
print('z' in my_list)
my_list[4] = [ 5, 6, 0, 5]
print(my_list)
print(my_list[4][4])
      