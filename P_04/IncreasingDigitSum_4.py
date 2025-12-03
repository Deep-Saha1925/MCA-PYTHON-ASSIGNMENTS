l = input("Enter string: ").split()
newL = []
digit_sum_list = []

def convert_digit(s):
    a = 0
    for ch in s:
        a = a*10 + (ord(ch)-48)
        
    return a

def digit_sum(a):
    summ = 0
    while a != 0:
        summ += a%10
        a = a//10
        
    return summ
        

for el in l:
    dig = convert_digit(el)
    newL.append(dig)
    digit_sum_list.append(digit_sum(dig))
    
for i in range(1, len(digit_sum_list)):
    if digit_sum_list[i] > digit_sum_list[i-1]:
        print(l[i])