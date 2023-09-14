from tkinter import *
from PIL import ImageTk
from time import sleep 
from random import randint
from playsound import playsound
from tkinter import messagebox  
import winsound
import threading
import time

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
        self.text_score = self.canvas.create_text(738, 22, fill="red", font=("Times", 30), tag="score")
        self.start_time = time.time()  # Thời điểm bắt đầu đếm ngược
        self.duration = 60  # Thời gian đếm ngược (60 giây)
    
    def play_sound(self, filename):
        def _play_sound_coin():
            winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)
        
        threading.Thread(target=_play_sound_coin).start()
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
            self.play_sound("coin_touch.wav")
            self.canvas.delete("score")
            self.score += 1
            self.canvas.itemconfig(self.text_score, text=str(self.score))
            self.canvas.delete("coin")
            self.y = 5
            self.x = randint(2, 750)
            self.canvas.coords(self.coin, self.x, self.y)

        self.canvas.after(50, self.coin_fall)

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
        
        self.background = self.canvas.create_image(0,0,anchor=NW,image=self.img[0])
        self.coin = self.canvas.create_image(self.x,self.y,anchor=NW,image=self.img[1])
        self.hand =self.canvas.create_image(0,340,anchor=NW,image=self.img[2])
        self.canvas.update()
        
        self.event=Event(self.game,self.canvas,self.coin,self.hand)   
        
        self.event.coin_fall()
        self.canvas.bind("<Key>",self.event.move_hand)       
        self.canvas.focus_set()  # Đảm bảo canvas nhận được sự kiện phím
        self.game.mainloop()

class HomePage:
    def __init__(self) -> None:
        self.game= Tk()
        self.game.title("Home Page")
        self.game.iconbitmap("logo.ico")
        self.canvas = Canvas(master=self.game, width=800, height=500)
        self.canvas.pack()
        
        self.img_background = ImageTk.PhotoImage(file="background.png")
        self.background = self.canvas.create_image(0, 0, anchor=NW, image=self.img_background)
        self.img_button_start_game = ImageTk.PhotoImage(file="startgame.png")
        self.button_start_game = Button(self.game,command=self.start_game ,image=self.img_button_start_game, borderwidth=10, highlightthickness=0)
        self.button_start_game.place(x=332, y=141)
        self.img_button_quit_game = ImageTk.PhotoImage(file="quitgame.png")
        self.button_quit_game = Button(self.game,command=self.quit_game,image=self.img_button_quit_game,borderwidth=10)
        self.button_quit_game.place(x=332,y=246)
        self.game.mainloop()

    def start_game(self):
        self.game.destroy()  # Đóng cửa sổ của trang chủ
        self.game = Game()    
    def quit_game(self):
        self.game.quit()
class App:
    def __init__(self) -> None:
        self.new_app= HomePage()

if __name__=="__main__":
    App()

    