import random
choose = input("choose a word: ")
choose = list(choose)
print(choose)
random.shuffle(choose)
l = len(choose)
for i in range(l):
    print(choose[i])