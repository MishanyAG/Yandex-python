size = int(input())
for i in range(size):
    for j in range(size):
        print(f"{(i + 1) * (j + 1)} ", end="")
    print("")