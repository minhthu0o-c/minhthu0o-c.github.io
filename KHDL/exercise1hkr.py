n = int(input("Enter an integer number: "))
i = 1
t = 0
if 1 <= n <= 1000:
    while i < n+1:
        t = t + i
        i = i + 1
    print(f"Sum = {t}")
else:
    print("Your input is out of range!")    