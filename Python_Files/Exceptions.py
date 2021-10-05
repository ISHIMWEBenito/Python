#if 5 > 3
#print('5 is greater than 3')
#print(1/0)
"""def findReciprocal(value):
    try:
        print("value:", value)
        r = 1/value
        print("The reciprocal of", value, "is", r, "\n")
        except:
            print("You cannot find reciprocal of", value, "\n")
        
findReciprocal("Benito the software engineer")
findReciprocal(2)


def findReciprocal(value):
    try:
        print("Value:", value)
        r = 1/value
        print("Reciprocal of", value, "is", r)
        except ValueError:
            print("You got value error.")
        except ZeroDivisionError:
            print("You got zero division error.")
        except:
            print("Handling all other errors.")

findReciprocal(0)

a = int(input("Enter a positive integer: "))

try:
    if a <= 0:
        raise ValueError("Not a positive number!")
    print("You entered", a)
except ValueError as ve:
    print(ve)"""

try:
    f = open("test.txt", encoding = 'cp1252')
    # perform file operations
    finally:
        f.close()