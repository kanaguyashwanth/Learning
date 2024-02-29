# Exercise - Prime Number Checker

#Write your code below this line 👇


def prime_checker(number):
    
    prime_flag = True
    for n in range(2, number):
        if number%n == 0:
            prime_flag = False
    if prime_flag:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)