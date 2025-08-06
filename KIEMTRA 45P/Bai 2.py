nhap_chuoi = input()

tach_pt = nhap_chuoi.split()

chuoi_moi = []

for item in tach_pt:
    for char in item:
        if char not in chuoi_moi: 
            chuoi_moi.append(char)

print(chuoi_moi)

