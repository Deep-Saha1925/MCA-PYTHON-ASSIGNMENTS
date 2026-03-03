def bubble_sort(a, n):
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
a = [5, 1, 2, 3, 8]
bubble_sort(a, len(a))
print(a)