def min_coins(N):
    coverage = 0
    total_value = 0

    c1 = c2 = c5 = 0

    while coverage < N:
        if 5 <= coverage + 1 and total_value + 5 <= N:
            c5 += 1
            total_value += 5
            coverage += 5

        elif 2 <= coverage + 1 and total_value + 2 <= N:
            c2 += 1
            total_value += 2
            coverage += 2

        else:
            c1 += 1
            total_value += 1
            coverage += 1

    total_coins = c1 + c2 + c5
    print(total_coins, c5, c2, c1)


N = int(input())
min_coins(N)