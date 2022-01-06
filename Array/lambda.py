x=lambda a,b: a+b
print(x(2,3))

def multipler(n):
    return lambda a: a*n
m=multipler(10)
print(m(5))