# Khai báo chuỗi S (dùng 3 dấu nháy đơn ''' để chứa chuỗi có nhiều dòng)
S = '''Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm
Ai thương, ai cảm, ai nhớ, ai trông
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non '''

# Khai báo từ cần tìm
word = 'ai'

# Dùng hàm count() để đếm số lần xuất hiện của biến 'word' trong biến 'S'
so_lan_xuat_hien = S.count(word)

# In ra kết quả (Dùng f-string để chèn biến vào câu in cho đẹp)
print(f"số từ {word} là {so_lan_xuat_hien}")