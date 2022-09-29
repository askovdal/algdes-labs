from pprint import pprint
import sys

dna = {}

for inp in sys.stdin:
    if inp[0] == '>':
        species = inp[1:].strip().split()[0]
        dna[species] = ''
    else:
        dna[species] += inp.strip()


pprint(dna)
