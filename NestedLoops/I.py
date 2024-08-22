count = int(input())
figure = 0
answer = ""
for _ in range(count):
    number = int(input())
    while number != 0:
        if number % 10 > figure:
            figure = number % 10
        number //= 10
    answer += f"{figure}"
    figure = 0
print(answer)