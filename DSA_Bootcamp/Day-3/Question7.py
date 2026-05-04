# Jump Search (Element Exists or Not)

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return False
        
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return True
    return False

# Example
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 0
print(jump_search(arr, target))