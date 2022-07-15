import random
wordList=['HOUSE','APPLE','PIZZA','ROUND','GREEN']
word=random.choice(wordList)
guess='*****'
while (guess!=word):
    print("Here is the word",guess)
    letter=input("Guess a letter")
    hasLetter=False
    newguess=[]
    for n in range(5):
        if(letter==word[n]):
            newguess.append(letter)
            hasLetter=True
        else:
            newguess.append(guess[n])
    guess.join(newguess)
    if (hasLetter==True):
        print("Good Guess")
    else:
        print("Not in the word")
print("The word was",word)