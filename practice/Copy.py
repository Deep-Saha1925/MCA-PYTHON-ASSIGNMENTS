import copy

original = [[1, 2, 3], [4, 5, 6]]
s = copy.copy(original)
# s = copy.deepcopy(original)

s[0][0] = 99
print(original)