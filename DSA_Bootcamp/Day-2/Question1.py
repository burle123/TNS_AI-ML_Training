# Bubble Sort

arr = [1,2,6,43,2,8]

n = len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr [j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]

print(arr)