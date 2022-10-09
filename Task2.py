# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


numbers = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]


def unique_nums(numbers):
    unique = []

    for num in numbers:
        if num in unique:
            continue
        else:
            unique.append(num)
    return unique


print('Уникальные числа:', unique_nums(numbers))
