from string import ascii_lowercase

f = file('words.txt').read()
a = int(raw_input("Put a number"))
c = file('encrypted.txt', 'w')
d = file('decrypted.txt', 'w')
def encrypt():

    for word in f.split():

        for i in range(0,len(word)):

            b = ord(word[i])

            b += a
            if b > 127:
                x = b - 127
                b = 31 + x
            c.write(chr(b))
    return c
encrypt()

def decrypt(f):

    for i in str(f):
        b = ord(i)

        b -= a
        if b < 31:
            x = b + 127
            b = 31 - x
        print b
        d.write(chr(b))
    return d
decrypt(open("encrypted.txt", "r"))
