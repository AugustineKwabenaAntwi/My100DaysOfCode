def squared():
    a = 1
    while True:
        yield a*a
        a =a+1

for num in squared():
    if num > 120:
        break
    print (num)    