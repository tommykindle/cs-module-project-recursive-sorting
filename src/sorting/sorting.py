def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middleIdx = len(arr) // 2
    left = arr[:middleIdx]
    right = arr[middleIdx:]
    return merge(merge_sort(left), merge_sort(right))
# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(left, right):
    merged_arr = [None] * (len(left) + len(right))

    k = i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr[k] = left[i]
            i += 1
        else:
            merged_arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        merged_arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        merged_arr[k] = right[j]
        j += 1
        k += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
    # Your code here

    # def merge_sort_in_place(arr, l, r):
    #     pass
