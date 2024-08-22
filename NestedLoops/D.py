count = int(input())
sum = 0
for _ in range(count):
    n = int(input())
    while n != 0:
        sum += n % 10
        n = n // 10
print(sum)
        