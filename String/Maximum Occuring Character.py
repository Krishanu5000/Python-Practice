def getMaxOccurringChar(s):
    #code herenonrepeatingCharacter
    d={}
    l=[]
    m=len(s)
    for i in range(m):
        d[s[i]]=0
    for i in s:
        d[i]+=1

    max_value=max(d.values())

    for i in d:
        if d[i]==max_value:
            l.append(i)
    return min(l)
print(getMaxOccurringChar("testsample"))