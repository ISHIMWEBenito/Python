"""# Outer enclosing function
def print_msg(msg):
    
# This is a nested function
    def printer():
        print(msg)
        
#calling printer() from inside print_msg()
        
        printer()
        
print_msg("HELlo")


#Define a closure

# Outer enclosing function
def print_msg(msg):
    
    def printer():
        print(msg)
                
        return printer  # returning printer()
# Now let's try calling this function
        
another = print_msg("HELlo")
another()"""

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times7 = make_multiplier_of(7)

print(times3(9))
print(times7(3))
print(times7(times3(2)))







