
# Định nghĩa giá trị PI theo đề bài
PI = 3.14159

# Nhập bán kính từ người dùng
# Chuyển sang kiểu float vì bán kính có thể là số thập phân
ban_kinh = float(input("Nhập bán kính hình tròn: "))

# Tính diện tích: S = pi * r^2
dien_tich = PI * (ban_kinh ** 2)

# Tính chu vi: C = 2 * pi * r
chu_vi = 2 * PI * ban_kinh

# In kết quả, làm tròn đến 2 chữ số thập phân cho đẹp
print(f"Diện tích: {dien_tich:.2f}")
print(f"Chu vi: {chu_vi:.2f}")