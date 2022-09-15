import copy
import re
import sys
import math

raw = "".join(list(sys.stdin))

expression = (
    "(\d+)\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
)

matches = re.findall(expression, raw)

def euclidian_distance(p1, p2):
    return math.sqrt((p1[1] - p2[1]) * (p1[1] - p2[1]) + (p1[2] - p2[2]) * (p1[2] - p2[2]))

def smallest_dist(P, n): 
    min_val = float('inf') # base value 
    p_0 = 0 
    p_1 = 0
    for i in range(n): # Nested loop to compare all points in the list (max 3 points = max )
        for j in range(i + 1, n):
            if euclidian_distance(P[i], P[j]) < min_val:
                min_val = euclidian_distance(P[i], P[j])
                p_0 = P[i]
                p_1 = P[j]
    return min_val

def smallest_dist_middle(S_y, n):
    min_val = float('inf')
    p_0 = 0 
    p_1 = 0
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if count == 15:
                count = 0
                break
            elif euclidian_distance(S_y[i], S_y[j]) < min_val:
                min_val = euclidian_distance(S_y[i], S_y[j])
                p_0 = S_y[i]
                p_1 = S_y[j]
            count += 1
    return min_val

def closest_pair(P):
    p_x = [list(map(float, p)) for p in P]
    p_y = copy.deepcopy(p_x)
    # Sorted by x-coordinates
    p_x.sort(key=lambda x: x[1])
    # Sorted by y-coordinates
    p_y.sort(key=lambda x: x[2])
    
    return closest_pair_rec(p_x, p_y, 'O')
    
def closest_pair_rec(p_x, p_y, m):
    
    if len(p_x) <= 3:
        
        
        return smallest_dist(p_x, len(p_x))
        
    # Else, divide and construct Qx, Qy, Rx, Ry (O(n) time)
    # Divide sorted x coordinates down the middle to find line L
    split = len(p_x) // 2
    # Left side of line L
    Q_x = p_x[:split]  
    Q_y = p_y[:split]
    # Right side of Line L
    R_x = p_x[split:]  
    R_y = p_y[split:] 
    
    q_min = closest_pair_rec(Q_x, Q_y, 'Q') # Return the two points in Q with smallest distance
   
    r_min = closest_pair_rec(R_x, R_y, 'R') # Return the two points in R with smallest distance
    
    
    delta = min(q_min, r_min) # smallest distance of the two halves Q & L
    
    x = p_x[split] # the point with the x-coordinate that is in the middle of the plane and defines L
    
    
    
    
    S_y = [point for point in p_y if (abs(point[1] - x[1]) < delta)] # set of all points in P, sorted by y coordinate, within delta distance of L
    s_min = smallest_dist_middle(S_y, len(S_y))
    
    
    
    if s_min < delta:   
        return s_min
    elif q_min < r_min: 
        return q_min
    else:
        return r_min
    
    
    

min_distance = closest_pair(matches)
print(len(matches), min_distance)


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
