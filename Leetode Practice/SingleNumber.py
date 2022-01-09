def singleNumber(nums):
    '''d={}
    for i in range(0,len(nums)):
        d[nums[i]]=0
    for i in range(0,len(nums)):
        d[nums[i]]+=1
    for i in d:
        if d[i]==1:
            return i'''
    a=0
    for i in range(0,len(nums)):
        a=a^nums[i]
    return a
print(singleNumber([2,10,1,10,2]))
