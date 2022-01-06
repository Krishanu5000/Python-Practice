def maxOccured(L, R, n, max_val):
    ##Your code here
    prefix_arr = [0] * (max_val + 2)
    for index, (l_val, r_val) in enumerate(zip(L, R)):
        prefix_arr[l_val]     += 1
        prefix_arr[r_val + 1] -= 1
    print(prefix_arr)

    for i in range(1, len(prefix_arr)):
        prefix_arr[i] += prefix_arr[i-1]
    print(prefix_arr)

maxOccured([1,2,3],[3,5,7],3,7)