def difference(arr):
    min_index = 0
    max_index = 0

    for i in range(len(arr)): #цикл по массиву
        if arr[i] < arr[min_index]:
            min_index = i
        if arr[i] > arr[max_index]:
            max_index = i

    return abs(max_index - min_index)