# Jump Search (Basic)
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
        
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Example

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 50
print(jump_search(arr, target))