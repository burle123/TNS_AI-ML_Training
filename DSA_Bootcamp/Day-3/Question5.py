#Binary Search - Last Occurence

def binary_search_lo(arr,target):

    low =0
    high = len(arr)-1
    result = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            result = mid
            low = mid + 1   # move right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

# Example

arr = [10, 20, 20, 20, 30, 50, 20, 2, 10, 30, 11, 21, 39 ]
target = 20

print(binary_search_lo(arr, target))