# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов,
# которые имеют средний балл более «4». Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

New_list_of_students = []
list_of_students = ['Оценки студентов:\n',
                    'Ангела Меркель-5\n',
                    'Андрей Валетов-5\n',
                    'Фредди Меркури-3\n',
                    'Анастасия Пономарева-4\n']

data = open('list.txt', 'w')
data.writelines(list_of_students)
data.close()


def find_five(line, num_5, falses):
    if line.find((num_5)) > 0:
        falses = 'true'
    if line.find((num_5)) == 0:
        falses = 'false'
    return falses


def new_find_five(string):
    if string.isdigit(5):
        string.upper()
    data = open('list.txt', 'w')
    data.writelines(list_of_students)
    data.close()


with open('list.txt', 'r') as file:
    for line in file:
        falses = 'false'

        num_5 = '5'
        A = find_five(line, num_5, falses)

        if A == 'false':
            New_list_of_students.append(line)

        if A == 'true':
            line = line.upper()
            New_list_of_students.append(line)

file.close()

print(New_list_of_students)
data = open('list.txt', 'w')
data.writelines(New_list_of_students)
data.close()


exit()
