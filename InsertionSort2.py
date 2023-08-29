def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        print(*arr)


arr=[1,3,4,5,2]
insertionSort2(len(arr), arr)
