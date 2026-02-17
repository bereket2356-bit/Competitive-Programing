n = int(input())
m = []
for _ in range(n):
    m.append(input())
count = 1 
for i in range(n-1):
    if m[i] != m[i + 1]:
        count += 1
print(count)
