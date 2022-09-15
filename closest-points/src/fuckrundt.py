import importlib

make = importlib.import_module("make-wc-instance")

points = make.distribute_points(1, 1, 1, 1)

print(points)

"""
Closest-Pair(P)
    Construct Px and Py (O(n log n) time)
    (p∗0, p∗1) = Closest-Pair-Rec(Px,Py)

Closest-Pair-Rec(Px, Py)
    If |P| ≤ 3 then 
        find closest pair by measuring all pairwise distances
    Endif

    Construct Qx, Qy, Rx, Ry (O(n) time)
    (q∗0,q∗1) = Closest-Pair-Rec(Qx, Qy)
    (r∗0,r∗1 ) = Closest-Pair-Rec(Rx, Ry)


    δ = min(d(q∗0,q∗1), d(r∗0,r∗1 ))
    x∗ = maximum x-coordinate of a point in set Q
    L = {(x,y) : x = x∗}
    S = points in P within distance δ of L.

    Construct Sy (O(n) time)
    For each point s ∈ Sy, compute distance from s
        to each of next 15 points in Sy
        Let s, s be pair achieving minimum of these distances
        (O(n) time)

    If d(s,s) < δ then
        Return (s,s)

    Else if d(q∗0,q∗1) < d(r∗0,r∗1 ) then
        Return (q∗0,q∗1)"""
