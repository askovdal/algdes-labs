import copy
import re
import sys
import math

raw = "".join(list(sys.stdin))

expression = (
    "(\d+)\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
)

matches = re.findall(expression, raw)

points_x = [list(map(float, p)) for p in matches]
points_y = copy.deepcopy(points_x)

# Sorted by x-coordinates
points_x.sort(key=lambda x: x[0])

# Sorted by y-coordinates
points_y.sort(key=lambda x: x[1])

print(points_x)
print(points_y)

# Divide sorted x coordinates down the middle to find line L
split = len(points_x) // 2
Q = points_x[:split]  # Left side of line L
R = points_x[split:]  # Right side of Line L

# Q sorted by x
Q_x = Q
# Q sorted by y
Q_y = sorted(Q, key=lambda x: x[1])

print(Q_x)
print(Q_y)

# R sorted by x
R_x = R
# R sorted by y
R_y = sorted(R, key=lambda x: x[1])

print(R_x)
print(R_y)


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))


# A Brute Force method to return the
# smallest distance between two points
# in P[] of size n
def find_smallest_distance(Q, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(Q[i], Q[j]) < min_val:
                min_val = dist(Q[i], Q[j])
    return min_val


def closest_pair_rec(P_x, P_y):
    if len(P_x) <= 3:
        find_smallest_distance()



"""
Closest-Pair(P)
    Construct Px and Py (O(n log n) time) 
    (p0∗, p1∗) = Closest-Pair-Rec(Px,Py)

Closest-Pair-Rec(Px, Py) 
    If |P| ≤ 3 then
        find closest pair by measuring all pairwise distances
    Endif
    
    Construct Qx, Qy, Rx, Ry (O(n) time) 
    (q0∗,q1∗) = Closest-Pair-Rec(Qx, Qy) 
    (r0∗,r1∗) = Closest-Pair-Rec(Rx, Ry)
    
    δ = min(d(q0∗,q1∗) , d(r0∗,r1∗))
    x∗ = maximum x-coordinate of a point in set Q 
    L = {(x,y) : x = x∗}
    S = points in P within distance δ of L.

    Construct Sy (O(n) time)
    For each point s ∈ Sy, compute distance from s
        to each of next 15 points in Sy
        Let s, s′ be pair achieving minimum of these distances 
        (O(n) time)
        
    If d(s,s′) < δ then 
        Return (s,s′)
    Else if d(q0∗,q1∗) < d(r0∗,r1∗) then 
        Return (q0∗,q1∗)
    Else
        Return (r0∗,r1∗)
    Endif
"""
