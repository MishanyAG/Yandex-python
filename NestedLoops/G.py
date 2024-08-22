count = int(input())
default = 3
for i in range(count):
    while default != 0:
        print(f"До старта {default} секунд(ы)")
        default -= 1
    default += 3 + i + 1
    print(f"Старт {i + 1}!!!")