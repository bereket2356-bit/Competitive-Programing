s = input()
t = input()
pos = 0
for i in t:
    if s[pos] == i:
        pos += 1
print(pos + 1)
