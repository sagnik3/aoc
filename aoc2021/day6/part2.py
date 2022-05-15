"""
lanternfish live forever and have unlomited food and space.
256 days after ?

"""

from collections import Counter

with open("input.txt") as f:
    p = f.read().split(",")

p = [int(i) for i in p]

lifes = dict(Counter(p))

days = 256

for day in range(1, days + 1):
    lifes = {
        l: (0 if lifes.get(l + 1) is None else lifes.get(l + 1)) for l in range(-1, 8)
    }

    #make all 8s :- -1 as we create new fish with 8 after it reaches 0
    lifes[8] = lifes[-1]

    # add new lifes to that which are exhausted 
    lifes[6] += lifes[-1]

    #reset the exhausted ones 
    lifes[-1] = 0

print(sum(lifes.values()))
