def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n=len(matrix)
    m=len(matrix[0])
    print(n)
    print(m)
    r=[]
    c=[]
    for i in range(n):
        r.append(False)
    #print(r)
    for i in range(m):
        c.append(False)
    #print(c)
    #print("length of c",len(c))
    for i in range(0,len(r)):
        for j in range(0,len(c)):
            if matrix[i][j]==0:
                c[j]=True
                r[i]=True
    print(c)
    print(r)

    for i in range(len(r)):
        for j in range(len(c)):
            if c[j]==True or r[i]==True:
                matrix[i][j]=0
    return matrix
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

