d1 = {'key1': 1, 'key2': 3, 'key3': 2}
d2 = {'key1': 1, 'key2': 2}

for d in d2:
    if d in d1 and d1[d] == d2[d]:
        print(d, ":", d1[d], "is present in both x and y")