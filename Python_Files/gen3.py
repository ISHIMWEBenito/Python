# A simple generator function
"""def my_gen():
    n = 1
    print('This is printed first')
    #Generator function contains yield statements
    yield n
    
    n += 1
    print('This is printed second')
    yield n
    
    n += 1
    print('This is printed at last')
    yield n
    
# using for loop
for item in  my_gen():
    print(item)"""
    
def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1,-1,-1):
        yield my_str[i]
        
# For loop to reverse the string
for char in rev_str("hello"):
    print(char, end= '')
print()

