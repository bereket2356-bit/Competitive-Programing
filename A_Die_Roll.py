Y, W = map(int, input().split())
max = max(Y, W)
fractions = ["1/1", "5/6", "2/3", "1/2", "1/3", "1/6"]
print(fractions[max- 1])
