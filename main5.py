#Write a Program to check if two numbers are equal without using any comparison operator.
num1 = int(input("Enter a number. "))
num2 = int(input("Enter another number. "))
if num1 ^ num2:
    print("They are not equal.")
else:
    print("They are equal.")