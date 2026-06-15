import tkinter as tk
import random
from tkinter import messagebox
from logic.constants import COLOR_GRID, COLOR_EMPTY, COLOR_CELLS


class Joc2048(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048 Neon Edition')

        self.main_grid = tk.Frame(self, bg=COLOR_GRID, bd=3, width=400, height=400)
        self.main_grid.grid(pady=(10, 10), padx=(10, 10))

        self.cells = []
        self.matrix = [[0] * 4 for _ in range(4)]
        self.won = False

        self.make_gui()
        self.start_game()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

    def make_gui(self):
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(self.main_grid, bg=COLOR_EMPTY, width=100, height=100)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=COLOR_EMPTY, justify=tk.CENTER,
                                       font=("Verdana", 30, "bold"), width=4, height=2)
                cell_number.grid(row=i, column=j)
                row.append(cell_number)
            self.cells.append(row)

    def start_game(self):
        self.matrix = [[0] * 4 for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()
        self.update_gui()

    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.matrix[r][c] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.matrix[row][col] = random.choice([2, 4])

    def update_gui(self):
        for i in range(4):
            for j in range(4):
                val = self.matrix[i][j]
                if val == 0:
                    self.cells[i][j].configure(text="", bg=COLOR_EMPTY)
                else:
                    bg_color, fg_color = COLOR_CELLS.get(val, ("#2e0a3d", "#ffffff"))
                    self.cells[i][j].configure(text=str(val), bg=bg_color, fg=fg_color)
        self.update_idletasks()

    def can_move(self):
        if any(0 in row for row in self.matrix):
            return True
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1] or self.matrix[j][i] == self.matrix[j + 1][i]:
                    return True
        return False

    def check_status(self):
        if any(2048 in row for row in self.matrix) and not self.won:
            self.won = True
            messagebox.showinfo("FELICITARI!", "ai castigat esti cel mai tare")

        if not self.can_move():
            over_frame = tk.Frame(self.main_grid, bg="#000000")
            over_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=1.0, relheight=1.0)
            tk.Label(over_frame, text="game over\nwomp womp :(",
                     bg="#000000", fg="#ff00ff",
                     font=("Verdana", 25, "bold"), justify=tk.CENTER).place(relx=0.5, rely=0.5, anchor="center")

    def stack(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_pos = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_pos] = self.matrix[i][j]
                    fill_pos += 1
        self.matrix = new_matrix

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0

    def reverse(self):
        self.matrix = [row[::-1] for row in self.matrix]

    def transpose(self):
        self.matrix = [list(row) for row in zip(*self.matrix)]

    def move(self):
        self.add_new_tile()
        self.update_gui()
        self.check_status()

    def left(self, event):
        old = [r[:] for r in self.matrix]
        self.stack()
        self.combine()
        self.stack()
        if old != self.matrix:
            self.move()

    def right(self, event):
        old = [r[:] for r in self.matrix]
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        if old != self.matrix:
            self.move()

    def up(self, event):
        old = [r[:] for r in self.matrix]
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        if old != self.matrix:
            self.move()

    def down(self, event):
        old = [r[:] for r in self.matrix]
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        if old != self.matrix:
            self.move()
