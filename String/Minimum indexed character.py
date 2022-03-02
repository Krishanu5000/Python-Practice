def minIndexChar(s, pat):
    #code here
    l=[]
    for i in pat:
        if s.find(i)!=-1:
            l.append(s.find(i))
    #print(l)
    if len(l)==0:
        return -1
    else:
        #print(min(l))
        return min(l)
print(minIndexChar("hasjkhflaskdf","sdlkjfshd"))
