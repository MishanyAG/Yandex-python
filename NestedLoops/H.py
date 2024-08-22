count = int(input())
maxSum = 0
sum = 0
winnerName = ""
for i in range(count):
    name = str(input())
    number = int(input())
    while number != 0:
        sum += number % 10
        number = number // 10
    if sum >= maxSum:
        maxSum = sum
        winnerName = name
    sum = 0
print(winnerName)