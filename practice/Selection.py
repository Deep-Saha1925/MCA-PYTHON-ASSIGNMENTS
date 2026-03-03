def selection_sort(a, n):
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                
a = [5, 1, 2, 3, 8]
selection_sort(a, len(a))
print(a)