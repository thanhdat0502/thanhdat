n = int(input("Hang: "))
m = int(input("Cot: "))

matran = []

for i in range(n):
    hang = list(map(int, input().split()))
    matran.append(hang)

matran_new = []
print()

for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(matran[j][i])
    matran_new.append(tmp)
    
for i in range(m):
    for j in range(n):
        print(matran_new[i][j], end = " ")
    print()

print("va mang ban dau van la:")

for i in range(n):
    for j in range(m):
        print(matran[i][j], end = " ")
    print()