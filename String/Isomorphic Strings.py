def areIsomorphic(str1,str2):
    if len(str1)!=len(str2):
        return False
    k=str1+str2
    m=len(str2)
    d1={}
    d2={}

    for i in range(len(str1)):
        d1[str1[i]]=0
        d2[str2[i]]=0
    for i in range(len(k)-m):
        d1[k[i]]+=1
        d2[k[i+m]]+=1

    #print(d)
    #print(k)
    for i in range(len(k)-m):
        if d1[k[i]]!=d2[k[i+m]]:
            return False
    return True
print(areIsomorphic("xudzhi","ftakcz"))