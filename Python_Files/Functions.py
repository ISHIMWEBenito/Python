def recursion(num):
    if n == 1:
        return 1
    else:
        return n + recursion(n-1)
sum = recursion(3)
print(sum)
