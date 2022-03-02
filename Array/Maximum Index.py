'''Given an array A[] of N positive integers.
The task is to find the maximum of j - i subjected to the constraint of A[i] < A[j] and i < j.
Input:
N = 9
A[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output:
6
Explanation:
In the given array A[1] < A[7]
satisfying the required
condition(A[i] < A[j]) thus giving
the maximum difference of j - i
which is 6(7-1).
'''

def maxIndexDiff(A,N):
    '''max=0
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            if A[i]<=A[j] and max<(j-i):
                max=j-i
    return max'''
    '''max=0
    high = len(A)-1
    for i in range(len(A)):
        if A[i]<A[high] and max<high-i:
            #max=high-i
            #high-=1
            max=high-i
            return max
        high-=1'''
    #return max

    '''index = dict()
    for i in range(n):
        if A[i] in index:
            #append to list (for duplicates)
            index[A[i]].append(i)
        else:
            # if first occurrence
            index[A[i]] = [i]
    print(index)
    # sort the input array
    A.sort()
    maxDiff = 0
    # Temporary variable to keep track of minimum i
    temp = n
    for i in range(n):
        if temp > index[A[i]][0]:
            temp = index[A[i]][0]
        maxDiff = max(maxDiff, index[A[i]][-1]-temp)

    print(maxDiff)'''
    maxDiff = 0;
    LMin = [0] * N
    RMax = [0] * N

    # Construct LMin[] such that
    # LMin[i] stores the minimum
    # value from (arr[0], arr[1],
    # ... arr[i])
    LMin[0] = A[0]
    for i in range(1, N):
        LMin[i] = min(A[i], LMin[i - 1])

    # Construct RMax[] such that
    # RMax[j] stores the maximum
    # value from (arr[j], arr[j + 1],
    # ..arr[n-1])
    RMax[N - 1] = A[N - 1]
    for j in range(N - 2, -1, -1):
        RMax[j] = max(A[j], RMax[j + 1]);

    # Traverse both arrays from left
    # to right to find optimum j - i
    # This process is similar to
    # merge() of MergeSort
    i, j = 0, 0
    maxDiff = -1
    while (j < N and i < N):
        if (LMin[i] <= RMax[j]):
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1

    return maxDiff

print(maxIndexDiff([34, 8, 10, 3, 2, 80, 30, 33, 1],9))
print(maxIndexDiff([65,6,74,94,56,89,9,63,75,25,34,68,93,48,16],15))