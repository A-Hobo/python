
b = file("quiz2.txt", "w")
a = file("quiz.txt", "r").read()
def words_num():
    words = {
    "1": "one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7": "seven", "8":"eight", "9": "nine"
    }
    for word in a:
        for i in range(1, 1001):
            if word == i:
                b.write(words[i])

words_num()
