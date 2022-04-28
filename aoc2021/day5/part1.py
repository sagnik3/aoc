import numpy as np

input = np.array(
    [
        [[int(z) for z in y.split(",")] for y in x.split(" -> ")]
        for x in open("input.txt", "r").readlines()
    ],
    dtype=int,
)
field = np.zeros([np.amax(input[:, :, 0]) + 1, np.amax(input[:, :, 1]) + 1], dtype=int)

for line in input:
    (x1, x2, y1, y2) = (line[0][0], line[1][0], line[0][1], line[1][1])
    if x1 == x2 or y1 == y2:
        if x1 > x2:
            (x1, x2) = (x2, x1)
        if y1 > y2:
            (y1, y2) = (y2, y1)
        field[x1 : x2 + 1, y1 : y2 + 1] += 1

print(np.count_nonzero(field >= 2))
