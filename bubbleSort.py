def bubbleSort(arr):

    arr_len = len(arr)
    
    for i in range(arr_len - 1): #6
        checkVal = 0

        for j in range(0, arr_len - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j+1], arr[j] = arr[j] , arr[j+1]
                checkVal = 1
                print(arr)
unsorted = ["D", "S", "M", "R", "A", "E"]
sorted = bubbleSort(unsorted)
print(sorted)
