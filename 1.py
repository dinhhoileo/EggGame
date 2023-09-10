    def coin_fall(self):
        self.canvas.move(self.coin, 0, 10)
        self.y += 10

        if self.y >= 550:
            self.y = 5
            self.x = randint(2, 750)
            self.canvas.coords(self.coin, self.x, self.y)

        self.coin_coords_x = self.canvas.coords(self.coin)[0]
        self.hand_coords_x = self.canvas.coords(self.hand)[0]
        self.coin_coords_y = self.canvas.coords(self.coin)[1]
        self.hand_coords_y = self.canvas.coords(self.hand)[1]
        
        self.text_score = self.canvas.create_text(745,22,fill="red",font=("Times",30))
        
        if  self.coin_coords_x+50 >= self.hand_coords_x and self.coin_coords_x+50 <=self.hand_coords_x +178 and self.coin_coords_y+50 >=self.hand_coords_y and self.coin_coords_y <=self.hand_coords_y+80:
            
            # self.playsound("coin_touch.wav")
            self.canvas.delete("self.score")
            self.score+=1
            self.canvas.itemconfig(self.text_score,text=str(self.score))
            self.canvas.delete("coin")
            self.y = 5
            self.x = randint(2, 750)
            self.canvas.coords(self.coin, self.x, self.y)

        self.canvas.after(100, self.coin_fall)