# # calling a function
# def my_func():
#     print("A")
#     print("B")
#     print("C")
#
# my_func()


# Reeborg's World
def starting():
    str_1 = input("Do you want to move or turn: ")

    if str_1 == 'move':
        n = int(input("Enter number of steps: "))
        for x in range(0, n - 1):
            move()

    if str_1 == 'turn':
        str = input("Enter direction: ")
        if str == 'left':
            turn_left()

        if str == 'right':
            turn_right()

        if str == 'opposite':
            turn_left()
            turn_left()

    starting()

starting()