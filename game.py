import boggle_board_randomizer as random
from board import Board
import tkinter as tk
import time
from button import Boggbutt

BUTTON_LOCATIONS = {'button1': (0, 0), 'button2': (0, 1), 'button3': (0, 2), 'button4': (0, 3),\
                    'button5': (1, 0), 'button6': (1, 1), 'button7': (1, 2), 'button8': (1, 3),\
                    'button9': (2, 0), 'button10': (2, 1), 'button11': (2, 2), 'button12': (2, 3),\
                    'button13': (3, 0), 'button14': (3, 1), 'button15': (3, 2), 'button16': (3, 3)}
BOGGLE_SIDE = 4

class Game:
    def __init__(self, board, letter_mat, timer=None):
        self.board = board
        self.timer = timer
        self.score = 0
        self.right_words = []
        self.root = self.board.root
        self.letter_mat = letter_mat

    def create_butt_locations(self):
        for button in self.board.boggle_buttons:
            button.location = BUTTON_LOCATIONS[button.get_name()]

    def boggle_button_click(self, letter, location):
        for bogg_button in self.board.boggle_buttons:
            if not (location[0] - 1 <= bogg_button.location[0] <= location[0] + 1 and
                    location[1] - 1 <= bogg_button.location[1] <= location[1] + 1):
                bogg_button.button.config(state='disabled')

    def create_bogg_butt_commands(self):
        for bogg_butt in self.board.boggle_buttons:
            bogg_butt.button.config(command=lambda: self.boggle_button_click(bogg_butt.letter, bogg_butt.location))


def create_word_list(filename):
    f = open(filename, "r")
    legal_words = [line.strip("\n") for line in f]
    return legal_words


def create_random_letters():
    random_letters = random.randomize_board()
    return random_letters

#class Timer:

 #   def __init__(self, board):
  #      self.board = board
   #     self.root = self.board.root
   #     self.label = tk.Label(text="")
   #     self.label.pack(side=tk.TOP)
   #     self.root.after(1000, self.update_timer())
    #    self.root.mainloop()

   # def update_timer(self):
    #    now = time.strftime("%H:%M:%S")
     ##   self.label.configure(text=now)
       # self.root.after(1000, self.update_timer())


if __name__ == '__main__':
    cur_letters = create_random_letters()
    board_game = Board(cur_letters)
    cur_game = Game(board_game, cur_letters)
    cur_game.board.root.geometry('500x500')
    cur_game.create_butt_locations()
    cur_game.create_bogg_butt_commands()
    cur_game.board.root.resizable(width=False, height=False)
    cur_game.board.root.mainloop()
   # my_timer = Timer(board_game)
    #my_game = Game(board_game, my_timer)
