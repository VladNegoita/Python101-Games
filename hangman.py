import random
import time
 
# Initial Steps to invite in the game:
print("\nWelcome to Hangman\n")
name = input("Enter your name: ")
print("Hello " + name + " ! " + "Good Luck!")
time.sleep(1)
print("The game is about to start!\n Let's play Hangman!\n")
time.sleep(1)

words = ["january", "auntie", "mother", "daughter", "dog", "cat", "apple", "pear", "ant", "august", "picture", "essay", "words", "above", "abandon", "absolute", "banana", "backhand", "backtracking", "bacterium", "bankrupt", "bed", "ball", "baggage", "camera", "camp", "callous", "calculate", "candid", "captain", "crimson", "dangerous", "date", "data", "dear", "declaration", "decorative", "deep", "earlobe", "ear", "early", "ecosystem", "edition", "affect", "effect", "embarrassment", "gain", "generate", "generation", "geography", "gentleman", "hair", "habitat", "hammer", "headache", "hesitate", "major", "machine", "mathematics", "measurement", "membership", "metaphor", "noise", "neutral", "notebook", "blackboard", "coursebook", "observation", "occasionally", "opportunity", "painting", "parallel", "physical", "suicide", "sacrifice", "salary", "schedule", "science", "seal", "sea", "second", "temperature", "tendency", "texture", "tennis", "territory", "terrible", "underground", "underneath", "undo", "reverse", "card", "uniform", "unique", "unicorn", "unlikely", "unusual", "valuable", "village", "video", "game", "vestige", "vessel", "violent"]

# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global play_game
    global length
    global word2
    word = random.choice(words)
    word2 = word
    length = len(word)
    display = '_' * length
    count = 0
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:
 
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y" or play_game =="Y":
        main()
        hangman()
    elif play_game == "n" or play_game == "N":
        exit()
 
# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    guess = guess.lower()
    if len(guess) == 0 or len(guess) >= 2 or guess.isalpha == False:
        print("Invalid Input, Try a letter\n")
        hangman()

    elif guess in word:
        while guess in word:
            already_guessed.append(guess)
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
 
    elif guess in already_guessed:
        print("Try another letter.\n")
 
    else:
        count += 1
 
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. You have " + str(limit - count) + " guesses remaining\n")
 
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. You have " + str(limit - count) + " guesses remaining\n")
 
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. You have " + str(limit - count) + " guesses remaining\n")
 
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("This is the last guess. Use it wisely!\n")
 
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess :( You are hanged!!!\n")
            print("The word was " + word2)
            play_loop()
 
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
 
    elif count != limit:
        hangman()


