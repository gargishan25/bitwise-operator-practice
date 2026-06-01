# Write a Program to check if the Nth bit is set or not.
num = int(input("Enter a number. "))
nth = int(input("What value do you want to go until? "))
print(f"The 1st bit is {num - nth*(num>>nth)}.")