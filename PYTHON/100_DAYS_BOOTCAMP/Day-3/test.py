# CODING EXERCISE - Pizza Order

'''
Small Pizza:  $15
Medium Pizza: $20
Large Pizza:  $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: +$1

INPUT:
size: "L"
add_pepperoni = "Y"
extra_cheese = "N"

OUTPUT:
Your final bill is: $28.
'''


size = input ('Enter size of Pizza(S/M/L): ')
pep = input('Add pepperoni? (Y or N): ')
xtra_cheese = input('Extra cheese? (Y or N): ')
bill = 0

if size == 'S':
    bill = 15
    if pep == 'Y':
        bill+=2

elif size == 'M':
    bill = 20
    if pep == 'Y':
        bill+=3

elif size == 'L':
    bill = 25
    if pep == 'Y':
        bill+=3

if xtra_cheese == 'Y':
    bill+=1
    print(f"Your final bill is: {bill}")
else:
    print(f"Your final bill is: {bill}")


