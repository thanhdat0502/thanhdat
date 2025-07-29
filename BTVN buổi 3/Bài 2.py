k = int(input("nhap k: "))
a = [int(input(f"a[{i}] = ")) for i in range(k)]

n = int(input("nhap so dong cua ma tran: : "))
m = int(input("nhap so cot cua ma tran: "))

if n * m > k:
    print("no")
else:
    matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        matrix.append(row)

    print("ma tran: ")
    for row in matrix:
        print(row)