# Nhập số phần tử N
N = int(input("Nhập số phần tử N: "))

# Nhập list số nguyên
list1 = []
for i in range(N):
    list1.append(int(input(f"Nhập phần tử thứ {i}: ")))

# Nhập X và đếm số lần xuất hiện
X = int(input("Nhập số X: "))
print("Số lần X xuất hiện:", list1.count(X))

# Thay thế phần tử từ vị trí 2 -> 7 
list1[2:8] = [8, 5, 4, 0, 1, 3]
print("List sau khi thay thế:", list1)

# Tìm số lớn nhất và nhỏ nhất 
print("Số lớn nhất:", max(list1))
print("Số nhỏ nhất:", min(list1))

# Nhập Y và chèn vào đầu list
Y = int(input("Nhập số Y: "))
list1.insert(0, Y)
print("List sau khi chèn:", list1)

# Kiểm tra tăng dần, giảm dần
if list1 == sorted(list1):
    print("TĂNG")
elif list1 == sorted(list1, reverse=True):
    print("GIẢM")
else:
    print("NO")






