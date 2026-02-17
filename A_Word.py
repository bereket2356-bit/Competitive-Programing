s=str(input())
count_upper=0
count_lower=0
for i in s:
    if i.isupper():
        count_upper+=1
    else:
        count_lower+=1
if count_lower>count_upper:
    s=s.lower()
    print(s)
elif count_lower==count_upper:
    s=s.lower()
    print(s)
else:
    s=s.upper()
    print(s)