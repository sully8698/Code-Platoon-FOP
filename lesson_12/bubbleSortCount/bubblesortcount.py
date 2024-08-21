def bubbleSortCount(arr):
    comparisons = 0
    exchanges = 0
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i):
            print(f'i:{arr[i]} and j:{arr[j]}')
            comparisons += 1
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                exchanges += 1
        

    print(arr)
    return (comparisons, exchanges)






print(bubbleSortCount([1, 2, 3, 5, 4, 6, 7])) # (21, 1)
print(bubbleSortCount([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # (45, 45)
print(bubbleSortCount([2, 1, 0, 5, 4])) # (10, 4)