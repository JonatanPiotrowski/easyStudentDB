FAIL = '\033[91m'
ENDC = '\033[0m'
OKGREEN = '\033[92m'

menu = [(1, "Add student"),
        (2, "Remove student"),
        (3, "Show students"),
        (4, "Save database to file"),
        (5, "Read database from file"),
        (6, "End program")]

student_db = []


def show_menu(list_of_tuples):
    for i in menu:
        print(i[0], i[1])


def add_student(user_list):
    while True:
        cancel = False
        s_f_name = input("Enter first name: ")
        s_l_name = input("Enter last name: ")
        try:
            s_index = int(input("Enter album number: "))
            if user_list is not None:
                for student in user_list:
                    if s_index == student[2]:
                        print(f"{FAIL}The student with the given album number is already in the database!{ENDC}")
                        cancel = True
            if cancel:
                break
        except ValueError:
            print(f"{FAIL}Given value is not a number!{ENDC}")
            break
        try:
            s_grade = float(input("Give rating: "))
            if s_grade < 2 or s_grade > 5:
                raise ValueError
        except ValueError:
            print(f"{FAIL}Given value is not a school grade!{ENDC}")
            break
        user_list.append((s_f_name.title(), s_l_name.title(), s_index, s_grade))
        break


def delete_student(user_list):
    try:
        student_not_find = True
        del_st_id = int(input("Enter the number of the student's album to be deleted: "))
        for student in user_list:
            if del_st_id == student[2]:
                user_list.remove(student)
                print(f"{OKGREEN}Successfully removed student{ENDC}")
                student_not_find = False
        if student_not_find:
            print(f"{FAIL}student id {del_st_id} not found.{ENDC}")
    except ValueError:
        print(f"{FAIL}Wrong value was given!{ENDC}")


def sorted_students_list(local_db):
    pass


def save_db_to_file(patch, local_db):
    pass


def open_db_from_file(patch, local_db):
    pass


while True:
    show_menu(menu)
    try:
        user_input = int(input("Choose option: "))

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
            print(f"{OKGREEN}Closing program{ENDC}")
            break
        else:
            raise ValueError
    except ValueError:
        print(f"{FAIL}You entered the wrong option{ENDC}")
