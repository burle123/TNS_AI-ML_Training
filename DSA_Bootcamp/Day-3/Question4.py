#Binary Search - First Occurence

def binary_search_fo(arr,target):

    low =0
    high = len(arr)-1
    result = -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            result = mid
            high = mid - 1   # move left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

# Example

arr = [10, 20, 20, 20, 30, 50, 20, 2, 10]
target = 20

print(binary_search_fo(arr, target))