n = int(input())
i = 1
t = 0
if 1 <= n <= 1000:
    while i < n+1:
        t = t + i
        i = i + 1
    print(t)
else:
    print("n is out of range")    