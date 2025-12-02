import math

f = open("input.txt", "r")
moves = f.readlines()
start = 50
counter = 0
for m in moves:
    if m[0] == "L":
        if start == 0:
            start = 100
        step = int(m[1:])  # 260
        if start - (step % 100) <= 0:
            counter += 1
        full_rotations = step // 100
        counter += full_rotations
        start = (start - step) % 100
    else:  # R
        step = int(m[1:])  # 260
        if start + (step % 100) >= 100:
            counter += 1
        full_rotations = step // 100
        counter += full_rotations
        start = (start + step) % 100
        pass


print(counter)
