my_list = [4, 7, 0, 3, 6, 9]

"""#get an iterator using iter()
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))

# next(obj) is same as obj.__next__()
print(my_iter.__next__())


#this wil raise an error if no more items left
next(my_iter)

for i in my_list:
    print(i)"""

iter_obj = iter(my_list)

while True:
    try:
        item = next(iter_obj)
        #next item
        print(item)
        
    except StopIteration:
        continue
        #terminate loop if StopIteration is raised
        #break
