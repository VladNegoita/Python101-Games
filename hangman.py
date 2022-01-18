import random
import time

words = ["january", "auntie", "mother", "daughter", "dog", "cat", "apple",
"pear", "ant", "august", "picture", "essay", "words", "above", "abandon",
"absolute", "banana", "backhand", "backtracking", "bacterium", "bankrupt",
"bed", "ball", "baggage", "camera", "camp", "callous", "calculate", "candid",
"captain", "crimson", "dangerous", "date", "data", "dear", "declaration",
"decorative", "deep", "earlobe", "ear", "early", "ecosystem", "edition", "affect",
"effect", "embarrassment", "gain", "generate", "generation", "geography", "gentleman",
"hair", "habitat", "hammer", "headache", "hesitate", "major", "machine", "mathematics",
"measurement", "membership", "metaphor", "noise", "neutral", "notebook", "blackboard",
"coursebook", "observation", "occasionally", "opportunity", "painting", "parallel",
"physical", "suicide", "sacrifice", "salary", "schedule", "science", "seal", "sea",
"second", "temperature", "tendency", "texture", "tennis", "territory", "terrible",
"underground", "underneath", "undo", "reverse", "card", "uniform", "unique", "unicorn",
"unlikely", "unusual", "valuable", "village", "video", "game", "vestige", "vessel",
"violent"]

class Hangman:
    def __init__(self):
        # Initial Steps to invite in the game:
        print("\nWelcome to Hangman\n")
        name = input("Enter your name: ")
        print("Hello " + name + " ! " + "Good Luck!")
        time.sleep(1)
        print("The game is about to start!\n Let's play Hangman!\n")
        time.sleep(1)
        self.hangman_main()
        self.hangman()

    # The parameters we require to execute the game:
    def hangman_main(self):
        self.word = random.choice(words)
        self.word2 = self.word
        self.length = len(self.word)
        self.display = '_' * self.length
        self.count = 0
        self.already_guessed = []
        self.play_game = ""

    # A loop to re-execute the game when the first round ends:
    def play_loop(self):
        global play_game
        play_game = input("Do You want to play again? y = yes, n = no \n")
        while play_game not in ["y", "n", "Y", "N"]:
            play_game = input("Do You want to play Hangman again? y = yes, n = no \n")
        if play_game == "y" or play_game =="Y":
            self.hangman_main()
            self.hangman()
        elif play_game == "n" or play_game == "N":
            exit()
    
    # Initializing all the conditions required for the game:
    def hangman(self):
        self.limit = 5
        guess = input("This is the Hangman Word: " + self.display + " Enter your guess: \n")
        guess = guess.strip()
        guess = guess.lower()
        if len(guess) == 0 or len(guess) >= 2 or guess.isalpha == False:
            print("Invalid Input, Try a letter\n")
            self.hangman()

        elif guess in self.word:
            while guess in self.word:
                self.already_guessed.append(guess)
                index = self.word.find(guess)
                self.word = self.word[:index] + "_" + self.word[index + 1:]
                self.display = self.display[:index] + guess + self.display[index + 1:]
            print(self.display + "\n")
    
        elif guess in self.already_guessed:
            print("Try another letter.\n")
    
        else:
            self.count += 1
    
            if self.count == 1:
                time.sleep(1)
                print("   _____ \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
                print("Wrong guess. You have " + str(self.limit - self.count) + " guesses remaining\n")
    
            elif self.count == 2:
                time.sleep(1)
                print("   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
                print("Wrong guess. You have " + str(self.limit - self.count) + " guesses remaining\n")
    
            elif self.count == 3:
                time.sleep(1)
                print("   _____ \n"
                        "  |     | \n"
                        "  |     |\n"
                        "  |     | \n"
                        "  |      \n"
                        "  |      \n"
                        "  |      \n"
                        "__|__\n")
                print("Wrong guess. You have " + str(self.limit - self.count) + " guesses remaining\n")
    
            elif self.count == 4:
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
    
            elif self.count == 5:
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
                print("The word was " + self.word2)
                self.play_loop()
    
        if self.word == '_' * self.length:
            print("Congrats! You have guessed the word correctly!")
            self.play_loop()
    
        elif self.count != self.limit:
            self.hangman()

