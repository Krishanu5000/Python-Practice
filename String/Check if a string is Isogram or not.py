'''Given a string S of lowercase alphabets, check if it is isogram or not.
An Isogram is a string in which no letter occurs more than once.'''

def isIsogram(s):
    #Your code here
    d={}
    for i in s:
        d[i]=0
    for i in s:
        d[i]+=1
    for i in d:
        if d[i]>1:
            return False
    return True
print(isIsogram("geeks"))
