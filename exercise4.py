# import random

secret = input("Enter the secret: ")
words = secret.split(" ")
r1 = "brh"
r2 = "jhg"
val = int(input("Enter 0 for encoding and 1 for decoding: "))

if(val == 0):
    coding = True
else:
    coding = False

if(coding):
    nword = []
    for word in words: 
        if(len(word) >= 3):
            coded = r1 + word[1:] + word[0] + r2
            nword.append(coded)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))
else:
    nword = []
    for word in words: 
        if(len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nword.append(stnew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))