size = int(input())
print('А Б В')
for a in range(1, size - 1):
    for b in range(1, size - a):
        c = size - a - b
        print(a, b, c)