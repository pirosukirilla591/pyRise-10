import tkinter as tk
import random

class HalloweenGame:
    def __init__(self, master):
        self.master = master
        master.title("Pie-Rise [ Take a Candy # 1 ]")
        
        self.canvas = tk.Canvas(master, width=600, height=400, bg='black')
        self.canvas.pack()
        
        self.pumpkin = self.canvas.create_oval(275, 150, 325, 200, fill='red')
        self.score = 0
        
        self.score_label = tk.Label(master, text="Количество баллов заработанных в игре: 0", bg='black', fg='orange')
        self.score_label.pack()
        
        self.spawn_candy()
        
        self.master.bind("<Button-1>", self.cath_candy)
        
    def spawn_candy(self):
        x = random.randint(50, 550)
        self.candy = self.canvas.create_oval(x, 0, x + 30, 30, fill='yellow')
        self.fall()
        
    def fall(self):
        self.canvas.move(self.candy, 0, 5)
        pos = self.canvas.coords(self.candy)
        
        if pos[3] < 400:
            self.master.after(50, self.fall)
        else:
            self.canvas.delete(self.candy)
            self.spawn_candy()
            
    def cath_candy(self, event):
        pos = self.canvas.coords(self.candy)
        if pos[0] < event.x < pos[2] and pos[1] < event.y < pos[3]:
            self.score += 1
            self.score_label.config(text=f"Количество баллов заработанных в игре: {self.score}")
            self.canvas.delete(self.candy)
            self.spawn_candy()
            
if __name__ == "__main__":
    root = tk.Tk()
    app = HalloweenGame(root)
    root.mainloop()
