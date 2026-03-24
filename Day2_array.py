nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)

# Optimized Solution

# nums = [2,7,11,15]
# target = 9
# num_dict = {}

# for i in range(len(nums)):
#     complement = target - nums[i]
    
#     if complement in num_dict:
#         print(num_dict[complement], i)
    
#     num_dict[nums[i]] = i
