import math

A = list(map(float, input().split()))
B = list(map(float, input().split()))
C = list(map(float, input().split()))
D = list(map(float, input().split()))

X = [A[i]-B[i] for i in range(3)]
Y = [C[i]-B[i] for i in range(3)]
Z = [D[i]-C[i] for i in range(3)]

def cross(a,b):
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]

def dot(a,b):
    return sum(a[i]*b[i] for i in range(3))

def mag(v):
    return math.sqrt(dot(v,v))

n1 = cross(X,Y)
n2 = cross(Y,Z)

angle = math.degrees(math.acos(dot(n1,n2)/(mag(n1)*mag(n2))))

print("%.2f" % angle)