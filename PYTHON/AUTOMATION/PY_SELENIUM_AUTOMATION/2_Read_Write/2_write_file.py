'''
file_content = open('text_file.txt')    # Opening a file
.
.
.
file_content.close()                    # Closing a file



a.k.a



with open('text_file.txt') as file_content:


'''


'''
WHAT TO DO?
-Read the file and store all the lines in list
-Reverse the list
-Write the list back to the file
'''


# Opening a file in READ-MODE:
with open('text_file.txt', 'r') as reader:      # Here, reader is exactly like file_content
    content = reader.readlines()                # ['zebra', 'pikachoo', 'abc', '23', '3.41', '3+2j', 'elephant', 'rhino']
    reversed(content)                           # ['rhino', 'elephant', '3+2j', '3.14', '23', 'abc', 'pikachoo', 'zebra']
    with open('text_file.txt', 'w') as writer:
        for line in reversed(content):          # ['rhino', 'elephant', '3+2j', '3.14', '23', 'abc', 'pikachoo', 'zebra']
            writer.write(line)