#import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
#array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

#is_sort = False  # станет True, если отсортирован
#count = 0  # счетчик количества перестановок

#while not is_sort:  # пока не отсортирован
#    count += 1  # прибавляем 1 к счётчику

#    random.shuffle(array)  # перемешиваем массив

    # проверяем, отсортирован ли
#    is_sort = True
#    for i in range(len(array) - 1):
#        if array[i] > array[i + 1]:
#            is_sort = False
#            break

#print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(count)
# 290698


#Сортировка выбором

#array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#count = 0  # счетчик количества перестановок

#for i in range(len(array)):  # проходим по всему массиву
#    idx_min = i  # сохраняем индекс предположительно минимального элемента
#    for j in range(i, len(array)):
#        if array[j] < array[idx_min]:
#            idx_min = j
#            count += 1  # прибавляем 1 к счётчику
#    if i != idx_min:  # если индекс не совпадает с минимальным, меняем

#       array[i], array[idx_min] = array[idx_min], array[i]
#print(count)
#print(array)


#Модифицируйте описанный алгоритм для сортировки по убыванию.
#for i in range(len(array)):
#    idx_max = i
#    for j in range(i, len(array)):
#        if array[j] > array[idx_max]:
#            idx_max = j
#    if i != idx_max:
#        array[i], array[idx_max] = array[idx_max], array[i]

#Сортировка выбором в виде танца.
#array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

#for i in range(len(array)):
#    for j in range(len(array) - i - 1):
#        if array[j] > array[j + 1]:
#           array[j], array[j + 1] = array[j + 1], array[j]
#print(array)

#Сортировка вставками
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        count+=1
    array[idx] = x
print(array)
print(count)








