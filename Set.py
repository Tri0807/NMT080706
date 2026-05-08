S = input("Nhập số điện thoại S = ")
tap_hop_chuan = set("0123456789")
tap_hop_nhap = set(S)
cac_so_thieu = tap_hop_chuan - tap_hop_nhap
ket_qua = sorted([int(x) for x in cac_so_thieu])
print(f"=> Trong số điện thoại {S} không chứa các ký số: {ket_qua}")
