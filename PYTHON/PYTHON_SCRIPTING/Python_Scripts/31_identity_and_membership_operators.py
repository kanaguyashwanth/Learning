#IDENTITY OPERATORS:

''' It is of two types:
        - type(x) is type(y)
        - type(x) is not type(y)
'''

#EXAMPLE: [Python Terminal - Filename: membership_operator.py]
'''
>>> x=6
>>> y='hi'
>>> print(x)
6
>>> print(y)
hi
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'str'>
>>> type(x) is type(y)
False
>>> y=7
>>> type(x) is type(y)
True
>>> y='hi'
>>> type(x) is type(y)
False
>>> type(x) is not type(y)
True
'''

#MEMBERSHIP OPERATORS:
''' It is of two types:
        - in
        - not in
'''

#EXAMPLE: [Python Terminal - Filename: membership_operator.py]
'''
valid_java = ['1.6', '1.7', '1.8', '1.9']
host_java = '1.7'

if host_java in valid_java:
    print("host deployed of valid java version")
else:
    print("host deployed with invalid java version")


db_users = ['db_admin', 'db_conf', 'db_installation']
random_user = "db_admin"

if random_user in db_users:
    print("yes this user is allowed to start db")
else:
    print("this user is not a valid user to start db")
'''

