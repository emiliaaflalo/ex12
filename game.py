import boggle
import tkinter as tk
import time


class Game:
    def __init__(self, board, timer):
        self.board = board
        self.timer = timer
        self.score = 0
        self.right_words = []
        self.root = self.board.root


class Timer:
    def __init__(self, board):
        self.board = board
        self.root = self.board.root
        self.label = tk.Label(text="")
        self.label.pack(side=tk.TOP)
        self.root.after(1000, self.update_timer())
        self.root.mainloop()

    def update_timer(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_timer())


if __name__ == '__main__':
    board_game = boggle.Board(boggle.create_board())
    board_game.root.geometry('500x500')
    board_game.create_boggle_buttons()
    board_game.root.resizable(width=False, height=False)
    my_timer = Timer(board_game)
    my_game = Game(board_game, my_timer)
