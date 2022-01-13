import turtle
import random

#variabile globale
tiles = ["", "", "", "", "", "", "", "", ""] #lista care memoreaza unde a fost pus x sau 0
turn = 'x' # variabila care memoreaza al cui e randul (x sau 0)
poz0, column0, row0 = -1, -1, -1
tile = 0

#initializare turtle
t = turtle.Turtle() #initializeaza functie pt desenare
t.speed(10) #seteaza viteza de desenare la 10 (valoarea maxima)
t.color('white') #seteaza albul drept culoare cu care se deseneaza 
t.width(4) #seteaza grosimea desenului la 4px

#initializare ecran
screen = turtle.getscreen() #initializeaza ecranul
screen.bgcolor('black') #seteaza negru drept culoare de fundal
screen.setup(600, 600) #seteaza dimensiunea ecranului 600px pe 600px

def goto(x, y): #functie pentru a desena fara a lasa urme
    global t #se foloseste variabila setata global pt desenare
    t.penup() #ridica creionul pentru a nu mai desena
    t.goto(x, y) #seteaza urmatoarele coordonate unde se va desena
    t.pendown() #coboara creionul pentru a desena din nou

def lines(): #deseneaza liniile pentru formarea matricei de 3x3
    #liniile orizontale
    goto(-300, 100)
    t.forward(600) #deseneaza o linie dintr-un capat in altul al tablei
    goto(-300, -100)
    t.forward(600)
    #liniile verticale
    t.setheading(-90) #seteaza unghiul de desenare in jos (el e by default de la stanga)
    goto(-100, 300)
    t.forward(600)
    goto(100, 300)
    t.forward(600)

def addtile(tile): #adauga cine e la mutare (x sau 0) in lista
    global tiles, turn
    if tiles[tile] == "":
        tiles[tile] = turn #adauga in lista cine a mutat
        if turn == 'x':
            turn = '0'
        else:
            turn = 'x' #schimba alternativ randul la mutare (daca s-a adaugat in lista x, acum va fi randul lui 0)

def drawx(x, y): #deseneaza x-ul
    global t
    if win() == True and turn == 'x':
        print("Final")
    else:
        goto(x + 20, y - 20) #se duce in stanga sus in patrat
        t.setheading(-45) #inclinatie de 45 de grade pt a ajunge in dreapta jos
        t.forward(226)
        goto(x + 180, y-20) #se duce in dreapta sus in patrat
        t.setheading(-135) #inclinatie de 45 de grade pt a ajunge in stanga jos
        t.forward(226)

def drawzero(x, y): #deseneaza 0-ul
    global t
    if win() == True and turn == '0':
        print("Final") #nu se printeaza mesajul, dar conditia face programul sa deseneze corect
    else:
        goto(x + 100, y - 180)
        t.setheading(0) #se reseteaza unghiul de desenare la 0 grade (anterior la desenarea x-ului era 45)
        t.circle(80) #metoda in turtle pt a desena un cerc cu raza de 80px

def draw(tile): #deseneaza x sau 0 pe fiecare patrat
    global tiles
    addtile(tile) #se adauga mutarea in lista si se schimba randul
    x, y = -300, 300 #coltul din stanga al ecranului
    for i in range(len(tiles)): #determina unde a fost adaugat elementul in lista si il deseneaza in patratul corespunzator 
        if i == tile: 
            if tiles[tile] == 'x':
                drawx(x, y)
            else:
                drawzero(x, y)
        else:
            #schimba coordonatele patratului unde ar urma sa se deseneze
            if x >= 100:
                x = -300 
                y -= 200
            else:
                x = x + 200

def click(x, y): #de fiecare data cand e apasat un patrat, in acesta se va desena
    global t, turn
    column, row, tile = 0, 0, 0
    if win() == False: #se verifica la fiecare click daca a castigat x sau 0
        if alldrawn() == True:
            print("remiza")
        else:
            column = (x + 300) // 200 #calculeaza coloana unde  s-a apasat cu mouse-ul 
            row = (-y + 300) // 200 #calculeaza linia unde s-a apasat cu mouse-ul
            tile = int(row * 3 + column) #determina numarul patratului in matrice
            tiles[tile] = turn #se adauga mutarea in lista
            if turn == 'x':
                turn = '0' #randul ii revine urmatorului jucator
            else:
                turn = 'x'
    draw(tile)

def drawline(column, row, direction): #deseneaza o linie deasupra pieselor castigatoare
    global t
    x, y = -300, 300 #coordonate stanga sus
    if direction == 'vertical': #o linie verticala a castigat
        x = x + 100 + column * 200 #calculeaza mijlocul coloanei castigatoare, bazat pe win()
        goto(x, y) 
        t.setheading(270) #seteaza directia in jos
        t.forward(600)
    if direction == 'horizontal': #o linie orizontala a castigat
        y = y - 100 - row * 200 ##calculeaza mijlocul liniei castigatoare
        goto(x, y)
        t.setheading(0) #seteaza directia stanga - dreapta
        t.forward(600) 
    if direction == 'firstd': #diagonala principala a castigat
        goto(x, y + 10) #putin deasupra coltului stanga sus pentru a nu se confunda linia desenata cu x-urile
        t.setheading(315) #directia SE
        t.forward(1000)
    if direction == 'secondd': #diagonala secundara a castigat
        goto(x + 600, y + 10) #putin deasupra coltului dreapta sus pentru a nu se confunda linia desenata cu x-urile
        t.setheading(225) #directia SV
        t.forward(1000)

#verifica la fiecare click daca x sau 0 a castigat
def win():
    global tiles
    if tiles[0] == tiles[1] == tiles[2] and tiles[0] != "": #daca s-a castigat pe prima linie
        print("a castigat ", tiles[0]) #afiseaza cine a castigat
        drawline(0, 0, 'horizontal') #se deseneaza linia pe linia castigatoare
        return True #finalul jocului
    if tiles[3] == tiles[4] == tiles[5] and tiles[3] != "": #daca s-a castigat pe a doua linie
        print("a castigat ", tiles[3]) 
        drawline(0, 1, 'horizontal') #se deseneaza linia pe linia castigatoare
        return True 
    if tiles[6] == tiles[7] == tiles[8] and tiles[6] != "": #daca s-a castigat pe a treia linie
        print("a castigat ", tiles[6]) 
        drawline(0, 2, 'horizontal') #se deseneaza linia pe linia castigatoare
        return True
    if tiles[0] == tiles[3] == tiles[6] and tiles[0] != "": #daca s-a castigat pe prima coloana
        print("a castigat ", tiles[0]) 
        drawline(0, 0, 'vertical') #se deseneaza linia pe coloana castigatoare
        return True
    if tiles[1] == tiles[4] == tiles[7] and tiles[1] != "": #daca s-a castigat pe a doua coloana
        print("a castigat ", tiles[1]) 
        drawline(1, 0, 'vertical') #se deseneaza linia pe coloana castigatoare
        return True 
    if tiles[2] == tiles[5] == tiles[8] and tiles[2] != "": #daca s-a castigat pe a treia coloana
        print("a castigat ", tiles[2]) 
        drawline(2, 0, 'vertical') #se deseneaza linia pe coloana castigatoare
        return True 
    if(tiles[0] == tiles[4] == tiles[8]) and tiles[0] != "": #daca s-a castigat pe diagonala principala
        print("a castigat ", tiles[0]) 
        drawline(0, 0, 'firstd') #se deseneaza linia pe diagonala principala
        return True 
    if(tiles[2] == tiles[4] == tiles[6]) and tiles[2] != "": #daca s-a castigat pe diagonala secundara
        print("a castigat ", tiles[2]) 
        drawline(2, 0, 'secondd') #se deseneaza linia pe diagonala secundara
        return True 
    
    return False #daca nimeni nu a castigat, jocul continua

#verifica daca toate patratele au fost desenate
def alldrawn():
    global tiles
    for i in tiles:
        if i == "":
            return False #nu toate patratele au fost desenate
    return True #se incheie jocul
    