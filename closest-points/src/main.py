import math
import os
import re

expression = (
    "(\d+)\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)"
)


def euclidian_distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
    )


def smallest_dist(P, n):
    min_val = float("inf")  # base value
    # Nested loop to compare all points in the list (max 3 points = max )
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidian_distance(P[i], P[j])
            if dist < min_val:
                min_val = dist

    return min_val


def smallest_dist_middle(S_y, n):
    min_val = float("inf")
    count = 0
    # Nested loop that only compare with the next 15 points (see book p. 135 5.10)
    for i in range(n):
        for j in range(i + 1, n):
            if count == 15:
                count = 0
                break

            dist = euclidian_distance(S_y[i], S_y[j])
            if dist < min_val:
                min_val = dist

            count += 1

    return min_val


def closest_pair_rec(P_x, P_y):
    if len(P_x) <= 3:
        # return the smallest distance between the three points and continue the recursion
        return smallest_dist(list(P_x.values()), len(P_x))

    # Else, divide and construct Qx, Qy, Rx, Ry (O(n) time):

    # Divide sorted x coordinates down the middle to find line L
    split = len(P_x) // 2

    # Left side of line L
    Q = dict(list(P_x.items())[:split])

    # Right side of Line L
    R = dict(list(P_x.items())[split:])

    # Q_x is the same as Q, sorted by increasing x-coordinate
    # R_x is the same as R, sorted by increasing x-coordinate
    # Q and R are already sorted by increasing x-coordinate, so we don't need to
    # do anything to create Q_x and R_x
    Q_x = Q
    R_x = R

    # Q_y is the same as Q, sorted by increasing y-coordinate
    # R_y is the same as R, sorted by increasing y-coordinate
    # To create Q_y and R_y, we do a single pass through P_y, as those points
    # are already sorted by increasing y-coordinate
    Q_y = {}
    R_y = {}
    for point in P_y:
        try:
            # If the point is in Q (the left side of line L), we add it to Q_y
            Q_y[point] = Q[point]
        except KeyError:
            # If the point is not in Q, we know that it's in R (the right side
            # of line L), so we add it to R_y
            R_y[point] = R[point]

    q_min = closest_pair_rec(Q_x, Q_y)  # Return the min distance in Q
    r_min = closest_pair_rec(R_x, R_y)  # Return the min distance in R

    delta = min(q_min, r_min)  # smallest distance of the two halves Q & L

    # the point with the x-coordinate that is in the middle of the plane and defines L
    x = list(P_x.values())[split]

    # set of all points in P, sorted by y coordinate, within delta distance of L
    S_y = [point for point in list(P_y.values()) if (abs(point[0] - x[0]) < delta)]

    # Return the min distance in the middle section
    s_min = smallest_dist_middle(S_y, len(S_y))

    # return the min distance and continue the recursion
    if s_min < delta:
        return s_min
    elif q_min < r_min:
        return q_min
    else:
        return r_min


def closest_pair(P):
    # Sorted by x-coordinates (O(n log n) time)
    P_x = sorted(P, key=lambda x: x[1])

    # Sorted by y-coordinates  (O(n log n) time)
    P_y = sorted(P, key=lambda x: x[2])

    # Transform the lists into dicts so we can index the points in constant time
    P_x = {int(p[0]): p[1:] for p in P_x}
    P_y = {int(p[0]): p[1:] for p in P_y}

    return closest_pair_rec(P_x, P_y)


if __name__ == "__main__":
    data_files = os.listdir("../data")
    # Remove files that don't end in "-tsp.txt"
    tsp_files = list(filter(lambda x: x.endswith("-tsp.txt"), data_files))
    tsp_files.sort()

    for tsp_file in tsp_files:
        filename = f"../data/{tsp_file}"
        with open(filename, "r") as file:
            data = file.read()
            # Find points using the regex from the hint
            matches = re.findall(expression, data)
            matches = [list(map(float, match)) for match in matches]

            min_distance = closest_pair(matches)
            print(f"{filename}: {len(matches)} {min_distance}")


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
