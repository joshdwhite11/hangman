from random_word import RandomWords

#Fetches random word
r = RandomWords()
word =list(r.get_random_word(hasDictionaryDef = "true", minLength = 5, maxLength = 15).lower())

#Deletes any hyphens
for i in word:
    if i == "-":
        word.remove(i)
word = "".join(word)

#Creates guess string with length of the word
guess = list("_" * len(word))

#Try counter
tries = int(input("Welcome! How many tries do you want? "))
print("")

usedcorrect = ""
usedtotal = ""

print("Your word has", len(word), "letters.")
while tries >= 1 and word != "".join(guess):
    print("Your guess is: ", "".join(guess))
    letter = input("Guess a letter: ")
    print("")
    if letter in usedtotal:
        print("You have already used that letter.")
    else:
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
            print("***********************************************************")
            print("That is not a correct letter, sorry. You have", tries, "tries left")
            print("You have used the letters:", usedtotal)
        else:
            print("***********************************************************")
            print("Correct guess! Nice.")
            print("You have used the letters", usedtotal)

if tries == 0:
    print("")
    print("***********************************************************")
    print("***********************************************************")
    print("")
    print("You lose! The word is", word)
else:
    print("")
    print("***********************************************************")
    print("***********************************************************")
    print("")
    print("Congrats! You win! The word is", word)
    print("You had", tries, "tries left.")
