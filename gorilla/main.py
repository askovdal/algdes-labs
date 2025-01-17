import numpy as np
import sys

T = [[]]  # matrix i,j size

# read substitution values
with open("data/BLOSUM62.txt", "r") as f:
    for line in f.readlines():
        if line[0] == "#":
            continue

        split_line = line.split()
        if line[0] == " ":
            blosum = {char: {} for char in split_line}
            idx = {i: char for i, char in enumerate(split_line)}
        else:
            for i, val in enumerate(split_line[1:]):
                blosum[idx[i]][split_line[0]] = int(val)

# dna strings for various species
dna = {}
for inp in sys.stdin:
    if inp[0] == ">":
        species = inp[1:].strip().split()[0]
        dna[species] = ""
    else:
        dna[species] += inp.strip()
# print(dna)


def alignment(x, y):
    x = list(x)  # x, m, i
    y = list(y)  # y, n, j
    m = len(x)
    n = len(y)

    xs = []
    ys = []

    # table for storing optimal substructure answers:
    dp = np.zeros([m + 1, n + 1], dtype=int)

    pgap = -4  # pgap er penalty for gap

    # make empty matric A with size (n+1 x m+1)
    # initialize A[i, 0]= iδ for each i and A[0, j]= jδ for each j
    for i in range(m + 1):
        dp[i, 0] = i * pgap

    for j in range(n + 1):
        dp[0, j] = j * pgap

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            a = blosum[x[i - 1]][y[j - 1]] + dp[i - 1, j - 1]
            b = pgap + dp[i - 1, j]
            c = pgap + dp[i, j - 1]

            max_val = max(a, b, c)

            dp[i, j] = max_val



    
    #print(dp)
    
    # print(dp[m, n])
    xs = []
    ys = []
    def findseq(i,j):

        a = blosum[x[i - 1]][y[j - 1]] + dp[i - 1, j - 1]
        b = pgap + dp[i - 1, j]
        c = pgap + dp[i, j - 1]
        
        if dp[i,j] == a:
            xs.insert(0,x[i - 1])
            ys.insert(0,y[j - 1])
            findseq(i-1,j-1)
        elif dp[i,j] == b:
            xs.insert(0,x[i - 1])
            ys.insert(0,'-')
            findseq(i-1,j)
        elif dp[i,j] == c:
            
            xs.insert(0,'-')
            ys.insert(0,y[j - 1])
            findseq(i,j-1)
    
    
    findseq(m,n)
    xs = ''.join(xs)
    ys = ''.join(ys)
    
    return dp[m, n], xs, ys


    

# print(alignment("KQRK", "KAK"))

keys = list(dna.keys())
for i, xasd in enumerate(keys):
    keys_left = keys[i+1:]
    for yasd in keys_left:
        x = dna[xasd]
        y = dna[yasd]
        val, xs, ys = alignment(x, y)
        print(xasd + '--' + yasd + ': ' + str(int(val)))
        print(xs)
        print(ys)

#OPT(i,j)=min[α_xi_yj + OPT(i−1,j−1), δ + OPT(i−1,j), δ + OPT(i,j−1)].

'''
# rat comparison
print('rat')
rat = 'MVHLTDAEKAAVNALWGKVNPDDVGGEALGRLLVVYPWTQRYFDSFGDLSSASAIMGNPKVKAHGKKVINAFNDGLKHLDNLKGTFAHLSELHCDKLHVDPENFRLLGNMIVIVLGHHLGKEFTPCAQAAFQKVVAGVASALAHKYH'
for xasd in dna.keys():
    x = dna[xasd]
    y = rat
    val, xs, ys = alignment(x, y)
    print(xasd + '--' + 'rat' + ': ' + str(int(val)))
    print(xs)
    print(ys)
'''

"""
>Sphinx 
KQRK
>Bandersnatch 
KAK
>Snark 
KQRIKAAKABK"""

"""pseudocode
Alignment(X,Y) //X and Y are sequences
    Array A[0 . . .m, 0 . . . n] ) // m and n are the last elements of sequnce X and Y
    Initialize A[i, 0]= iδ for each i // δ is the penalty for a gap (-4)
    Initialize A[0, j]= jδ for each j

    For j = 1, ... , n
        For i = 1, ... , m
        Use the recurrence (6.16) to compute A[i, j]
        Endfor
    Endfor
    Return A[m, n]


Space-Efficient-Alignment(X,Y)
    Array B[0 . . .m, 0 . . . 1]
    Initialize B[i, 0]= iδ for each i (just as in column 0 of A)
    For j = 1, . . . , n
        B[0, 1]= jδ (since this corresponds to entry A[0, j])
        For i = 1, . . . , m
            B[i, 1]= min(αxiyj + B[i − 1, 0], δ + B[i − 1, 1], δ + B[i, 0])

        Endfor

        Move column 1 of B to column 0 to make room for next iteration:
            Update B[i, 0]= B[i, 1] for each i
    Endfor
    
    
Divide-and-Conquer-Alignment(X,Y)
    Let m be the number of symbols in X
    Let n be the number of symbols in Y
    If m ≤ 2 or n ≤ 2 then
        Compute optimal alignment using Alignment(X,Y)
    Call Space-Efficient-Alignment(X,Y[1 : n/2])
    Call Backward-Space-Efficient-Alignment(X,Y[n/2+ 1 : n])
    Let q be the index minimizing f (q, n/2) + g(q, n/2)
    Add (q, n/2) to global list P
    Divide-and-Conquer-Alignment(X[1 : q],Y[1 : n/2])
    Divide-and-Conquer-Alignment(X[q + 1 : n],Y[n/2+ 1 : n])
    Return P"""
