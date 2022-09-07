import sys
from collections import deque

## INPUT

input = sys.stdin.read().split("\n")
input = [i for i in input if (i != '') and ('#' not in i)]

n = int(input[0][2:])
input.pop(0)

names = {}
proposers = {}
rejecters = {}
matchings = {}
free = set()

for i in range(n*2):
    person = [j for j in input[i].split()]
    names[int(person[0])] = person[1]
    
input = input[n*2:]

for i in range(n*2):
    if (int(input[i].split(':')[0])%2) == 0:
        woman = [j for j in input[i].split(':')]
        rejecters[int(woman[0])] = {int(man): rank for rank, man in enumerate(woman[1].split())}
        matchings[int(woman[0])] = None
    else:
        man = [j for j in input[i].split(':')]
        free.add(int(man[0]))
        proposers[int(man[0])] = deque([int(i) for i in man[1].split()])



### ALGORITHM

while len(free) != 0: #While there is a man m who is free and hasn't proposed to every woman
    man = free.pop() #Choose such a man m
    woman = proposers[man][0]#Let w be the highest-ranked woman in m's preference list
    if matchings[woman] == None: #If w is free then
        matchings[woman] = man #(m, w) become engaged
        proposers[man].popleft() #remove woman from list of women man has proposed to
    elif rejecters[woman][man] > rejecters[woman][matchings[woman]]: # Else w is currently engaged to m and If w prefers old m to new m then
        proposers[man].popleft() #m remains free and remove the woman that he has proposed to from rank list
        free.add(man)
    else: #w prefers new m to old m
        free.add(matchings[woman]) #add currently matched man to list of free men
        matchings[woman] = man #add new man to matching
     
        
for woman, man in matchings.items():
    print(names[man] + ' -- ' + names[woman])      


