'''
Try-Catch in Java and C++

try-except in Python

TEST CONTINUES TO RUN THO THERE ARE ERRORS
'''


'''
Where to use try-catch?
- For example, we see a pop-up on a webpage when we enter. 
  Sometimes the pop-up appears and sometime it doesnt.
  Now, if there is pop-up, we are trying to close the pop-up in the try block, try block handles it.

'''


# TEST 1: [OUTPUT: We can see that it printed something from the except block which means there is some error on try block]
# try:
#     with open('filelog.txt','r') as reader:         # Purposefully giving a wrong file name
#         reader.read()
#
# except:
#     print('Somehow I reach this block because there is failure in try block')


# TEST 2: [OUTPUT: We can see exit code 0, that means there were no errors and nothing got executed on the except block since there were no errors on the try block.]
# try:
#     with open('test.txt','r') as reader:         # Giving the right file name
#         reader.read()
#
# except:
#     print('Somehow I reach this block because there is failure in try block')


# TEST 3: [OUTPUT: We can see the actual error message rather than us typing the message on the except block.]
# try:
#     with open('testlog.txt','r') as reader:         # Purposefully giving a wrong file name
#         reader.read()
#
# except Exception as e:
#     print(e)


# TEST 4: [OUTPUT: We can see the actual error message rather than us typing the message on the except block.]
try:
    with open('testlog.txt','r') as reader:         # Purposefully giving a wrong file name
        reader.read()

except Exception as e:
    print(e)

finally:                                            # This block of code gets executed irrespective of the try and except block.
    print('cleaning up processes')
