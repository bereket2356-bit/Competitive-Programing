s = input()
current = 'a'
rotations = 0
for i in s:
    diff = abs(ord(i) - ord(current))
    rotations += min(diff, 26 - diff)
    current = i
print(rotations)
