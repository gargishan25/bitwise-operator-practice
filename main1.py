#Write a Program to find the number of zero bits and one bit present in a number.
num = int(input("Enter a number. "))
# bits = []
count0 = 0
count1 = 0
# while num>=1:
#     bits.append(num%2)
#     num //= 2
# for i in range(len(bits)):
#     if bits[i] == 0:
#         count0 +=1
#     if bits[i] == 1:
#         count1 +=1
while num>=1:
    if num&1 == 0:
        count0+=1
    else:
        count1+=1
    num >>= 1
print(f"There are {count1} 1s.")
print(f"There are {count0} 0s.")