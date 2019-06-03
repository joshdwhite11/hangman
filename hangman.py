from random_word import RandomWords

r = RandomWords()
word = r.get_random_word(hasDictionaryDef = "true", minLength=5, maxLength=15)
guess = list("_" * len(word))

tries = int(input('Welcome! How many tries do you want? ')) #Try counter

usedcorrect = ''
usedtotal = ''

print("Your word has", len(word), "letters.")
while tries >= 0 and word != "".join(guess):
    print("Your guess is: ", "".join(guess))
    letter = input('Guess a letter: ')
    print("")
    if letter in usedcorrect:
        print("You have already used that letter.")
    usedtotal = usedtotal + letter
    rightcounter = 0
    lencounter = 0 #Counter to parse word
    while len(word) > lencounter:
        if word[lencounter] == letter:
            guess[lencounter] = letter
            rightcounter += 1
            lencounter += 1
            usedcorrect = usedcorrect + letter
        else:
            lencounter += 1
    if rightcounter == 0:
        tries = tries - 1
        print("That is not a correct letter, sorry. You have", tries + 1, "tries left")
        print("")
        print("You have used the letters", usedtotal)
    else:
        print("Correct guess! Nice.")
        print("")
        print("You have used the letters", usedtotal)

if tries == -1:
    print("You lose! The word is", word)
else:
    print("Congrats! You win! The word is", word)
