# def calculate_average(scores):
#     total = 0
#     for score in scores:
#         total += score
#     return total / len(scores)
# print(calculate_average([90, 80, 70, 0]))
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

# Test Case 1: Empty list 
try:
    result = calculate_average([])
    print(f"Empty list result: {result}")
except ZeroDivisionError:
    print("Test 1 FAILED: Division by zero error with empty list")

# Test Case 2: A list with one element
result = calculate_average([90])
print(f"Single element [90]: {result}")
assert result == 90.0, "Test 2 FAILED"

# Test Case 3: A list with multiple elements
result = calculate_average([90, 80, 70, 0])
print(f"Multiple elements [90, 80, 70, 0]: {result}")
assert result == 60.0, "Test 3 FAILED"

# Additional test cases for robustness:
# Test Case 4: All same values
result = calculate_average([100, 100, 100])
print(f"All same values [100, 100, 100]: {result}")
assert result == 100.0, "Test 4 FAILED"

# Test Case 5: Negative numbers
result = calculate_average([-10, 10, 0])
print(f"With negatives [-10, 10, 0]: {result}")
assert result == 0.0, "Test 5 FAILED"

# n = int(input("Nhập số lượng phần tử trong danh sách: "))
# li = list(input("Nhập các số, cách nhau bởi dấu phẩy: ").split(","))
# sum = 0
# if n == 0:
#     print("Danh sách rỗng, không thể tính trung bình cộng.")
#     exit()
# for i in li:
#     sum += float(i)
# print("Trung bình cộng là:", sum / n)


