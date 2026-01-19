def mulAllNums(nums):
    s = 1
    for n in nums:
        s *= n
        
    return s

nums = [1,3,4,5,6,7,9]
print("Multiplication of list elements:", mulAllNums(nums))