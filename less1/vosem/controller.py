import model
import view

def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Добавить контакт')
        print('2. Удалить контакт')
        print('3. Изменить контакт')
        print('4. Найти контакт')
        print('5. Сохранить файл')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                add_contact()
                print('\nКонтакт добавлен!\n')
            case 2:
                remove_contact()
                print('\nКонтакт удален!\n')
            case 3:
                change_contact()
                print('\nКонтакт изменен!\n')
            case 4:
                search_contact()
                print('\nКонтакт найден!\n')
            case 5:
                save_file()
                print('\nФайл сохранен!\n')
            case 0:
                break

def start():
    open_file()
    view.printPhoneBook()
    main_menu()

def open_file():
    with open(model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        model.phonebook = contacts_list

def save_file():
    with open(model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    model.phonebook.append(contact)
    view.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    model.phonebook.pop(choice)
    view.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    model.phonebook.insert(choice, ';'.join(contact))
    view.printPhoneBook()

def search_contact():
    
    choice = input('Ищем: ')
    for i, item in enumerate(model.phonebook):
        if choice in item:
            print(i , item)