#Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
arr = [10, 20, 30, 40]
target = 30

print(linear_search(arr, target))