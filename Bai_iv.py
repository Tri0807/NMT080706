import datetime
hien_tai = datetime.datetime.now()
print("Thời gian hiện tại \t\t:", hien_tai.strftime("%H:%M:%S"))
goi_5_giay = datetime.timedelta(seconds=5)
thoi_gian_moi = hien_tai + goi_5_giay
print("Thời gian sau khi thêm 5 giây\t:", thoi_gian_moi.strftime("%H:%M:%S"))