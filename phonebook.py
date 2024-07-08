
def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as file:
        for record in phone_book:
            line = ','.join(record.values())
            file.write(f'{line}\n')

def print_result(phone_book):
    for record in phone_book:
        print(', '.join(record.values()))

def find_by_lastname(phone_book, lastname):
    return [record for record in phone_book if record['Фамилия'] == lastname]

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.strip().split(',')))
    phone_book.append(record)

def change_number(phone_book, lastname, new_number):
    for record in phone_book:
        if record['Фамилия'] == lastname:
            record['Телефон'] = new_number
    return phone_book

def delete_by_lastname(phone_book, lastname):
    return [record for record in phone_book if record['Фамилия'] != lastname]

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер абонента\n"
          "4. Удалить абонента\n"
          "5. Добавить абонента\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу\n"
          "8. Копировать строку из одного файла в другой")
    choice = int(input())
    return choice

def copy_line(source_file, target_file, line_number):
    with open(source_file, 'r', encoding='utf-8') as src:
        lines = src.readlines()
    if line_number <= len(lines):
        line_to_copy = lines[line_number - 1]
        with open(target_file, 'a', encoding='utf-8') as tgt:
            tgt.write(line_to_copy)
    else:
        print("Неверный номер строки.")

def work_with_phonebook():
    phone_book = read_txt('phon.txt')
    choice = show_menu()

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            lastname = input('Введите фамилию: ')
            print(find_by_lastname(phone_book, lastname))
        elif choice == 3:
            lastname = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            phone_book = change_number(phone_book, lastname, new_number)
        elif choice == 4:
            lastname = input('Введите фамилию: ')
            phone_book = delete_by_lastname(phone_book, lastname)
        elif choice == 5:
            user_data = input('Введите данные (Фамилия, Имя, Отчество, Телефон, Описание): ')
            add_user(phone_book, user_data)
        elif choice == 6:
            write_txt('phon.txt', phone_book)
        elif choice == 8:
            line_number = int(input('Введите номер строки для копирования: '))
            copy_line('phon.txt', 'copied_lines.txt', line_number)

        choice = show_menu()

work_with_phonebook()
