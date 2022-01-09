def findDisappearedNumbers(nums):
    l=[]
    for i in range(0,len(nums)):
        idx=abs(nums[i])-1
        nums[idx]=abs(nums[idx])*-1
    for i in range(0,len(nums)):
        if nums[i]>0:
            l.append(i+1)
    return l
print(findDisappearedNumbers([1,2]))