def fibo(n):
    
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
        
    return fibo(n-1) + fibo(n-2)

n = 20
l = []
for i in range(n):
    l.append(fibo(i))
    
    
for i in range(1, n-1):
    print(l[i+1], '/' ,l[i], '=', l[i+1]/l[i])
    
# print(l)