# Задание «Квадратное уравнение»

# def discriminant(a, b, c):
#     """
#     функция для нахождения дискриминанта
#     """
#     disc = b**2-4*a*c
#     return disc
#
#
# def solution(a, b, c):
#     """
#     функция для нахождения корней уравнения
#     """
#     if discriminant(a, b, c) < 0:
#         print('корней нет')
#     elif discriminant(a, b, c) == 0:
#         x = -(b / (2 * a))
#         print(x)
#     else:
#         x_1 = (-b + discriminant(a, b, c) ** 0.5) / (2 * a)
#         x_2 = (-b - discriminant(a, b, c) ** 0.5) / (2 * a)
#         print(x_1, x_2)
#
#
# if __name__ == '__main__':
#     solution(1, 8, 15)
#     solution(1, -13, 12)
#     solution(-4, 28, -49)
#     solution(1, 1, 1)


# Задание «Голосование»

# def vote(votes: list):
#     vote_dict = {}
#     for key in set(votes):
#         vote_dict[key] = votes.count(key)
#     max_value = max(vote_dict.values())
#     for key, value in vote_dict.items():
#         if value == max_value:
#             return key
#
#
# if __name__ == '__main__':
#     print(vote([1,1,1,2,3]))
#     print(vote([1,2,3,2,2]))


# Задание «Секретарь»
#
# documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
#         {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
#       ]
#
# directories = {
#         '1': ['2207 876234', '11-2', '5455 028765'],
#         '2': ['10006'],
#         '3': []
#       }
#
# def get_name(doc_number):
#     for dict in documents:
#         if doc_number in dict['number']:
#             return dict['name']
#     return ('Документ не найден')
#
#
# def get_directory(doc_number):
#     for shelf, document in directories.items():
#         if doc_number in document:
#             return shelf
#     return ('Полки с таким документом не найдено')
#
#
# def add(document_type, number, name, shelf_number):
#     documents.append({'type':document_type, 'number':number, 'name':name})
#     shelf_number = str(shelf_number)
#     if shelf_number in directories:
#         directories[shelf_number].append(number)
#     else:
#         directories[shelf_number] = [number]
#
# if __name__ == '__main__':
#     print(get_name("10006"))
#     print(get_directory("11-2"))
#     print(get_name("101"))
#     add('international passport', '311 020203', 'Александр Пушкин', 3)
#     print(get_directory("311 020203"))
#     print(get_name("311 020203"))
#     print(get_directory("311 020204"))


# Домашнее задание

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def people():
    doc_number = input('Введите номер документа: ')
    for dict in documents:
        if doc_number in dict['number']:
            print(f'Документ на имя {dict["name"]}')
            return dict['name']
    print("Введен несуществующий номер документа")


def shelf():
    doc_number = input('Введите номер документа: ')
    for shelf, document in directories.items():
        if doc_number in document:
            return print(f'{shelf}')
    return print('Полки с таким документом не найдено')


def list():
    for dict in documents:
        print(f'{dict["type"]} {dict["number"]} {dict["name"]}')


def add():
    document_type = input('Введите тип документа: ')
    number = input('Введите номер документа: ')
    name = input('Введите имя: ')
    shelf_number = input(str('Введите номер полки: '))
    if shelf_number in directories:
        directories[shelf_number].append(number)
        documents.append({'type': document_type, 'number': number, 'name': name})
    else:
        return print('Полки с таким номером не существует!')
        # directories[shelf_number] = [number]


def delete():
    doc_number = input('Введите номер документа\nдля удаления из каталога\nи перечня полок: ')
    for id, dict in enumerate(documents):
        if doc_number in dict['number']:
            del documents[id]
    for shelf, value in directories.items():
        if doc_number in value:
            directories[shelf].remove(doc_number)
            return print("Документ удалён")
    return print("Документ с таким номером не найден!")


def move():
    doc_number = input('Введите номер документа: ')
    for key, value in directories.items():
        if doc_number in value:
            shelf_number = input('Введите целевую полку для перемещения: ')
            if shelf_number in directories.keys():
                value.remove(doc_number)
                directories[shelf_number].append(doc_number)
                return print(f'Документ перемещен на {shelf_number} полку')
            else:
                return print('Такой номер полки отсутствует')
    return print('Такой номер документа отсутствует!')


def add_shelf():
    shelf_number = (input('Введите номер полки\nдля добавления ее в перечень: '))
    if shelf_number in directories.keys():
        print(f'Полка под номером {shelf_number} уже существует!')
    else:
        directories[shelf_number] = []
        print(f'Полка под номером {shelf_number} добавлена в перечень')


def help():
    print("""p - команда, которая спросит номер документа
и выведет имя человека, которому он принадлежит

s - команда, которая спросит номер документа
и выведет номер полки, на которой он находится

l - команда, которая выведет список всех документов
в формате passport "2207 876234" Василий Гупкин

a - команда, которая добавит новый документ в каталог и в перечень полок,
спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться

d - команда, которая спросит номер документа и удалит полностью документ из каталога
и его номер из перечня полок

m - команда, которая спросит номер документа и целевую полку
и переместит его с текущей полки на целевую

as - команда, которая спросит номер новой полки и добавит ее в перечень

h - повторный вызов справки""")


def main():
    command = input('Введите команду: ')
    if command == 'p':
        people()
    elif command == 's':
        shelf()
    elif command == 'l':
        list()
    elif command == 'a':
        add()
    elif command == 'd':
        delete()
    elif command == 'm':
        move()
    elif command == 'as':
        add_shelf()
    elif command == 'h':
        help()
    else:
        print('Введена не существующая команда!\nПовторите ввод!')


if __name__ == '__main__':
    help()
    while True:
        print()
        main()
