n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    left = y - 1
    right = a[x-1] - y
    if x > 1:
        a[x-2] += left
    if x < n:
        a[x] += right
    a[x-1] = 0  
    
for b in a:
    print(b)
