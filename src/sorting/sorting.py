# def merge_sort(arr):
#     if len(arr) > 1:
#         return arr
#     middleIdx = len(arr) // 2
#     left = arr[:middleIdx]
#     right = arr[middleIdx:]
#     return merge(merge_sort(left), merge_sort(right))
# # TO-DO: complete the helper function below to merge 2 sorted arrays


# def merge(left, right):
#     merged_arr = [None] * (len(left) + len(right))

#     k = i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged_arr[k] = left[i]
#             i += 1
#         else:
#             merged_arr[k] = right[j]
#             j += 1
#         k += 1
#     while i < len(left):
#         merged_arr[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         merged_arr[k] = right[j]
#         j += 1
#         k += 1

#     return merged_arr
def merge(left, right):

    left_index, right_index = 0, 0
    merged = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middleIdx = len(arr) // 2
    left = merge_sort(arr[:middleIdx])
    right = merge_sort(arr[middleIdx:])

    return merge(left, right)


# TO-DO: implement the Merge Sort function below recursively


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
# Your code here

# def merge_sort_in_place(arr, l, r):
#     pass
