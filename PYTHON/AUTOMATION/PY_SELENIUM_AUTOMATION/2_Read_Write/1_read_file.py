'''
NOTE:
    - When you open a file, always close the file to avoid errors
    - When you read a line or the characters in the line, it will start where u stopped reading them.
            EXAMPLE:
                abc     [Text file contents]
                efg
                hij

            print(var_name.read(5))     --->    Reads till e
            [OUTPUT]
            abc
            e

            print(var_name.read(2))     --->    Reads till g    (because it starts from where it stopped reading previously)
            [OUTPUT]
            fg
'''

file_content = open('text_file.txt')     # Opening a file

#print(file_content.read())              # Reading all contents of file

#print(file_content.read(3))             # Reading the first 3 bytes/chara of the file

#print(file_content.read(7))             # Reading the first 7 bytes of the file (\n is also a character)

#print(file_content.readline(10))        # Reading one line at a time, for reading 2 lines, we need to use readline() twice.
#print(file_content.readline(4))



# 1. READLINE METHOD()
# PRINT LINE BY LINE USING READLINE METHOD:
# line = file_content.readline()
# while line!="":
#     print(line)
#     line = file_content.readline()



# 2. READLINES METHOD()
# OTHER WAY TO PRINT LINE BY LINE USING READLINES METHOD:

'''
values = ['zebra', 'pikachoo', 'abc', '23', '3.41', '3+2j', 'elephant', 'rhino']
'''
for line in file_content.readlines():
    print(line)


file_content.close()                     # Closing a file