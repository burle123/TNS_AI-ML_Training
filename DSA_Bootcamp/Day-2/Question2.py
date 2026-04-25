# Optimize Bubble Sort
# - Optimized Bubble Sort stops early when no swaps happen.

arr = [1,2,6,4,3,2,8]

n = len(arr)

for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
        if arr[j] > arr [j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
            swapped = True
    if not swapped:
        break        

print(arr)