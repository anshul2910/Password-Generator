from random import * 

alphaSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaCaps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special = "~!@#$%^&*()_-+=[]{}|\:;'<>?,./"

sequence1 = [str(randint(0, 9)), choice(alphaSmall), choice(alphaCaps), choice(special)]
sequence2 = [str(randint(0, 9)), choice(alphaSmall), choice(alphaCaps), choice(special)]

shuffle(sequence1)
shuffle(sequence2)

print(sequence1, sequence2)
final = sequence1 + sequence2
shuffle(final)
# print(final)

final1 =""

for i in final:
    final1 += str(i)
print(final1)    

