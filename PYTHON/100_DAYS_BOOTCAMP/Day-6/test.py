# # calling a function
# def my_func():
#     print("A")
#     print("B")
#     print("C")
#
# my_func()

# CHALLENGE - 1
# # Reeborg's World - Hurdle Jump - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# USING FOR LOOP
# def turn_right():
#     for i in range(3):
#         turn_left()
#
# for i in range(6):
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# USING WHILE LOOP
# def turn_right():
#     for i in range(3):
#         turn_left()
#
# n_hurdles = 6
#
# while n_hurdles > 0:
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#     n_hurdles -= 1

# CHALLENGE - 2
# # Hurdle stops at anytime - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
# def turn_right():
#     for i in range(3):
#         turn_left()
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# switch = True
# while (switch):
#     jump()
#     if at_goal():
#         switch = False
#     else:
#         switch = True

# CHALLENGE 3 - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
# def turn_right():
#     for i in range(3):
#         turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while not at_goal():
#     if front_is_clear():
#         while(not wall_in_front()):
#             move()
#     else:
#         jump()



# CHALLENGE 4 - https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# def turn_right():
#     for i in range(3):
#         turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
#
#
# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         while (not wall_in_front()):
#             move()
#
#     else:
#         jump()