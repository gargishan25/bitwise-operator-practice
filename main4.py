#Write a Program to find two numbers that are odd occurring
nums = [4,2,4,5,2,3,3,1]
result = 0
for i in range(len(nums)):
    nums.sort()
    result = result^nums[i]
    if result == 0:
        nums.remove(nums[i])
    if len(nums) == 2:
        break
print(nums)