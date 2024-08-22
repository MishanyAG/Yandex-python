size = int(input())
jump = 1
current_line = 0
for i in range(size):
    print(f"{i + 1} ", end="")
    current_line += 1
    if current_line == jump:
        print("")
        current_line = 0
        jump += 1