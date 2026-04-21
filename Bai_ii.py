import datetime
ngay1_str = input("Nhập ngày thứ nhất (ví dụ 15/09/2023): ")
ngay2_str = input("Nhập ngày thứ hai (ví dụ 20/09/2023): ")
quy_tac = "%d/%m/%Y"
ngay1 = datetime.datetime.strptime(ngay1_str, quy_tac)
ngay2 = datetime.datetime.strptime(ngay2_str, quy_tac)
so_ngay = abs((ngay2 - ngay1).days)
print(f"Số ngày cách nhau là: {so_ngay} ngày")