def count_qualities(grid, i, j, N, M):
    directions = [(-1,-1), (-1,0), (-1,1),
                  (0,-1),         (0,1),
                  (1,-1), (1,0), (1,1)]
    
    count = 0
    
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        
        if 0 <= ni < N and 0 <= nj < M:
            # Ignore Sam's house
            if not (ni == 0 and nj == 0):
                if grid[ni][nj] == 1:
                    count += 1
                    
    return count


def distance_from_sam(i, j):
    # Chebyshev distance
    return max(abs(i - 0), abs(j - 0))


def find_bride():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_qualities = -1
    min_distance = float('inf')
    best = []

    for i in range(N):
        for j in range(M):

            # Skip Sam's house
            if i == 0 and j == 0:
                continue

            if grid[i][j] == 1:
                qualities = count_qualities(grid, i, j, N, M)
                distance = distance_from_sam(i, j)

                if qualities > max_qualities:
                    max_qualities = qualities
                    min_distance = distance
                    best = [(i, j)]

                elif qualities == max_qualities:
                    if distance < min_distance:
                        min_distance = distance
                        best = [(i, j)]
                    elif distance == min_distance:
                        best.append((i, j))

    if max_qualities == -1:
        print("No suitable girl found")
    elif len(best) > 1:
        print("Polygamy not allowed")
    else:
        r, c = best[0]
        print(f"{r+1}:{c+1}:{max_qualities}")


find_bride()