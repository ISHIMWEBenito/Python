class Number:
    def add(self, a, b):
        return a+b
    def multiply(self, a, b):
        return a*b
    
#instantiate an object
n1 = Number()

sum = n1.add(2, 5)
print(sum)

product = n1.multiply(2, 5)
print(product)