#Copyright 2022 George Raducanu <georgecristian2002@gmail.com>
from tkinter import *
from tkinter import messagebox
import random

class Board:
    bg_color={
        '2': '#eee4da',
        '4': '#eee4da',
        '8': '#eee4da',
        '16': '#eee4da',
        '32': '#eee4da',
        '64': '#eee4da',
        '128': '#eee4da',
        '256': '#eee4da',
        '512': '#eee4da',
        '1024': '#eee4da',
        '2048': '#eee4da',
    }
    color={
        '2': '#f9f6f2',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#f9f6f2',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }

    def __init__(self):
        self.n=4
        self.window=Tk()
        self.window.title('2048 Game! It begins!')
        self.gameArea=Frame(self.window,bg= 'azure4')
        self.board=[]
        self.gridcell=[[0]*4 for i in range(4)]
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0
        
        for i in range(4):
            rows=[]
            for j in range(4):
                l=Label(self.gameArea,text='',bg='azure4',
                font=('calibri',24,'bold'),width=4,height=2)
                l.grid(row=i,column=j,padx=7,pady=7)
                rows.append(l)
            self.board.append(rows)
        self.gameArea.grid()

    def reverse(self):
        for w in range(4):
            i=0
            j=3
            while(i<j):
                self.gridcell[w][i],self.gridcell[w][j]=self.gridcell[w][j],self.gridcell[w][i]
                i+=1
                j-=1

    def transpose(self):
        self.gridcell=[list(t)for t in zip(*self.gridcell)]

    def compressgrid(self):
        self.compress=False
        temporary=[[0] *4 for i in range(4)]
        for i in range(4):
            count=0
            for j in range(4):
                if self.gridcell[i][j]!=0:
                    temporary[i][count]=self.gridcell[i][j]
                    if count!=j:
                        self.compress=True
                    count+=1
        self.gridcell=temporary

    def mergegrid(self):
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridcell[i][j] == self.gridcell[i][j + 1] and self.gridcell[i][j] != 0:
                    self.gridcell[i][j] *= 2
                    self.gridcell[i][j + 1] = 0
                    self.score += self.gridcell[i][j]
                    self.merge = True

    def random_cell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridcell[i][j] == 0:
                    cells.append((i, j))

        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridcell[i][j]=2

    def can_merge(self):
        for i in range(4):
            for j in range(3):
                if self.gridcell[i][j] == self.gridcell[i][j+1]:
                    return True
        
        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False

    def paintgrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='azure4')
                else:
                    self.board[i][j].config(text=str(self.gridcell[i][j]),
                    bg=self.bg_color.get(str(self.gridcell[i][j])),
                    fg=self.color.get(str(self.gridcell[i][j])))

class Game:
    def __init__(self,panel):
        self.panel=panel
        self.end=False
        self.won=False

    def start(self):
        self.panel.random_cell()
        self.panel.random_cell()
        self.panel.paintgrid()
        self.panel.window.bind('<Key>', self.link_keys)
        self.panel.window.mainloop()
    
    def link_keys(self,event):
        if self.end or self.won:
            return

        self.panel.compress = False
        self.panel.merge = False
        self.panel.moved = False
        presed_key=event.keysym
        if presed_key=='Up':
            self.panel.transpose()
            self.panel.compressgrid()
            self.panel.mergegrid()
            self.panel.moved = self.panel.compress or self.panel.merge
            self.panel.compressgrid()
            self.panel.transpose()
        elif presed_key=='Down':
            self.panel.transpose()
            self.panel.reverse()
            self.panel.compressgrid()
            self.panel.mergegrid()
            self.gamepanel.moved = self.panel.compress or self.panel.merge
            self.panel.compressgrid()
            self.panel.reverse()
            self.panel.transpose()
        elif presed_key=='Left':
            self.panel.compressgrid()
            self.panel.mergegrid()
            self.panel.moved = self.panel.compress or self.panel.merge
            self.panel.compressgrid()
        elif presed_key=='Right':
            self.panel.reverse()
            self.panel.compressgrid()
            self.panel.mergegrid()
            self.panel.moved = self.panel.compress or self.panel.merge
            self.panel.compressgrid()
            self.panel.reverse()
        else:
            pass

        self.panel.paintgrid()
        print(self.panel.score)

        flag=0
        for i in range(4):
            for j in range(4):
                if(self.panel.gridcell[i][j]==2048):
                    flag=1
                    break
        if(flag==1):
            self.won=True
            messagebox.showinfo('2048', message='Game WON!!! =))')
            print("You won! Congrats!")
            return

        for i in range(4):
            for j in range(4):
                if self.panel.gridcell[i][j]==0:
                    flag=1
                    break

        if not (flag or self.panel.can_merge()):
            self.end=True
            messagebox.showinfo('Game Over!!! =(( You lost!')
            print("Over")

        if self.panel.moved:
            self.panel.random_cell()
        
        self.panel.paintgrid()
    
