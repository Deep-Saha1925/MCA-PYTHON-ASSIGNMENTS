import math

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(math.ceil(math.log2(N + 1)))
