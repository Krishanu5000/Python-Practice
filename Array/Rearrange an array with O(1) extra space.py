'''Given an array arr[] of size N where every element is in the range from 0 to n-1.
Rearrange the given array so that arr[i] becomes arr[arr[i]].
Input:
N = 5
arr[] = {4,0,2,1,3}
Output: 3 4 2 0 1
Explanation:
arr[arr[0]] = arr[4] = 3.
arr[arr[1]] = arr[0] = 4.
and so on.
'''

def arrange(arr, n):
    #Your code here
    l=[]
    for i in range(len(arr)):
        l.append(arr[arr[i]])
    for j in range(len(l)):
        arr[j]=l[j]
    return arr

print(arrange([4,0,2,1,3],5))