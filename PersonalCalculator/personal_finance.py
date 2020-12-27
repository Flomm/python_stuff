# Functions
import time


def program_start():
    start_data = input(
        'Welcome to the Super Expense Calculator 1980, your best friend when it comes to calculating personal expenses! \n  Press enter to continue.')


def create_expense_list():
    is_list = True
    while is_list == True:
        try:
            list_data = input(
                "Please type in your expenses one at a time and press enter to add to the list. \n When you're ready, please type 'R' to continue.\n Your expense: ")
            if list_data.upper() == "R" and len(list_of_expenses) != 0:
                is_list = False
                return(list_of_expenses)

            elif list_data.upper() == "R" and len(list_of_expenses) == 0:
                print(".")
                print(".")
                print("You haven't added any items yet.")

            elif (float(list_data) >= 1000000000000000000000000000000000000000000000000):
                print(".")
                print(".")
                print("The amount is too high!")

            else:
                list_of_expenses.append(float(list_data))
                print(".")
                print(".")
                print(f'Your current list: {stringify(list_of_expenses)}')

        except ValueError:
            print("Please enter a number or R.")


def choose_from_menu(list_of_expenses):

    menu_on = True
    while menu_on == True:
        print(" ")
        print(" ")
        try:
            menu_data = input(
                "Please choose from the below options:\n 1. Sum of your expenses \n 2. Your biggest expense \n 3. Your smallest expense \n 4. Your average expense \n 5. Exit \n Your choice: ")
            if int(menu_data) == 1:
                print(".")
                print(".")
                print(
                    f'You spent {finance_calculator(list_of_expenses)} dollars.')
                time.sleep(2)
                menu_on = False
                back_to_main()

            elif int(menu_data) == 2:
                print(".")
                print(".")
                print(
                    f'Your greatest expense was {greatest_expense_calculator(list_of_expenses)} dollars.')
                time.sleep(2)
                menu_on = False
                back_to_main()

            elif int(menu_data) == 3:
                print(".")
                print(".")
                print(
                    f'Your smallest expense was {smallest_expense_calculator(list_of_expenses)} dollars.')
                time.sleep(2)
                menu_on = False
                back_to_main()

            elif int(menu_data) == 4:
                print(".")
                print(".")
                print(
                    f'Your average expense was {average_calculator(list_of_expenses)} dollars.')
                time.sleep(2)
                menu_on = False
                back_to_main()

            elif int(menu_data) == 5:
                list_of_expenses = []
                menu_on = False

            else:
                print(".")
                print(".")
                print(
                    "This is not a correct number. Please choose from the menu options!")
                continue

        except ValueError:
            print("Please enter a correct number!")


def finance_calculator(add_list):
    sum_spent = 0
    for i in range(len(add_list)):
        sum_spent += add_list[i]
    return sum_spent


def greatest_expense_calculator(add_list):
    greatest_expense = 0

    for i in range(len(add_list)):
        if greatest_expense >= add_list[i]:
            continue

        elif add_list[i] > add_list[i - 1]:
            greatest_expense = add_list[i]

        else:
            greatest_expense = add_list[i - 1]

    return greatest_expense


def smallest_expense_calculator(add_list):

    for i in range(len(add_list)):
        smallest_expense = 1000000000000000000000000000000000000000000000000
        if smallest_expense <= add_list[i]:
            continue

        elif add_list[i] < add_list[i - 1]:
            smallest_expense = add_list[i]

        else:
            smallest_expense = add_list[i - 1]

    return smallest_expense


def average_calculator(add_list):
    average_expense = 0
    average_expense = finance_calculator(
        list_of_expenses) / len(list_of_expenses)
    return average_expense


def back_to_main():
    back_menu = True
    while back_menu == True:
        back_to = input(
            "If you'd like to go back to the main menu, enter Y. \n If you'd like to exit, enter E. \n")

        if back_to.upper() == "Y":
            back_menu = False
            choose_from_menu(list_of_expenses)

        elif back_to.upper() == "E":
            back_menu = False
            break

        else:
            print("Please enter a valid command!")


def stringify(list1):
    string = [str(i) for i in list1]
    res = str(", ".join(string))
    return res


# Variables
menu_numbers = [1, 2, 3, 4, 6]
list_of_expenses = []

# Game


program_start()

while True:
    list_of_expenses = []

    create_expense_list()

    print(f'Your list of expenses is: {stringify(list_of_expenses)}')
    time.sleep(2)
    choose_from_menu(list_of_expenses)

    print(" ")
    print(" ")
    exit = input(
        "Are you sure you want to exit, or you'd rather add a new list? Y(exit) or N   ")

    if exit.upper() == "N":
        continue

    else:
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("Thank you for choosing our calculator. See you soon!")
        break
