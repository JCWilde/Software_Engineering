from random import randint, choice

alpha = "ABCDEFHGIJKLMNOPQRSTUVWXYZ"

res = ""
while True:
    if ''.join([choice(alpha) for i in range(randint(0, 12))]) == "HELLO WORLD":
        break
print(res)