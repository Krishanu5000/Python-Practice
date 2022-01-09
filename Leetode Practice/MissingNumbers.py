def missingNumber(nums):
    nums.sort()
    #print(nums)
    for i in range(len(nums)):
        if i!=nums[i]:
            return i
    if i==len(nums)-1:
        return i+1
print(missingNumber([0,1]))