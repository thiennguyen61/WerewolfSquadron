
for n in range(0,10000):
    i = n
    if(n%2 != 0):
        n = n-1
    n = n//2
    if(n%2 != 0):
        n = n+1
    n = n - (n//4)
    n = n * 12
    n = n**2
    
    if(n == 3640464.0):
        break
    else:
        print("n = {}".format(n))
print(i)
