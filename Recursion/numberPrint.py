def numberPrint(n):
    if(n==0):
        return
    print(n)
    numberPrint(n-1)

def numberPrint1(n):
    if(n==0):
        return
    numberPrint1(n-1)
    print(n)
numberPrint(5)
numberPrint1(5)

