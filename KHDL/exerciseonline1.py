
# Chương trình tính tuổi của một người ra đơn vị giây và tuần.

# Nhập số tuổi từ bàn phím
so_tuoi = int(input("Nhập số tuổi của bạn (theo năm): "))

# Các hằng số quy đổi
NGAY_TRONG_NAM = 365
TUAN_TRONG_NAM = 52
GIAY_TRONG_NGAY = 24 * 60 * 60  # 86400 giây

# Tính toán tuổi ra giây và tuần
# Lưu ý: Tính toán cơ bản, chưa tính đến năm nhuận
tuoi_tinh_theo_giay = so_tuoi * NGAY_TRONG_NAM * GIAY_TRONG_NGAY
tuoi_tinh_theo_tuan = so_tuoi * TUAN_TRONG_NAM

# In kết quả ra màn hình
print(f"Bạn đã sống được khoảng {tuoi_tinh_theo_giay} giây.")
print(f"Bạn đã sống được khoảng {tuoi_tinh_theo_tuan} tuần.")