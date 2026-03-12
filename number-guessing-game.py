from random import randint


def is_valid(num, n_max):
    if not num.isdigit():
        return False
    num = int(num)
    return 0 < num < n_max + 1


def is_maximum_valid(n_max):
    return n_max.isdigit() and int(n_max) > 1


def new_target(n_max):
    return randint(1, n_max)


def get_valid_maximum():
    maximum = input("Select the maximum number that can be guessed: ")
    while not is_maximum_valid(maximum):
        maximum = input(
            "Select the maximum NUMBER that can be guessed (it must be greater than 1:) "
        )
    return int(maximum)


def play_game():

    n_max = get_valid_maximum()

    target = new_target(n_max)
    counter = 0

    while True:
        entered = input(f"Enter a number from 1 to {n_max} inclusive: ")

        if is_valid(entered, n_max):
            entered = int(entered)
            counter += 1

            if entered < target:
                print("Your number is LESS than the secret number, try again!")
            elif entered > target:
                print("Your number is GREATER than the secret number, try again!")
            else:
                print(f"You guessed it, congratulations! Number of attempts: {counter}")
                play_more = input("Do you want play more? Yes: Y, No: N ")

                if play_more.upper() == "Y":
                    n_max = get_valid_maximum()
                    target = new_target(n_max)
                    counter = 0

                else:
                    print(
                        "Thank you for playing the Number Guessing Game. See you again..."
                    )
                    break

        else:
            print(f"How about we enter a whole number from 1 to {n_max}?")


print("Welcome to the Number Guessing Game!")
play_game()
