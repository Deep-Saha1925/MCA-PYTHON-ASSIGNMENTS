# Using LOG
# import math

# T = int(input().strip())
# for _ in range(T):
#     N = int(input().strip())
#     print(math.ceil(math.log2(N + 1)))



def min_denominations(N):
    coverage = 0
    count = 0

    while coverage < N:
        coin = coverage + 1
        coverage += coin
        count += 1

    return count

T = int(input())
for _ in range(T):
    N = int(input())
    print(min_denominations(N))
