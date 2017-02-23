a = file("quiz.txt", "w")
for i in range (1,1001):
    if i % 3 == 0 and i % 2 == 0:
        a.write(str(i))
