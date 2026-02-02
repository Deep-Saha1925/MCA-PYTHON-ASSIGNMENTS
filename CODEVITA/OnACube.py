import math

def same_face(p1, p2):
    for i in range(3):
        if p1[i] == p2[i] and p1[i] in (0, 10):
            return True
    return False

def euclidean(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(3)))

def surface_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    # Possible surface unfoldings (excluding bottom face z=0)
    distances = []

    # Top + sides
    distances.append(math.hypot(x1 - x2, y1 - y2) + abs(z1 - z2))
    distances.append(math.hypot(x1 - x2, z1 - z2) + abs(y1 - y2))
    distances.append(math.hypot(y1 - y2, z1 - z2) + abs(x1 - x2))

    return min(distances)

def total_distance(points):
    total = 0

    for i in range(len(points) - 1):
        p1, p2 = points[i], points[i + 1]

        if same_face(p1, p2):
            d = (math.pi / 3) * euclidean(p1, p2)
        else:
            d = surface_distance(p1, p2)

        total += round(d, 2)

    return f"{total:.2f}"

n = int(input())
coords = list(map(float, input().split(',')))

points = []
for i in range(0, len(coords), 3):
    points.append((coords[i], coords[i+1], coords[i+2]))

print(total_distance(points))