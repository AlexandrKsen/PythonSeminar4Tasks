# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

rle = "AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool"

data = open('rle.txt', 'w')
data.writelines(rle)
data.close()


def main():
    encoded = encode(rle)
    decoded = decode(encoded)

    print("Тестовая строка: " + rle)

    # Предполагаемый результат после сжатия: 12A11B10C6D5E4FG python is s7o c7ol
    print("Результатат сжатия строки: " + formatOutput(encoded))

    data = open('encoded.txt', 'w')
    data.writelines(formatOutput(encoded))
    data.close()

    # Предполагаемый результат после декодирования: AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
    print("Декодированная строка: " + decoded)


def encode(sequence):
    count = 1
    result = []

    for x, item in enumerate(sequence):
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:
            result.append((sequence[x - 1], count))
            count = 1

    result.append((sequence[len(sequence) - 1], count))



    return result


def decode(sequence):
    result = []

    for item in sequence:
        result.append(item[0] * item[1])

    return "".join(result)


def formatOutput(sequence):
    result = []

    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])

    return "".join(result)



if __name__ != "_main_":
    main()