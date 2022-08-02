from metods import filename
from metods import searchcontact
from metods import newcontact

def main_menu(): 
    print( "\nMAIN MENU\n") 
    print( "1. Показать все существующие контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Поиск среди контактов") 
    print( "4. Выход") 
    choice = input("Пожалуйста сделайте выбор: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "В телефонной книге нет контакта.") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "2": 
        newcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "3": 
        searchcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif choice == "4": 
        print("Благодарим вас за использование телефонной книги!") 
    else: 
        print( "Пожалуйста, предоставьте корректные данные!\n") 
        enter = input( "Нажмите Enter, чтобы продолжить ...") 
        main_menu() 