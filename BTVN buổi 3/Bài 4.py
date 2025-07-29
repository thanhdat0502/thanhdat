chuoi = input("nhap ho ten: ")
tu_list = chuoi.strip().split()
tu_list_chuan = [tu.capitalize() for tu in tu_list]
kq = ' '.join(tu_list_chuan)
print (kq)