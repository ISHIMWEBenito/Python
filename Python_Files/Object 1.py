class MyClass:
    #Methods and attributes
    a = 10
    b = 29
    def func(self):
        return 'Hello'
    
ob1 = MyClass()
ob2 = MyClass()
ob = MyClass()

print(ob1.a)
print(ob2.a)

ob1.a = 0
ob2.a = 100

print(ob1.a)
print(ob2.a)
print(MyClass.b)
print(ob.func())
