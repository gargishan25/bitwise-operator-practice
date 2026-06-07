# Write a Program to find the element not making a pair.
nums = [2,5,7,5,7]
result = 0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)-1):
#         if nums[i]^nums[j]:
#             nums.remove(nums[i])
#             nums.remove(nums[j])
# print(nums)
for i in range(len(nums)):
    result = result^nums[i]
print(result)