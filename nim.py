from random import randint

class Nim:
    def __init__(self, bags_number):

        #introduction
        print("Welcome to Nim game!")
        print("Here is a short introduction to this game:")
        print(f"\tWe have {bags_number} bags, each containing a number of stones.")
        print("\tAt each turn, you can extract any number of stones from a single bag.")
        print("\tYou win if you extract the last stone and lose otherwise.")
        print("\tThis game has mostly educational purposes.")
        print("\tPay attention! The computer is annoyingly good!")

        #random generation of values
        self.list = []
        last_element = 0
        for i in range(bags_number - 1):
            n = randint(1, 100)
            last_element ^= n
            self.list.append(n)
        
        #the last element shouldn't be the xor of the first (bags_number - 1) elements
        n = randint(1, 100)
        while n == last_element:
            n = randint(1, 100)
        self.list.append(n)
        
        #Intructions:
        print("Now, the game starts!")
        print("Note: If you want to take x stones from the bag y, you have to write: x y ")
        print("Example: 2 5 means that I want to take 5 stones from bag 2.\n")
        print("Here are the bags! We have printed our configuration.")
        self.print_list()
        self.start_game()

    def validate_input(self, player_input):

        count = 0

        #invalid characters
        for string in player_input:
            count += 1
            for character in string:
                if ord(character) < ord('0') or ord(character) > ord('9'):
                    print("Your input has been corrupted!\n")
                    return False 

        if count < 2 or count > 2:
            print("Try Again!")
            return False


        x = int(player_input[0])
        y = int(player_input[1])

        #invalid values
        if x < 1 or x > len(self.list):
            print("Wrong bag!")
            return False

        if self.list[x - 1] < y:
            print("Too many stones!")
            return False

        if y < 1:
            print("You should choose at least one stone!")
            return False

        return True

    def print_list(self):
        for i in range(len(self.list)):
            print(f"Bag{i + 1}: {self.list[i]}    ", end = '')
        print("\n")

    def start_game(self):
        Victory = 0
        print("Your turn:")
        player_input = input().split()

        if self.validate_input(player_input):
            x = int(player_input[0])
            y = int(player_input[1])
            self.list[x - 1] -= y
            print("\nAfter your move, the configuration will be:")
            self.print_list()
            Victory = self.calculate()
        else:
            print("Your input was not correct. You should:")
            print("\tEnter only 2 numbers (with space between).")
            print(f"\tThe first number should be between 1 and {len(self.list)}.")
            print("\tThe second number should be between 1 and the number of stones in the chosen bag.")
    
        if Victory == 1:
            print("You won!")
            return 0
        elif Victory == -1:
            print("The computer won!")
            return 0
        else:
            self.start_game()

    def calculate(self):
        xor_sum = 0
        sum = 0
        for elem in self.list:
            xor_sum ^= elem
            sum += elem

        #The computer cannot move anymore, the player won!
        if sum == 0:
            return 1
        
        #The computer is in a losing state, it does something random waiting for the opponent to make a mistake
        if xor_sum == 0:
            for i in range(len(self.list)):
                if self.list[i] > 0:
                    n = randint(1, self.list[i])
                    self.list[i] -= n
                    print(f"The computer chose to take {n} stones from the Bag{i + 1}.")
                    print("Consequently, the configuration will be:")
                    self.print_list()
                    return 0

        #The computer will win!
        aux = xor_sum
        msb = -1 #the most significant bit
        while aux != 0:
            aux >>= 1
            msb += 1
        for i in range(len(self.list)):
            if (self.list[i] & (1 << msb)) != 0:
                print(f"The computer chose to take {self.list[i] - (xor_sum ^self.list[i])} stones from the Bag{i + 1}.")
                print("Consequently, the configuration will be:")
                sum -= self.list[i] - (xor_sum ^self.list[i])
                self.list[i] -= self.list[i] - (xor_sum ^self.list[i])
                self.print_list()
                if sum == 0:
                    return -1
                else:
                    return 0


Nim(3)