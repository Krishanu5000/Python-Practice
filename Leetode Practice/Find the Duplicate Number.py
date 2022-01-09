'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
Example:
Input: nums = [1,3,4,2,2]
Output: 2
'''

def findDuplicate(nums):
    n=len(nums)
    l=[0]*(n+1)
    for i in range(n):
        l[nums[i]]+=1
    for i in range(len(l)):
        if l[i]>1:
            return i
print(findDuplicate([1,3,4,2,2]))