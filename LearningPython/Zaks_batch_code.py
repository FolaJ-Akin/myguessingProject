from itertools import permutations



cleaning = 2



#Below are values for pre + post downtime values

DD=9

DE=9-cleaning

DF=11-cleaning

ED=10-cleaning

EE=11

EF=7-cleaning

FD=18-cleaning

FE=21-cleaning

FF=17



perm = permutations('DDEFFF')

permSet = set(perm)

permList = list(permSet)

permOverlap = []



for i in permSet:

    print (i)

    comboVal = [0,0,0,0,0,0]

    for y in range(0, 5):

        comboVal[y] = eval(i[y]+i[y+1])

    print(sum(comboVal))

    permOverlap.append((sum(comboVal)))



print((permOverlap))

best = (max(permOverlap))

print (best)

bestIndex = [i for i, j in enumerate(permOverlap) if j == best]

for i in bestIndex:

    print(permList[i])