'''
To define multiple variables in a single line,
x=3; y=5.2; lang_name="Python Scripting"
'''
x=3
y=5.2
lang_name="Python3"

#Printing all these variables

#Method_1 - Prints all in same line
print(x,y,lang_name)
print("\n")

#Method_2 - Prints all in same line, here in the format, we provide the order in which we want to print
print("{} {} {}".format(x,y,lang_name))
print("{} {} {}".format(y,x,lang_name))
print("{} {} {}".format(lang_name,x,y))
print("\n")

#Method_3 - Prints all in different line, NOTE: \n should always be inside the double quotes - "\n"
print("{} \n{} \n{}".format(x,y,lang_name))
print("\n")

#Method_4
'''Prints all in same line, alternative for .format()
   NOTE: When using \n, if a space is present after/before the word, it will be considered while printing the output
'''
print(f"x value is: {x} \ny value is: {y} \nLanguage is: {lang_name}")
print("\n")


#Method_5 - Storing the output in a variable and printing it
my_required_output = (f"Language is: {lang_name} \ny value is: {y} \nx value is: {x}")
print(my_required_output)
print("\n")

#Method_6
print('X value is: {}\nY value is: {}'.format(x,y))
