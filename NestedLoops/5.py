size = int(input())
lock = False
word = ""
count = 0
for _ in range(size):
    while(word != "ВСЁ"):
        word = str(input())
        if word == "зайка" and lock != True:
            count += 1
            lock = True
    word = ""
    lock = False