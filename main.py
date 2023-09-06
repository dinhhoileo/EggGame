from tkinter import *
from PIL import ImageTk
from time import sleep 
from random import randint
from playsound import playsound


class Game:
    def __init__(self):
        self.game=Tk()
        # self.game.geometry("800x500")
        self.game.title("EGG GAME")
        self.canvas =Canvas(master=self.game,width=800,height=500)
        self.canvas.pack()
        self.img= [0,0,0]
        self.y=5
        self.x=randint(20,800)
        
        self.img[0]=ImageTk.PhotoImage(file="background.png")
        self.img[1]=ImageTk.PhotoImage(file="coin.png")
        self.img[2]=ImageTk.PhotoImage(file="bantay.png")
        
        self.background = self.canvas.create_image(0,0,anchor=NW,image=self.img[0])
        self.coin = self.canvas.create_image(self.x,self.y,anchor=NW,image=self.img[1])
        self.bantay =self.canvas.create_image(0,340,anchor=NW,image=self.img[2])
        self.canvas.update()
        
        self.game.mainloop()
if __name__=="__main__":
    new_game=Game()
