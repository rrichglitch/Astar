import tkinter as tk
import Astar_main

class draw_board:
    def __init__(self, size):
        # initialize the position array
        self.root = tk.Tk()
        self.pos = [[0] * size for i in range(size)]
        self.size = size

        self.gen_buttons()

        self.root.bind("<Button-3>", self.ends)
        restart = tk.Button(self.root, text='restart', padx=5, pady=5,command = self.gen_buttons)
        scoreB = tk.Label(self.root, text='score: 0')
        scoreB.grid(column=int(size / 2) + 1, row=size, columnspan=5)
        restart.grid(column=int(size / 2) - 4, row=size, columnspan=4)

        self.root.mainloop()

    def sink(self,p):
        mx = self.root.winfo_pointerx()- self.root.winfo_rootx()
        my = self.root.winfo_pointery() - self.root.winfo_rooty()
        # print(mx,my)
        self.pos[int(mx/34)][int(my/34)].config(relief='sunken', bg='black')

    def gen_buttons(self):
        self.scor = 0
        self.start = 0
        self.end = 0
        self.started = False

        # filling the positions with buttons
        # !!!buttons are 34x34 in kinter coords
        for x in range(self.size):
            for y in range(self.size):
                self.pos[x][y] = tk.Button(self.root, text='     ', padx=5, pady=5)
                self.pos[x][y].grid(column=x, row=y)
                self.pos[x][y].bind("<B1-Motion>", lambda p,: self.sink(p))

    def ends(self,*args):
        print("here")
        mx = self.root.winfo_pointerx() - self.root.winfo_rootx()
        my = self.root.winfo_pointery() - self.root.winfo_rooty()
        if not self.started:
            self.start = self.pos[int(mx/34)][ int(my/34)]
            self.pos[int(mx / 34)][int(my / 34)].config(bg='green')
            self.started=True
        else:
            self.end = self.pos[int(mx/34)][ int(my/34)]
            self.pos[int(mx / 34)][int(my / 34)].config(bg='red')
            self.algor = Astar_main.astar(self)


draw_board(18)
