def find_first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num-1] = -abs(nums[num-1])
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    return  n + 1

nums =[-3,-4,1,2,3,1,-3]
print(find_first_missing_positive(nums))