import sys

## INPUT

input = sys.stdin.read().split("\n")
input = [i for i in input if (i != '') and ('#' not in i)]

n = int(input[0][2:])
input.pop(0)

names = {}
proposers = {}
rejecters = {}
matchings = {}
free = []

for i in range(n*2):
    person = [j for j in input[i].split()]
    names[int(person[0])] = person[1]
    
input = input[n*2:]

for i in range(n*2):
    if (int(input[i].split(':')[0])%2) == 0:
        woman = [j for j in input[i].split(':')]
        rejecters[int(woman[0])] = [int(i) for i in woman[1].split()]
    else:
        man = [j for j in input[i].split(':')]
        free.append(int(man[0]))
        proposers[int(man[0])] = [int(i) for i in man[1].split()]
    


### ALGORITHM

while len(free) != 0: #While there is a man m who is free and hasn't proposed to every woman
    man = free[0] #Choose such a man m
    woman = proposers[man][0] #Let w be the highest-ranked woman in m's preference list

    if woman not in matchings: #If w is free then
        matchings[woman] = man #(m, w) become engaged
        del free[0] #remove man from list of free men
        proposers[man].remove(woman) #remove woman from list of women man has proposed to
    elif rejecters[woman].index(man) > rejecters[woman].index(matchings[woman]): # Else w is currently engaged to m and If w prefers old m to new m then
        proposers[man].remove(woman) #m remains free and remove the woman that he has proposed to from rank list
    else: #w prefers new m to old m
        free.append(matchings[woman]) #add currently matched man to list of free men
        matchings[woman] = man #add new man to matching
        del free[0] #remove new man from free men list
        
for woman, man in matchings.items():
    print(names[man] + ' -- ' + names[woman])      


