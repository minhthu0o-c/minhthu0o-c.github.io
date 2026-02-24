a = float(input("Nhập điểm mon 1: "))
b = float(input("Nhập điểm mon 2: "))
c = float(input("Nhập điểm mon 3: "))
def tinh_dtb(a, b, c):
    dtb = (a + b + c) / 3
    return dtb
print("Điểm trung bình là:", tinh_dtb(a, b, c))