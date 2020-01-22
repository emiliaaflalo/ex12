import boggle_board_randomizer as random
from board import Board
import tkinter as tk
import time
import datetime
from button import Boggbutt

BUTTON_LOCATIONS = {'button1': (0, 0), 'button2': (0, 1), 'button3': (0, 2), 'button4': (0, 3),
                    'button5': (1, 0), 'button6': (1, 1), 'button7': (1, 2), 'button8': (1, 3),
                    'button9': (2, 0), 'button10': (2, 1), 'button11': (2, 2), 'button12': (2, 3),
                    'button13': (3, 0), 'button14': (3, 1), 'button15': (3, 2), 'button16': (3, 3)}
BOGGLE_SIDE = 4
SECONDS = 180

def create_word_list(filename):
    f = open(filename, "r")
    legal_words = [line.strip("\n") for line in f]
    return legal_words


def create_random_letters():
    random_letters = random.randomize_board()
    return random_letters

class Game:
    def __init__(self, board, letter_mat, timer, legal_words):
        self.board = board
        self.timer = timer
        self.score = 0
        self.legal_words = legal_words
        self.right_words = []
        self.root = self.board.root
        self.letter_mat = letter_mat
        self.cur_letters = []
        self.correct_words = []

    def create_butt_locations(self):
        for button in self.board.boggle_buttons:
            button.location = BUTTON_LOCATIONS[button.get_name()]

    def boggle_button_click(self, location, letter):
        self.cur_letters.append(letter)
        global cur_string
        cur_string = tk.StringVar()
        current = ''
        cur_string.set(current.join(self.cur_letters))
        print(cur_string)
        for bogg_button in self.board.boggle_buttons:
            if not (location[0] - 1 <= bogg_button.location[0] <= location[0] + 1 and
                    location[1] - 1 <= bogg_button.location[1] <= location[1] + 1):
                bogg_button.button.config(state='disabled')
            else:
                bogg_button.button.config(state='normal')

    def create_bogg_butt_commands(self):
        for bogg_butt in self.board.boggle_buttons:
            bogg_butt.button.config(command=lambda location=bogg_butt.location,
                                    letter=bogg_butt.letter: self.boggle_button_click(location, letter))

    def check_word(self, letters_list):
        word = ""
        for letter in letters_list:
            word.join(letter)
        if word in self.legal_words:
            self.correct_words.append(word)
            self.score += len(word)**2
        elif word not in self.legal_words:
            pass
        self.cur_letters = []



class Timer:
    def __init__(self, root):
        self.root = root
        self.secs = SECONDS
        self.label = tk.Label(self.root, bg="pink",
                              text=str(datetime.timedelta(seconds=self.secs)))
        self.label.pack(side=tk.TOP)
        self.root.after(1000, self.refresh_timer)

    def refresh_timer(self):
        self.secs -= 1
        self.label.configure(text=str(datetime.timedelta(seconds=self.secs)))
        self.root.after(1000, self.refresh_timer)


if __name__ == '__main__':
    cur_letters = create_random_letters()
    board_game = Board(cur_letters)
    my_timer = Timer(board_game.root)
    cur_game = Game(board_game,cur_letters,my_timer)
    cur_game.board.root.geometry('500x500')
    cur_game.create_butt_locations()
    cur_game.create_bogg_butt_commands()
    cur_game.board.root.resizable(width=False, height=False)
    cur_game.board.root.mainloop()




