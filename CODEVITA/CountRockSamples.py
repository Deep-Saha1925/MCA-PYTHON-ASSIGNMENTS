def calculate_rock_samples():
    n, r = map(int, input("Enter sample size and ranges: ").split())
    samples = list(map(int, input("Enter samples: ").split()))
    ans = []
    for _ in range(r):
        x, y = map(int, input(f"Enter range {_+1}: ").split())
        a = 0
        for sample in samples:
            if sample >= x and sample <= y:
                a += 1
                
        ans.append(a)
    
    print(ans)
    
calculate_rock_samples()