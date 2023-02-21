FAIL = '\033[91m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'

menu = [(1, "Dodaj studenta"),
        (2, "Usuń studenta"),
        (3, "Wyświetl studentów"),
        (4, "Zapisz do pliku"),
        (5, "Wczytaj z pliku"),
        (6, "Zakończ program")]

student_db = []


def show_menu(list_of_tuples):
    for i in menu:
        print(i[0], i[1])


def add_student(local_db):
    pass


def delete_student(local_db):
    pass


def sorted_students_list(local_db):
    pass


def save_db_to_file(patch, local_db):
    pass


def open_db_from_file(patch, local_db):
    pass


while True:
    show_menu(menu)
    try:
        user_input = int(input("Wybierz opcję: "))

        if user_input == menu[0][0]:
            add_student(student_db)
        elif user_input == menu[1][0]:
            delete_student(student_db)
        elif user_input == menu[2][0]:
            sorted_students_list(student_db)
        elif user_input == menu[3][0]:
            save_db_to_file('students.csv', student_db)
            print()
        elif user_input == menu[4][0]:
            open_db_from_file('students.csv', student_db)
            print()
        elif user_input == menu[5][0]:
            print(f"{OKGREEN}Zamykam program{ENDC}")
            break
        else:
            raise ValueError
    except ValueError:
        print(f"{FAIL}Podałeś błędną opcję{ENDC}")
