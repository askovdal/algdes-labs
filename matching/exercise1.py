# -*- coding: utf-8 -*-

#from collections import deque  # https://realpython.com/linked-lists-python/

from operator import index
import sys



"""
n=3
1 Ross
2 Monica
3 Chandler
4 Phoebe
5 Joey
6 Rachel

1: 6 4 2
2: 3 5 1
3: 2 6 4
4: 5 1 3
5: 6 4 2
6: 1 5 3"""



input = sys.stdin.read().split("\n")

for line in input[0:8]:
    if line[0]== '#':
        input.remove(line)

n = int(input[0][2:])

m_names = {}
w_names = {}
for line in input[1:2*n+1]:
    num = int(line[0])
    print(num)
    if num%2 !=0: 
        m_names[num]=line[2:]
    if num%2 ==0:
        w_names[num]=line[2:]


proposers = {}
rejecters = {}
for line in input[2*n+2:4*n+2]:
    num = int(line[0])
    if num%2 !=0: 
        #x = [int(i) for i in x.split()]
        proposers[num]= [int(line) for line in line[3:].split(' ')]
    if num%2 ==0:
        rejecters[num]= [int(line) for line in line[3:].split(' ')]


#proposers = {1: [6, 4, 2], 3: [2, 6, 4], 5: [6, 4, 2]} #men
#rejecters = {2: [3, 5, 1], 4: [5, 1, 3], 6: [1, 5, 3]} #woman
matchings = {}
free = [1, 3, 5] #Initially all m ∈ M and w ∈W are free


while len(free) != 0: #While there is a man m who is free and hasn't proposed to every woman
    man = free[0] #Choose such a man m
    woman = proposers[man][0] #Let w be the highest-ranked woman in m's preference list

    if woman not in matchings: #If w is free then
        matchings[woman] = man #(m, w) become engaged
        del free[0] #remove man from list of free men
        proposers[man].remove(woman) #remove woman from list of women man has proposed to
    elif rejecters[woman].index(man) < rejecters[woman].index(matchings[woman]): # Else w is currently engaged to m and If w prefers old m to new m then
        proposers[man].remove(woman) #m remains free and remove the woman that he has proposed to from rank list
    else: #w prefers new m to old m
        free.append(matchings[woman]) #add currently matched man to list of free men
        matchings[woman] = man #add new man to matching
        del free[0] #remove new man from free men list
        
        
    
print(matchings)

"""
Initially all m ∈ M and w ∈W are free
While there is a man m who is free and hasn't proposed to every woman
    Choose such a man m
    Let w be the highest-ranked woman in m's preference list
        to whom m has not yet proposed
    If w is free then
        (m, w) become engaged
    Else w is currently engaged to m
        If w prefers m to m then
            m remains free
        Else w prefers m to m
            (m, w) become engaged
            m becomes free
        Endif
    Endif
Endwhile
Return the set S of engaged pairs
"""