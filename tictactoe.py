#Copyright 2022 Armand Hangu <armandhangu2@gmail.com>
import turtle

class TicTacToe:
    def __init__(self):
        self.tictactoe_main()
        self.lines() #draws the lines
        self.screen.onscreenclick(self.click) #detecting clicks
        #close the window
        self.screen.mainloop() #keeps the window opened

    def tictactoe_main(self):
        #variabile
        self.tiles = ["", "", "", "", "", "", "", "", ""] #list with x or 0
        self.turn = 'x' #move variable
        self.tile = 0

        #initializing turtle
        self.t = turtle.Turtle() #drawing function
        self.t.speed(10) #speed setup
        self.t.color('white') #drqwing color - white
        self.t.width(4) #width setup - 4px

        #initializing screen
        self.screen = turtle.getscreen()
        self.screen.bgcolor('black') #background - black
        self.screen.setup(600, 600) #screen size 600px x 600px

    def goto(self, x, y): #function that draws without leaving traces
        #t variable used for drawing
        self.t.penup() #pick up the pencil
        self.t.goto(x, y) #set up the following coordinates
        self.t.pendown() #puts the pencil down

    def lines(self): #grid
        #horizontal lines
        self.goto(-300, 100)
        self.t.forward(600) #cross-line
        self.goto(-300, -100)
        self.t.forward(600)
        #vertical lines
        self.t.setheading(-90) #angle setup (down, from to left);
        self.goto(-100, 300)
        self.t.forward(600)
        self.goto(100, 300)
        self.t.forward(600)

    def addtile(self, tile): #the next move (x or 0)
        if self.tiles[tile] == "":
            self.tiles[tile] = self.turn #marks the move
            if self.turn == 'x':
                self.turn = '0'
            else:
                self.turn = 'x' #alternates moves

    def drawx(self, x, y): #draws the x
        if self.win() == True and self.turn == 'x':
            self.winner()
        else:
            self.goto(x + 20, y - 20) #top -eft
            self.t.setheading(-45) #45 degrees angle
            self.t.forward(226)
            self.goto(x + 180, y-20) #top-right
            self.t.setheading(-135) #45 degrees angle
            self.t.forward(226)

    def drawzero(self, x, y): #draws the 0
        if self.win() == True and self.turn == '0':
            self.winner()
        else:
            self.goto(x + 100, y - 180)
            self.t.setheading(0) #angle reset to 0
            self.t.circle(80) #circle with radius = 80px

    def draw(self): #draws x or 0 on each cell
        self.addtile(self.tile) #adds the move to the list and switch between players
        x, y = -300, 300 #left corner
        for i in range(len(self.tiles)): #compute the desired cell
            if i == self.tile: 
                if self.tiles[self.tile] == 'x':
                    self.drawx(x, y)
                else:
                    self.drawzero(x, y)
            else:
                #change the coordinates of the next cell
                if x >= 100:
                    x = -300 
                    y -= 200
                else:
                    x = x + 200

    def click(self, x, y): #get the corresponding cell
        column, row, self.tile = 0, 0, 0
        if self.win() == False: #win / lose check
            if self.alldrawn() == True:
                print("Remiza! Incercati din nou")
            else:
                column = (x + 300) // 200 #columns calculus
                row = (-y + 300) // 200 #line calculus
                self.tile = int(row * 3 + column) #cell formula
                self.tiles[self.tile] = self.turn #marks the move
                if self.turn == 'x':
                    self.turn = '0' #switch players
                else:
                    self.turn = 'x'
                self.draw()
        else:
            self.winner()

    def drawline(self, column, row, direction): #marks the victory-line
        x, y = -300, 300 #top left coordinates
        if direction == 'vertical': #vertical line winning
            x = x + 100 + column * 200 #calculate the middle of the wining-column
            self.goto(x, y) 
            self.t.setheading(270) #direction: up-down
            self.t.forward(600)
        if direction == 'horizontal': #horizontal line wining
            y = y - 100 - row * 200 #calculate the middle of the wining-line
            self.goto(x, y)
            self.t.setheading(0) #direction: left-right
            self.t.forward(600) 
        if direction == 'firstd': #the main diagonal
            self.goto(x, y + 10) #above the corner for a better visibility (when x)
            self.t.setheading(315) #direction: SE
            self.t.forward(1000)
        if direction == 'secondd': #the secondary diagonal
            self.goto(x + 600, y + 10) #above the corner for a better visibility (when x)
            self.t.setheading(225) #direction: SV
            self.t.forward(1000)

    #checks if the game has ended
    def win(self):
        if self.tiles[0] == self.tiles[1] == self.tiles[2] and self.tiles[0] != "": #first line
            return True #end
        if self.tiles[3] == self.tiles[4] == self.tiles[5] and self.tiles[3] != "": #second line
            return True 
        if self.tiles[6] == self.tiles[7] == self.tiles[8] and self.tiles[6] != "": #third line
            return True
        if self.tiles[0] == self.tiles[3] == self.tiles[6] and self.tiles[0] != "": #first column
            return True
        if self.tiles[1] == self.tiles[4] == self.tiles[7] and self.tiles[1] != "": #second column
            return True 
        if self.tiles[2] == self.tiles[5] == self.tiles[8] and self.tiles[2] != "": #third column
            return True 
        if(self.tiles[0] == self.tiles[4] == self.tiles[8]) and self.tiles[0] != "": #main diagonal
            return True 
        if(self.tiles[2] == self.tiles[4] == self.tiles[6]) and self.tiles[2] != "": #secondary diagonal
            return True 
        
        return False #nobody won, game continues

    def winner(self):
        if self.tiles[0] == self.tiles[1] == self.tiles[2] and self.tiles[0] != "": #first line
            print("a castigat ", self.tiles[0]) #winner
            self.drawline(0, 0, 'horizontal') #marks the 3 adjacent cells
        if self.tiles[3] == self.tiles[4] == self.tiles[5] and self.tiles[3] != "": #second line
            print("a castigat ", self.tiles[3]) 
            self.drawline(0, 1, 'horizontal') #marks the 3 adjacent cells
        if self.tiles[6] == self.tiles[7] == self.tiles[8] and self.tiles[6] != "": #third line
            print("a castigat ", self.tiles[6]) 
            self.drawline(0, 2, 'horizontal') #marks the 3 adjacent cells
        if self.tiles[0] == self.tiles[3] == self.tiles[6] and self.tiles[0] != "": #first column
            print("a castigat ", self.tiles[0]) 
            self.drawline(0, 0, 'vertical') #marks the 3 adjacent cells
        if self.tiles[1] == self.tiles[4] == self.tiles[7] and self.tiles[1] != "": #second column
            self.drawline(1, 0, 'vertical') #marks the 3 adjacent cells
        if self.tiles[2] == self.tiles[5] == self.tiles[8] and self.tiles[2] != "": #third column
            print("a castigat ", self.tiles[2]) 
            self.drawline(2, 0, 'vertical') #marks the 3 adjacent cells
        if(self.tiles[0] == self.tiles[4] == self.tiles[8]) and self.tiles[0] != "": #main diagonal
            print("a castigat ", self.tiles[0]) 
            self.drawline(0, 0, 'firstd') #marks the 3 adjacent cells
        if(self.tiles[2] == self.tiles[4] == self.tiles[6]) and self.tiles[2] != "": #secondary diagonal
            print("a castigat ", self.tiles[2]) 
            self.drawline(2, 0, 'secondd') #marks the 3 adjacent cells
        print("Final")

    #checks if all the squares are filled
    def alldrawn(self):
        for i in self.tiles:
            if i == "":
                return False #still playing
        return True #end
        
        