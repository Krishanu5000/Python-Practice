def smallestWindow(s, p):
    #code here
    l=[]
    d1={}
    d2={}
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            l.append(s[i:j+1])
    #print(l)
    for i in l:
        flag=False
        for j in range(len(p)):
            if i.find(p[j])>-1:
                flag=True
            else:
                flag=False
                break
        if flag==True:
            d1[i]=len(i)
    minm=min(d1.values())
    if len(d1)==0:
        return -1
    else:
        for i in d1:
            if d1[i]==minm:
                d2[i]=s.find(i)
        mimn_indx=min(d2.values())
        for i in d2:
            if d2[i]==mimn_indx:
                return i
print(smallestWindow("zoomlazapzo","oza"))