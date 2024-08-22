size = int(input())
n = 0
for _ in range(size):
    a = int(input())
    tr = 1
    if a == 1:
        tr = 0
    else:
        a1 = int(a ** 0.5)
        while a1 > 1:
            if a % a1 == 0:
                tr = 0
                break
            a1 -= 1
    if tr == 1:
        n += 1
    tr = 1
print (n)