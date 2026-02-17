n = int(input())
a = list(map(int, input().split()))
pos = 0
neg = 0
for i in a:
    if i > 0:
        pos += i
    else:
        if pos>0:
            pos-=1
        else:
            neg+=1
print(neg)

