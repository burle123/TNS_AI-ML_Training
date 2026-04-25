# Count Number of Swaps in Bubble Sort

arr = [5,3,2,1,7,9,4]
count = 0
n = len(arr)

for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            count += 1

print("Swaps = ", count)
print(arr)            

