n = int(input())
a = list(map(int, input().split()))
left = 0
right = n - 1
b, c = 0, 0
turn = 0 
while left <= right:
    if a[left] > a[right]:
        pick = a[left]
        left += 1
    else:
        pick = a[right]
        right -= 1
    
    if turn == 0:
        b += pick
    else:
        c += pick  
    turn ^= 1 
print(b, c)
