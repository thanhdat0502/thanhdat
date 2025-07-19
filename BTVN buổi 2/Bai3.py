n = int(input("Nhập số nguyên n: "))

# Biến để đếm số chữ số
dem = 0
tong = 0
bien = n

# Duyệt từng chữ số
while bien > 0:
    chu_so = bien % 10       
    tong += chu_so         
    dem += 1                
    bien //= 10              
print("Số chữ số:", dem, "Tổng chữ số:", tong)