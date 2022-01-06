def containsDuplicate(nums):
    d={}
    for i in range(0,len(nums)):
        d[nums[i]]=0
    for i in range(0,len(nums)):
        d[nums[i]]+=1

    for i in d:
        if d[i]>1:
            return True
    return False

print(containsDuplicate([1,2,3,1]))