def sumAllNums(nums):
    s = 0
    for n in nums:
        s += n
        
    return s

nums = [1,3,4,5,6,7,9]
print("Sum of list elements:", sumAllNums(nums))