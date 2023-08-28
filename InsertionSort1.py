def insertionSort1(arr):
    temp = arr[-1]; #reserve the last number
    
    for i in reversed(arr[:-1]):
        if i>temp:
            arr[arr.index(i)+1] = i
        else:
            arr[arr.index(i)+1] = temp
            break
        print (*arr)
    else:
        arr[0] = temp
    print(*arr)
    

arr=[8,3,4,5,7,6,2]
insertionSort2(len(arr), arr)