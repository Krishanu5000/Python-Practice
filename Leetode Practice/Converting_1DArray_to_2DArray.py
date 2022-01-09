def construct2DArray(original,m,n):
    l=[[0 for i in range(n)] for j in range(m)]
    cnt=0
    for i in range(0,m):
        for j in range(0,n):
            cnt+=1
    print(cnt)
    if cnt!=len(original):
        return []
    #k=len(original)
    #if (k==1 and k<n) or (k==1 and k<m):
        #return []
    #elif k==m*n:
    pos=0
    for i in range(0,m):
        for j in range(0,n):
            l[i][j]=original[pos]
            pos+=1
    return l

print(construct2DArray([1,2,3,4],2,2))

