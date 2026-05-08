#iii
S = input("Nhập số điện thoại S = ")
tap_hop_chuan = set("0123456789")
tap_hop_nhap = set(S)
cac_so_thieu = tap_hop_chuan - tap_hop_nhap
ket_qua = sorted([int(x) for x in cac_so_thieu])
print(f"=> Trong số điện thoại {S} không chứa các ký số: {ket_qua}")
#iv
S_chuoi = input("Nhập chuỗi S = ")
danh_sach_tu = S_chuoi.split()
da_thay = set()
tu_lap_lai = None
for tu in danh_sach_tu:
    if tu in da_thay:
        tu_lap_lai = tu
        break 
    else:
        da_thay.add(tu)

print(f"=> Sẽ in ra {tu_lap_lai}")
