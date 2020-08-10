# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    middle = (start + end) // 2
    possibleMatch = arr[middle]
    if target == possibleMatch:
        return middle
    elif target < possibleMatch:
        return binary_search(arr, target, start, middle - 1)
    else:
        return binary_search(arr, target, middle + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here
