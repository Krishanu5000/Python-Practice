def repeatingCharacter(s):
    #code here
    d={}
    m=len(s)
    for i in range(m):
        d[s[i]]=0
    for i in s:
        d[i]+=1
    for i in range(len(s)):
        if d[s[i]]>1:
            return i
    return -1

print(repeatingCharacter("geeksforgeeks"))