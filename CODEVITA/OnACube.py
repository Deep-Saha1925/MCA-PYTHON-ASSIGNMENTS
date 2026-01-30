import math

# def face_of(p):
#     x, y, z = p
#     if z == 10:
#         return 'top'
#     if x == 0:
#         return 'left'
#     if x == 10:
#         return 'right'
#     if y == 0:
#         return 'front'
#     if y == 10:
#         return 'back'

# def same_face_arc(p1, p2):
#     # chord length on the face
#     chord = math.dist(p1, p2)
#     # arc subtends 60 degrees = pi/3 radians
#     return chord * math.pi / 3

# def unfold_distance(p1, p2):
#     x1, y1, z1 = p1
#     x2, y2, z2 = p2

#     distances = []

#     # XY plane
#     distances.append(math.dist((x1, y1), (x2, y2)))

#     # Unfold via XZ plane
#     distances.append(math.dist((x1, z1), (x2, z2)))

#     # YZ plane
#     distances.append(math.dist((y1, z1), (y2, z2)))

#     return min(distances)

# def total_distance(points):
#     total = 0.0

#     for i in range(len(points) - 1):
#         p1 = points[i]
#         p2 = points[i + 1]

#         if face_of(p1) == face_of(p2):
#             d = same_face_arc(p1, p2)
#         else:
#             d = unfold_distance(p1, p2)

#         total += round(d, 2)

#     return total

# N = int(input())
# coords = list(map(float, input().split(',')))

# points = []
# for i in range(0, len(coords), 3):
#     points.append((coords[i], coords[i+1], coords[i+2]))

# print(total_distance(points))




"""
import math

def arcDist(a1,b1,a2,b2):
    return math.pi * math.sqrt((a1-a2)**2 + (b1-b2)**2) / 3

def distSameFace(A, B):
    if(A[0] == B[0]):
        return arcDist(A[1],A[2],B[1],B[2])
    elif(A[1] == B[1]):
        return arcDist(A[0],A[2],B[0],B[2])
    else:
        return arcDist(A[0],A[1],B[0],B[1])


# face
def currFace(x,y,z):
    if(x==0):
        return 'd'
    elif(x==10):
        return 'b'
    elif(y==0):
        return 'a'
    elif(y==10):
        return 'c'
    else:
        return 'e'

def oppFace(x,y):
    l = [x,y]

    if ('a' in l and 'c' in l):
        return True
    elif ('b' in l and 'd' in l):
        return True
    else:
        return False

def distSideWall(A,B):
    x1 = A[0]
    y1 = A[1]
    z1 = A[2]

    x2 = B[0]
    y2 = B[1]
    z2 = B[2]

    d = math.sqrt((abs(x2-x1)+abs(y2-y1))**2 + (z2-z1)**2)
    return d

def distOppWall(A,face_a,B,face_b):

    #Method 1
    #if it's bw 'a' and 'c'
    if face_a == 'a' or face_b == 'a':
        dist1 = math.sqrt((30-A[0]-B[0])**2 + (A[2]-B[2])**2)
    #if it's bw 'b' and 'd'
    else:
        dist1 = math.sqrt((30-A[1]-B[1])**2 + (A[2]-B[2])**2)

    #Method 2
    if face_a == 'a' or face_b == 'a':
        dist2 = math.sqrt((10+A[0]+B[0])**2 + (A[2]-B[2])**2)
    #if it's bw 'b' and 'd'
    else:
        dist2 = math.sqrt((10+A[1]+B[1])**2 + (A[2]-B[2])**2)

    #Method 3 - through top face
    #if it's bw 'a' and 'c'
    if face_a == 'a' or face_b == 'a':
        dist3 = math.sqrt((30-A[2]-B[2])**2 + (A[0]-B[0])**2)
    #if it's bw 'b' and 'd'
    else:
        dist3 = math.sqrt((30-A[2]-B[2])**2 + (A[1]-B[1])**2)

    return min(dist1,dist2,dist3)

def distToTop(A,face_a,B,face_b):
    l = [face_a,face_b]
    x1 = A[0]
    y1 = A[1]
    z1 = A[2]

    x2 = B[0]
    y2 = B[1]
    z2 = B[2]

    # if 'a' or 'c' to 'e'
    if 'a' in l or 'c' in l:
        d = math.sqrt( (abs(z2-z1)+abs(y2-y1))**2 + (x2-x1)**2)
    #if 'b' or 'd' to 'e'
    else:
        d = math.sqrt( (abs(z2-z1)+abs(x2-x1))**2 + (y2-y1)**2)

    return d

def travel(A,B):
    face_a = currFace(A[0],A[1],A[2])
    face_b = currFace(B[0],B[1],B[2])

    if face_a == face_b :
        return distSameFace(A,B)
    elif (face_a !='e' and face_b !='e'):
        if oppFace(face_a,face_b) == False:
            return distSideWall(A,B)
        else:
            return distOppWall(A,face_a,B,face_b)
    else:
        return distToTop(A,face_a,B,face_b)

########################## Driver Code ############################

N = int(input()) # total number of points the beatle visits
lp = [] #list of list of points

# takes input as string, splits it, converts it into floats, and then makes a list of them
a = list(map(float, input().split(',')))

#coverts 'a' into list of points and puts them in lp
for i in range(N):
    k = 3*i
    b = [a[k],a[k+1],a[k+2]]
    lp.append(b)

totalDist = 0
for k in range(1,N):
    totalDist += travel(lp[k-1],lp[k])

print(round(totalDist,2))
"""

print(round(math.dist((1,1,10), (2,1,10)),2))