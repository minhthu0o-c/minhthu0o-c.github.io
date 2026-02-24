
# Nhập cho Vở (Notebooks)
sl_vo = int(input("Nhập số lượng vở: "))
gia_vo = float(input("Nhập giá mỗi quyển vở: "))

# Nhập cho Bút (Pens)
sl_but = int(input("Nhập số lượng bút: "))
gia_but = float(input("Nhập giá mỗi chiếc bút: "))

# Nhập cho Bìa hồ sơ (Folders)
sl_bia = int(input("Nhập số lượng bìa hồ sơ: "))
gia_bia = float(input("Nhập giá mỗi bìa hồ sơ: "))

# Tính tổng cộng
tong_tien = (sl_vo * gia_vo) + \
            (sl_but * gia_but) + \
            (sl_bia * gia_bia)

# In tổng tiền
print(f"Tổng chi phí cho tất cả dụng cụ là: ${tong_tien:.2f}")