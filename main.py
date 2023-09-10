from tkinter import *
from PIL import ImageTk
from time import sleep 
from random import randint
from playsound import playsound
from tkinter import messagebox  

class Event:
    def __init__(self, game, canvas, coin, hand):
        self.game = game
        self.canvas = canvas
        self.coin = coin
        self.hand = hand
        self.y = 5  # tạo độ khoảng cách gắn trên trục y
        self.x = randint(30, 720)  # tạo đô
        self.limit_left = -2
        self.limit_right = 650
        self.score = 0
        self.text_score = self.canvas.create_text(745, 22, fill="red", font=("Times", 30), tag="score")
        
    def coin_fall(self):
        self.canvas.move(self.coin, 0, 10)
        self.y += 10
        # khoảng rơi [0;550]
        if self.y >= 550:
            self.y = 5 # khoảng cách mỗi lần rơi
            self.x = randint(2, 750)
            self.canvas.coords(self.coin, self.x, self.y)
        # lấy tạo độ x,y của tiền và
        self.coin_coords_x = self.canvas.coords(self.coin)[0]
        self.hand_coords_x = self.canvas.coords(self.hand)[0]
        self.coin_coords_y = self.canvas.coords(self.coin)[1]
        self.hand_coords_y = self.canvas.coords(self.hand)[1]

        self.text_score = self.canvas.create_text(745, 22,text=f"SCORE:"+str(self.score), fill="red", font=("Times", 20), tag="score")

        if self.coin_coords_x + 50 >= self.hand_coords_x and self.coin_coords_x + 50 <= self.hand_coords_x + 178 and self.coin_coords_y + 50 >= self.hand_coords_y and self.coin_coords_y <= self.hand_coords_y + 80:
            self.canvas.delete("score")
            self.score += 1
            self.canvas.itemconfig(self.text_score, text=str(self.score))
            self.canvas.delete("coin")
            self.y = 5
            self.x = randint(2, 750)
            self.canvas.coords(self.coin, self.x, self.y)

        self.canvas.after(100, self.coin_fall)

    def right(self):
        self.current_x=self.canvas.coords(self.hand)[0] # lấy vị trí của bàn tay hiện tại và thay đổi trục x
        if self.current_x <= self.limit_right:
            self.canvas.move(self.hand,30,0)
            self.canvas.update()

    def left(self):
        self.current_y=self.canvas.coords(self.hand)[0] # lấy vị trí của bàn tay hiện tại và thay đổi trục current_y
        if self.current_y > self.limit_left:
            self.canvas.move(self.hand,-30.56412,0)
            self.canvas.update()
            
    def move_hand(self,event):
        if event.keysym =="Right":
            self.right()
        elif event.keysym =="Left":
            self.left()
    
    def exit_game(self):
        self.game.quit()
class Game:
    def __init__(self):
        self.game=Tk()
        # self.game.geometry("800x500")
        self.game.title("DOGECOIN GAME")
        self.game.iconbitmap("logo.ico")
        self.canvas =Canvas(master=self.game,width=800,height=500)
        self.canvas.pack()
        self.img= [0,0,0]
        self.y=5
        self.x=randint(20,800)
        self.img[0]=ImageTk.PhotoImage(file="background.png")
        self.img[1]=ImageTk.PhotoImage(file="coin.png")
        self.img[2]=ImageTk.PhotoImage(file="hand.png")
        
        # self.background = self.canvas.create_image(0,0,anchor=NW,image=self.img[0])
        self.coin = self.canvas.create_image(self.x,self.y,anchor=NW,image=self.img[1])
        self.hand =self.canvas.create_image(0,340,anchor=NW,image=self.img[2])
        self.canvas.update()
        
        self.event=Event(self.game,self.canvas,self.coin,self.hand)
        
        self.exit_button = Button(self.game,text="X",bg="red",command=self.event.exit_game)
        self.exit_button.place(x=4,y=12)    
        
        self.event.coin_fall()
        self.canvas.bind("<Key>",self.event.move_hand)       
        self.canvas.focus_set()  # Đảm bảo canvas nhận được sự kiện phím
        self.game.mainloop()

if __name__=="__main__":
    new_game=Game()
