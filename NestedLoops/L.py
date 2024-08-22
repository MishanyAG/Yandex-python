height = int(input())
number = 1
width = int(input())
spas = len(str(height * width))
for i in range(height):
    for j in range(width):
        print(f"{number:>{spas}}", end = " ")
        number += 1
    print()