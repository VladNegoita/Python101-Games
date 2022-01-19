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
        self.tiles = ["", "", "", "", "", "", "", "", ""] #lista care memoreaza unde a fost pus x sau 0
        self.turn = 'x' # variabila care memoreaza al cui e randul (x sau 0)
        self.tile = 0

        #initializare turtle
        self.t = turtle.Turtle() #initializeaza functie pt desenare
        self.t.speed(10) #seteaza viteza de desenare la 10 (valoarea maxima)
        self.t.color('white') #seteaza albul drept culoare cu care se deseneaza 
        self.t.width(4) #seteaza grosimea desenului la 4px

        #initializare ecran
        self.screen = turtle.getscreen() #initializeaza ecranul
        self.screen.bgcolor('black') #seteaza negru drept culoare de fundal
        self.screen.setup(600, 600) #seteaza dimensiunea ecranului 600px pe 600px

    def goto(self, x, y): #functie pentru a desena fara a lasa urme
        #se foloseste variabila t pt desenare
        self.t.penup() #ridica creionul pentru a nu mai desena
        self.t.goto(x, y) #seteaza urmatoarele coordonate unde se va desena
        self.t.pendown() #coboara creionul pentru a desena din nou

    def lines(self): #deseneaza liniile pentru formarea matricei de 3x3
        #liniile orizontale
        self.goto(-300, 100)
        self.t.forward(600) #deseneaza o linie dintr-un capat in altul al tablei
        self.goto(-300, -100)
        self.t.forward(600)
        #liniile verticale
        self.t.setheading(-90) #seteaza unghiul de desenare in jos (el e by default de la stanga)
        self.goto(-100, 300)
        self.t.forward(600)
        self.goto(100, 300)
        self.t.forward(600)

    def addtile(self, tile): #adauga cine e la mutare (x sau 0) in lista
        if self.tiles[tile] == "":
            self.tiles[tile] = self.turn #adauga in lista cine a mutat
            if self.turn == 'x':
                self.turn = '0'
            else:
                self.turn = 'x' #schimba alternativ randul la mutare (daca s-a adaugat in lista x, acum va fi randul lui 0)

    def drawx(self, x, y): #deseneaza x-ul
        if self.win() == True and self.turn == 'x':
            self.winner()
        else:
            self.goto(x + 20, y - 20) #se duce in stanga sus in patrat
            self.t.setheading(-45) #inclinatie de 45 de grade pt a ajunge in dreapta jos
            self.t.forward(226)
            self.goto(x + 180, y-20) #se duce in dreapta sus in patrat
            self.t.setheading(-135) #inclinatie de 45 de grade pt a ajunge in stanga jos
            self.t.forward(226)

    def drawzero(self, x, y): #deseneaza 0-ul
        if self.win() == True and self.turn == '0':
            self.winner()
        else:
            self.goto(x + 100, y - 180)
            self.t.setheading(0) #se reseteaza unghiul de desenare la 0 grade (anterior la desenarea x-ului era 45)
            self.t.circle(80) #metoda in turtle pt a desena un cerc cu raza de 80px

    def draw(self): #deseneaza x sau 0 pe fiecare patrat
        self.addtile(self.tile) #se adauga mutarea in lista si se schimba randul
        x, y = -300, 300 #coltul din stanga al ecranului
        for i in range(len(self.tiles)): #determina unde a fost adaugat elementul in lista si il deseneaza in patratul corespunzator 
            if i == self.tile: 
                if self.tiles[self.tile] == 'x':
                    self.drawx(x, y)
                else:
                    self.drawzero(x, y)
            else:
                #schimba coordonatele patratului unde ar urma sa se deseneze
                if x >= 100:
                    x = -300 
                    y -= 200
                else:
                    x = x + 200

    def click(self, x, y): #de fiecare data cand e apasat un patrat, in acesta se va desena
        column, row, self.tile = 0, 0, 0
        if self.win() == False: #se verifica la fiecare click daca a castigat x sau 0
            if self.alldrawn() == True:
                print("Remiza! Incercati din nou")
            else:
                column = (x + 300) // 200 #calculeaza coloana unde  s-a apasat cu mouse-ul 
                row = (-y + 300) // 200 #calculeaza linia unde s-a apasat cu mouse-ul
                self.tile = int(row * 3 + column) #determina numarul patratului in matrice
                self.tiles[self.tile] = self.turn #se adauga mutarea in lista
                if self.turn == 'x':
                    self.turn = '0' #randul ii revine urmatorului jucator
                else:
                    self.turn = 'x'
                self.draw()
        else:
            self.winner()

    def drawline(self, column, row, direction): #deseneaza o linie deasupra pieselor castigatoare
        x, y = -300, 300 #coordonate stanga sus
        if direction == 'vertical': #o linie verticala a castigat
            x = x + 100 + column * 200 #calculeaza mijlocul coloanei castigatoare, bazat pe win()
            self.goto(x, y) 
            self.t.setheading(270) #seteaza directia in jos
            self.t.forward(600)
        if direction == 'horizontal': #o linie orizontala a castigat
            y = y - 100 - row * 200 ##calculeaza mijlocul liniei castigatoare
            self.goto(x, y)
            self.t.setheading(0) #seteaza directia stanga - dreapta
            self.t.forward(600) 
        if direction == 'firstd': #diagonala principala a castigat
            self.goto(x, y + 10) #putin deasupra coltului stanga sus pentru a nu se confunda linia desenata cu x-urile
            self.t.setheading(315) #directia SE
            self.t.forward(1000)
        if direction == 'secondd': #diagonala secundara a castigat
            self.goto(x + 600, y + 10) #putin deasupra coltului dreapta sus pentru a nu se confunda linia desenata cu x-urile
            self.t.setheading(225) #directia SV
            self.t.forward(1000)

    #verifica la fiecare click daca x sau 0 a castigat
    def win(self):
        if self.tiles[0] == self.tiles[1] == self.tiles[2] and self.tiles[0] != "": #daca s-a castigat pe prima linie
            return True #finalul jocului
        if self.tiles[3] == self.tiles[4] == self.tiles[5] and self.tiles[3] != "": #daca s-a castigat pe a doua linie
            return True 
        if self.tiles[6] == self.tiles[7] == self.tiles[8] and self.tiles[6] != "": #daca s-a castigat pe a treia linie
            return True
        if self.tiles[0] == self.tiles[3] == self.tiles[6] and self.tiles[0] != "": #daca s-a castigat pe prima coloana
            return True
        if self.tiles[1] == self.tiles[4] == self.tiles[7] and self.tiles[1] != "": #daca s-a castigat pe a doua coloana
            return True 
        if self.tiles[2] == self.tiles[5] == self.tiles[8] and self.tiles[2] != "": #daca s-a castigat pe a treia coloana
            return True 
        if(self.tiles[0] == self.tiles[4] == self.tiles[8]) and self.tiles[0] != "": #daca s-a castigat pe diagonala principala
            return True 
        if(self.tiles[2] == self.tiles[4] == self.tiles[6]) and self.tiles[2] != "": #daca s-a castigat pe diagonala secundara
            return True 
        
        return False #daca nimeni nu a castigat, jocul continua

    def winner(self):
        if self.tiles[0] == self.tiles[1] == self.tiles[2] and self.tiles[0] != "": #daca s-a castigat pe prima linie
            print("a castigat ", self.tiles[0]) #afiseaza cine a castigat
            self.drawline(0, 0, 'horizontal') #se deseneaza linia pe linia castigatoare
        if self.tiles[3] == self.tiles[4] == self.tiles[5] and self.tiles[3] != "": #daca s-a castigat pe a doua linie
            print("a castigat ", self.tiles[3]) 
            self.drawline(0, 1, 'horizontal') #se deseneaza linia pe linia castigatoare
        if self.tiles[6] == self.tiles[7] == self.tiles[8] and self.tiles[6] != "": #daca s-a castigat pe a treia linie
            print("a castigat ", self.tiles[6]) 
            self.drawline(0, 2, 'horizontal') #se deseneaza linia pe linia castigatoare
        if self.tiles[0] == self.tiles[3] == self.tiles[6] and self.tiles[0] != "": #daca s-a castigat pe prima coloana
            print("a castigat ", self.tiles[0]) 
            self.drawline(0, 0, 'vertical') #se deseneaza linia pe coloana castigatoare
        if self.tiles[1] == self.tiles[4] == self.tiles[7] and self.tiles[1] != "": #daca s-a castigat pe a doua coloana
            print("a castigat ", self.tiles[1]) 
            self.drawline(1, 0, 'vertical') #se deseneaza linia pe coloana castigatoare
        if self.tiles[2] == self.tiles[5] == self.tiles[8] and self.tiles[2] != "": #daca s-a castigat pe a treia coloana
            print("a castigat ", self.tiles[2]) 
            self.drawline(2, 0, 'vertical') #se deseneaza linia pe coloana castigatoare
        if(self.tiles[0] == self.tiles[4] == self.tiles[8]) and self.tiles[0] != "": #daca s-a castigat pe diagonala principala
            print("a castigat ", self.tiles[0]) 
            self.drawline(0, 0, 'firstd') #se deseneaza linia pe diagonala principala
        if(self.tiles[2] == self.tiles[4] == self.tiles[6]) and self.tiles[2] != "": #daca s-a castigat pe diagonala secundara
            print("a castigat ", self.tiles[2]) 
            self.drawline(2, 0, 'secondd') #se deseneaza linia pe diagonala secundara
        print("Final") #nu se printeaza mesajul, dar conditia face programul sa deseneze corect    

    #verifica daca toate patratele au fost desenate
    def alldrawn(self):
        for i in self.tiles:
            if i == "":
                return False #nu toate patratele au fost desenate
        return True #se incheie jocul
        