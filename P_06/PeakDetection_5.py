# l = [10, 45, 34, 43, 56, 57, 35]

l=[1,2,1,3,5,2,1]
def isPeak(l):
    k = 1
    newList = []
    for i, x in enumerate(l, 1):
        if l[i] > l[i-1]:
            newList.append(l[i])
        elif l[i] < l[i-1]:
            k+=1
        print(k)
    
isPeak(l[1:])
