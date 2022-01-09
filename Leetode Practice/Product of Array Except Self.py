''''def productExceptSelf(nums):
    product=1
    answer=[]
    for i in nums:
        product*=i
    print(product)
    for i in nums:
        answer.append(product//i)
    return answer
print(productExceptSelf([1,2,3,4]))'''

def productArray(nums):

    # Base case
    n=len(nums)
    if n == 1:
        print(0)
        return

    i, temp = 1, 1

    # Allocate memory for the product array
    prod = [1 for i in range(n)]
    #print(arr)
    #print("prod",prod)

    # Initialize the product array as 1

    # In this loop, temp variable contains product of
    # elements on left side excluding arr[i]
    for i in range(n):
        #print("i ",i)
        prod[i] = temp
        temp *= nums[i]
    #print("left side excluding arr[i]",prod)
    # Initialize temp to 1 for product on right side
    temp = 1

    # In this loop, temp variable contains product of
    # elements on right side excluding arr[i]
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= nums[i]
        #print("from right side i",i)
        #print("arr[i]",arr[i])
        #print("right side excluding arr[i]",prod)

    '''# Print the constructed prod array
    for i in range(n):
        print(prod[i], end = " ")'''

    return prod

# Driver Code
arr = [10, 3, 5, 6, 2]
n = len(arr)
print("The product array is: n")
print(productArray(arr))
