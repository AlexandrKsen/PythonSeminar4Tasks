# Шифр Цезаря - это способ шифрования, где каждая буква смещается на
# определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. К примеру, слово "абба"
# можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо,
# "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

# тестовая строка - Я остановил машину, вылез и снял черные очки.

string_for_encoding = "Я остановил машину, вылез и снял черные очки."
#string_for_encoding = "Я остановил машину, вылез и снял черные очки."

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = input("Введите цифры, это будет ключем (сдвиг) : ")


def checking_characters(symbols, res):
    main_out_1 = symbols.lower()  # проверка на строчные буквы
    main_out_2 = symbols.upper()  # проверка на прописные буквы
    if (symbols != main_out_1) and (symbols == main_out_2):
        res = 'True'
        return res
    if (symbols != main_out_2) and (symbols == main_out_1):
        res = 'False'
        return res


def search_in_alphabet_by_number(number_search, founded_symbol):
    all_alphabet1 = len(alphabet)
    res1 = 0
    for i in range(all_alphabet1):
        res1 += 1
        symb = alphabet[i]
        if res1 == (number_search+1):
            founded_symbol = symb
            break
    return founded_symbol

# перевод в строчные и заглавные буквы


def transfotmation_symbols(main_in, main_out_1, main_out_2):
    main_out_1 = main_in.lower()  # проврка на строчные буквы
    main_out_2 = main_in.upper()  # проверка на заглавные буквы
    if (main_in != main_out_1) and (main_in == main_out_2):
        return main_out_2
    if (main_in != main_out_2) and (main_in == main_out_1):
        return main_out_1


def search_symbol_in_alphabet_by_shift(variable3, variable5, variable4):

    main_out_1 = ''
    main_out_2 = ''

    B = transfotmation_symbols(variable3, main_out_1, main_out_2)

    variable3 = B
    symbols = variable3
    res = 'False'
    F = checking_characters(symbols, res)

    all_alphabet = len(alphabet)
    for i in range(all_alphabet):
        params = alphabet[i]
        if (variable3 == params) or (variable3 == params.upper()):
            # проверка не вышли ли мы за границы алфавита, за число 33...
            res2 = i+int(variable5)
            if res2 < all_alphabet:

                if F == 'False':
                    variable4 = alphabet[res2]
#                    print('i :' + str(i) + '// variable3: ' + variable3 + '// variable4: ' + variable4)
                    break
                if F == 'True':
                    variable4 = alphabet[res2]
                    variable4 = variable4.upper()
#                    print('i :' + str(i) + '// variable3: ' + variable3 + '// variable4: ' + variable4)
                    break
            if res2 == all_alphabet:
                res2 = res2 + 1

            if (res2) > all_alphabet:
                # вот на этом месте надо на начало переводить ...
                Sign = (res2) - all_alphabet
                number_in_search = int(Sign)
                founded_symbol = ''
                C = search_in_alphabet_by_number(
                    number_in_search, founded_symbol)

                if F == 'False':
                    variable4 = C
                    break
                if F == 'True':
                    variable4 = C
                    variable4 = variable4.upper()
                    break

    return variable4


def encode(variable1, variable2, variable3):

    line_length = len(variable1)
    for elem in range(line_length):
        symbol = variable1[elem]

        symbol_zpt = ','
        if symbol == symbol_zpt:
            variable3 = variable3 + str(',')

        symbol_tchk = '.'
        if symbol == symbol_tchk:
            variable3 = variable3 + str('.')

        symbol_out = ' '
        if symbol == symbol_out:
            variable3 = variable3 + str(symbol_out)

        if (symbol != symbol_out) and (symbol != symbol_zpt) and (symbol != symbol_tchk):
            A = search_symbol_in_alphabet_by_shift(symbol, sam_key, symbol_out)
            variable3 = variable3 + str(A)

    return variable3


def find_back(symbol2, sam_key, simvol_back):

    symbol_out = ' '
    if symbol2 == symbol_out:
        simvol_back = symbol_out

    symbol_tchk = '.'
    if symbol2 == symbol_tchk:
        simvol_back = symbol_tchk

    symbol_zpt = ','
    if symbol2 == symbol_zpt:
        simvol_back = symbol_zpt

    if (symbol2 != symbol_out) and (symbol2 != symbol_tchk) and (symbol2 != symbol_zpt):
        all_alphabet = len(alphabet)
        q = 0
        for i in range(all_alphabet):
            znahes = alphabet[i]
            if (symbol2 == znahes) or (symbol2 == znahes.upper()):
                res3 = int(i - int(sam_key))
                if res3 <= 33:
                    simvol_back = alphabet[res3]
                    break
                if res3 > 33:
                    res3 = 33 - (res3)
                    simvol_back = alphabet[res3]
                    break
    return simvol_back


def decrypt(line_shifr, sam_key, line_decrypt):

    line_length2 = len(line_shifr)
    for elem2 in range(line_length2):
        symbol2 = line_shifr[elem2]

        symbol_out = ' '
        if symbol2 == symbol_out:
            line_decrypt = line_decrypt + str(symbol_out)

        symbol_tchk = '.'
        if symbol2 == symbol_tchk:
            line_decrypt = line_decrypt + str(symbol_tchk)

        symbol_zpt = ','
        if symbol2 == symbol_zpt:
            line_decrypt = line_decrypt + str(symbol_zpt)

        if (symbol2 != symbol_out) and (symbol2 != symbol_tchk) and (symbol2 != symbol_zpt):

            simvol_back = ''
            E = find_back(symbol2, sam_key, simvol_back)
            res = 'False'

            GG = checking_characters(symbol2, res)
            if GG == 'True':
                line_decrypt = line_decrypt + str(E.upper())
            if GG == 'False':
                line_decrypt = line_decrypt + str(E)

    return line_decrypt


print('строка для шифрования:            '+string_for_encoding)
sam_key = key
line_shifr = ''
D = encode(string_for_encoding, sam_key, line_shifr)
print('строка, зашифрованная ключем   '+sam_key+' :' + D)

data = open('encoded.txt', 'w')
data.writelines(D)
data.close()

line_decrypt = ''
line_shifr = D
sam_key = key
G = decrypt(line_shifr, sam_key, line_decrypt)
print('строка, расшифрованная ключем -'+sam_key+' :' + G)
