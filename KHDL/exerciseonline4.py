# Chuyển đổi từ Celsius sang Fahrenheit và Kelvin theo công thức.

# Nhập nhiệt độ C từ người dùng
do_c = float(input("Nhập nhiệt độ (độ C): "))

# Tính độ F
# Công thức: (Celsius * 9/5) + 32
do_f = (do_c * 9/5) + 32

# Tính độ K
# Công thức: Celsius + 273.15
do_k = do_c + 273.15

# In kết quả chuyển đổi
print(f"{do_c}°C bằng {do_f}°F")
print(f"{do_c}°C bằng {do_k}K")