def find_slope(x, y):
    try:
        slope = y/x
        print('Slope between ', x, ' & ', y, '= ', slope)
        except ValueError:
            print("InvalidInput")
        except ZeroDivisionError:
            print("Divide-by-zero error")
        except:
            print("Some other error occurred")
            

find_slope(5, 10)
find_slope('a', 'b')
find_slope(9, 1)
        