num = int(input("Enter a number. "))
if num & (num-1) == 0:
    print("The number is a power of 2.")
else:
    print("The number is not a power of 2.")
# while new_num>=2:
#     new_num = num>>divider
#     if new_num == 2:
#         print("The number is a power of 2.")
#         break
#     if int(new_num) != new_num:
#         print("The number is not a power of 2.")
#         break