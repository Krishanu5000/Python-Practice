'''Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.
Eaxmple:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
'''

def findDuplicates(nums):
    n=len(nums)
    l=[0]*(n+1)
    dup=[]
    for i in range(n):
        l[nums[i]]+=1
    for i in range(len(l)):
        if l[i]>1:
            dup.append(i)
    return dup
print(findDuplicates([4,3,2,7,8,2,3,1]))