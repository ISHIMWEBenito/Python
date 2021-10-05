"""def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
        return inner
    
def ordinary():
    print("I am ordinary")
ordinary()

pretty = make_pretty(ordinary)


pretty()

def turnit_prettier(func):
    def inner():
        print("I'm getting more prettier")
        func()
    return inner

def ordinary():
    print("I am an average")
    
ordinary = turnit_prettier(ordinary)
ordinary()"""

def turnit_prettier(func):
    def inner():
        print("I'm getting more prettier")
        func()
    return inner

@turnit_prettier
def ordinary():
    print("I am an average")
    
ordinary()