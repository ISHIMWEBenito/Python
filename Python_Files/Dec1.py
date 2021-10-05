"""def first(msg):
    print(msg)
    
first("A girl")

second = first
second("in town")

#higher-order functions

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result= func(x)
    return result

print(operate(inc, 6))
print(operate(dec, 2))"""

def is_called(msg):
    def is_returned():
        print(msg)
    return is_returned

new = is_called("Hello")
new()