tuple1 = tuple(map(int, input().split()))

set1 = set(tuple1)

for num in set1:
    count = tuple1.count(num)
    if count % 5 == 0 and count % 10 != 0:
        print(num, end=' ')