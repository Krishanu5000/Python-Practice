'''def printmsg():
    return "How are you"

def printer(func,y):
    print("Executing the function")
    print(func(),"..",y)
    print("Finsihed the function")

printer(printmsg,"Krishanu")

#Closure

def numcheck_positive(x):
    d=1
    def checker():
        if x>0:
            print(x)
        else:
            print("Not positive, Hence returning default value", d)
    return checker

f = numcheck_positive(-1)

f()'''

#decorator
'''
def evenodd(x):
    if x%2==0:
        print("even number")
    elif x%2!=0:
        print("odd number")
def decorated_fun(y,func):
    def inner():
           if y>0:
               print("excuting function")
               func(y)
               print("Finshed function")
           else:
               print("excuting function")
               print("provide a valid number in function")
               print("Finshed function")
    return inner

f1= decorated_fun(10,evenodd)
f1()
'''
def decorated_fun(func):
    def inner(y):
        if y>0:
            print("excuting function")
            func(y)
            print("Finshed function")
        else:
            print("excuting function")
            print("provide a valid number in function")
            print("Finshed function")
    return inner
@decorated_fun
def evenodd(x):
    if x%2==0:
        print("even number")
    elif x%2!=0:
        print("odd number")

evenodd(-1)