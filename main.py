

#5.	Реализовать модуль, содержащий функцию нахождения в массиве целых чисел
#   разности индексов максимального и минимального элементов.

import find_difference

n = int(input("Enter the size of the array: "))
arr = []
for i in range(n):
    arr.append(int(input()))

dif = find_difference.difference(arr)
print(dif)