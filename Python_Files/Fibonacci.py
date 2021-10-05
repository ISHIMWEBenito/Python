n1 = 0
n2 = 1
n_terms = 10
count = 0
while count < n_terms:
    print(n1, end=',')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print()