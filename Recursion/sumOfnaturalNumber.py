'''sum=0
def sumOfnaturalNumber(sum,n):
    if n==0:
        return sum
    #print(sum)
    return sumOfnaturalNumber(sum+n,n-1)

print(sumOfnaturalNumber(sum,5))'''

def sumOfnaturalNumber(n):
    if(n==0):
        return 0;
    return n + sumOfnaturalNumber(n-1)

print(sumOfnaturalNumber(5))