def bubbleSort(arr):
    for i in range(len(arr) -1, -1, -1):
        for j in range(0, i):
            if arr[j] < arr[j + 1]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr 






print(bubbleSort([5, 3, 10, 6, 1])) # [1, 3, 5, 6, 10]
print(bubbleSort([100, 98, 101, 10])) # [10, 98, 100, 101]
print(bubbleSort([2, 1, 0, 5, 4])) # [0, 1, 2, 4, 5]