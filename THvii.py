
danh_sach = []
print("--- CHƯƠNG TRÌNH NHẬP VÀ XỬ LÝ SỐ NGUYÊN ---")
while True:
    try:
        so = int(input("Nhập một số nguyên: "))
        danh_sach.append(so)
    except ValueError:
        print("-> Lỗi rồi! Vui lòng chỉ nhập số nguyên.")
        continue 
    
    tiep_tuc = input("Bạn có muốn nhập nữa không (Y/N)? ").strip().upper()
    if tiep_tuc == 'N':
        break
if not danh_sach:
    print("\nDanh sách rỗng, không có gì để tính toán!")
else:
    print("\n" + "="*40)
    print(f"Danh sách bạn vừa nhập: {danh_sach}")
    print("="*40)
    is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    

    so_nguyen_to = list(filter(is_prime, danh_sach))
    print(f"a) Các số nguyên tố có trong list: {so_nguyen_to}")

    so_am = list(filter(lambda x: x < 0, danh_sach))
    so_duong = list(filter(lambda x: x > 0, danh_sach))
    tinh_tb = lambda lst: sum(lst) / len(lst)  
    try:
        tb_am = tinh_tb(so_am)
    except ZeroDivisionError:
        tb_am = 0       
    try:
        tb_duong = tinh_tb(so_duong)
    except ZeroDivisionError:
        tb_duong = 0
        
    print(f"b) Trung bình cộng các số âm   : {tb_am}")
    print(f"   Trung bình cộng các số dương: {tb_duong}")
    try:
        print(f"c) Số lớn nhất: {max(danh_sach)}")
        print(f"   Số nhỏ nhất: {min(danh_sach)}")
    except ValueError:
        print("c) Lỗi: Không thể tìm Max/Min của một danh sách rỗng.")
    is_sorted = lambda lst: lst == sorted(lst)   
    if is_sorted(danh_sach):
        print("d) Mảng ĐÃ ĐƯỢC sắp xếp tăng dần.")
    else:
        print("d) Mảng CHƯA ĐƯỢC sắp xếp tăng dần.")