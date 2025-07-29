s1 = input("nhap chuoi s1: ")
s2 = input("nhap chuoi s2: ")

print("dao nguoc s1:", s1[::-1])

a = int(input("nhap a (1 <= a < b): "))
b = int(input("nhap b (a < b <= len(s2)): "))

if 1 <= a < b <= len(s2):
    s2_new = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
    print("chuoi s2 sau khi dao nguoc doan [a, b] la: ", s2_new)
else:
    print("gia tri a, b khong hop le.")

s3 = ''.join(s1[i] for i in range(len(s1)) if i % 2 != 0)
print("s3: ", s3)

length = max(len(s1), len(s2))
s4 = ''
for i in range(length):
    if i < len(s1):
        s4 += s1[i]
    if i < len(s2):
        s4 += s2[i]
print("s4: " ,s4)