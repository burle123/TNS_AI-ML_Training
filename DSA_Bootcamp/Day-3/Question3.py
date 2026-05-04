#Binary Search (Basic Search)

def binary_search(arr,target):

    low =0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1  # Target not found

# Example

arr = [10, 20, 40, 30, 22, 100, 32, 234 ]
target = 30

print(binary_search(arr, target))