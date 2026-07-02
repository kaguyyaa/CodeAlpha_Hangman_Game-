import random

words = ["apple", "tiger", "chair", "planet", "python"]
word = random.choice(words)

guessed = []
wrong = 0
limit = 6

while wrong < limit:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display.strip())
    print("Wrong guesses left:", limit - wrong)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single alphabet.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess not in word:
        wrong += 1
        print("Wrong guess!")

if wrong == limit:
    print("\nGame Over!")
    print("The word was:", word)