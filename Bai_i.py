import datetime
now = datetime.datetime.now()

print(f"{'Năm hiện tại':<45} | {now.strftime('%Y')}")
print(f"{'Tháng hiện tại bằng chữ':<45} | {now.strftime('%B')}")
print(f"{'Tuần hiện tại là tuần thứ mấy trong năm':<45} | {now.strftime('%W')}")
tuan_trong_thang = (now.day - 1) // 7 + 1
print(f"{'Tuần hiện tại là tuần thứ mấy trong tháng':<45} | {tuan_trong_thang}")

print(f"{'Ngày hiện tại là ngày thứ mấy trong năm':<45} | {now.strftime('%j')}")
print(f"{'Ngày dương lịch hiện tại là ngày':<45} | {now.strftime('%d')}")
print(f"{'Thứ của ngày hiện tại':<45} | {now.strftime('%A')}")
print(f"{'Giờ phút giây hiện tại':<45} | {now.strftime('%H:%M:%S')}")