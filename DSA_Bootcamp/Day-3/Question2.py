# Linear Search (Count Occurrences)

arr=[1,2,2,4,5,6,2,1]
target = 2

def linear_search_count(arr,target):

    count = 0

    for i in range(len(arr)):

        if arr[i] == target:

            count +=1

    return count

print(linear_search_count(arr,target))        
