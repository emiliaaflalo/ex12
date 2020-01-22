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
        self.cur_string = tk.StringVar()
        self.cur_string.set('')
        self.board.cur_letters.config(textvariable=self.cur_string)
        self.board.score_label.config(text="Your Score Is: \n" + str(self.score))

    def create_butt_locations(self):
        for button in self.board.boggle_buttons:
            button.location = BUTTON_LOCATIONS[button.get_name()]

    def boggle_button_click(self, location, letter, bogg_butt):
        self.cur_letters.append(letter)
        current = ''
        self.cur_string.set(current.join(self.cur_letters))
        bogg_butt.is_pressed = True
        bogg_butt.button.config(background='pink')
        for bogg_button in self.board.boggle_buttons:
            if not (location[0] - 1 <= bogg_button.location[0] <= location[0] + 1 and
                    location[1] - 1 <= bogg_button.location[1] <= location[1] + 1) or bogg_button.is_pressed:
                bogg_button.button.config(state='disabled')
            else:
                bogg_button.button.config(state='normal')

    def create_bogg_butt_commands(self):
        for bogg_butt in self.board.boggle_buttons:
            bogg_butt.button.config(command=lambda location=bogg_butt.location,
                                    letter=bogg_butt.letter, button=bogg_butt:
                                    self.boggle_button_click(location, letter, button))

    def create_check_button_command(self):
        self.board.check_butt.config(command=self.check_word)

    def check_word(self):
        word = ""
        word = word.join(self.cur_letters)
        if word in self.legal_words and word not in self.correct_words:
            self.correct_words.append(word)
            self.board.correct_words_box.insert(0, word)
            self.score += len(word) ** 2
            self.board.score_label.config(
                text="Your Score Is: \n" + str(self.score))
        elif word not in self.legal_words:
            pass
        self.cur_letters = []
        self.cur_string.set("")
        for butt in self.board.boggle_buttons:
            butt.is_pressed = False
            butt.button.config(state='normal')
            butt.button.config(background='white')


class Timer:
    def __init__(self, root):
        self.root = root
        self.secs = SECONDS
        self.label = tk.Label(self.root, bg="pink",
                              text="Time Left: \n" + str(datetime.timedelta(seconds=self.secs)), width=16, height=2, )
        self.label.place(in_=self.root, anchor="e", relx=.31, rely= .4)
        self.root.after(1000, self.refresh_timer)

    def refresh_timer(self):
        self.secs -= 1
        self.label.configure(text="Time Left: \n" + str(datetime.timedelta(seconds=self.secs)))
        self.root.after(1000, self.refresh_timer)

def create_word_list(filename):
    f = open(filename, "r")
    legal_words = [line.strip("\n") for line in f]
    return legal_words


def create_random_letters():
    random_letters = random.randomize_board()
    return random_letters

if __name__ == '__main__':
    correct_words = create_word_list('boggle_dict.txt')
    cur_letters = create_random_letters()
    board_game = Board(cur_letters)
    my_timer = Timer(board_game.root)
    cur_game = Game(board_game, cur_letters, my_timer, correct_words)
    cur_game.board.root.geometry('500x500')
    cur_game.create_butt_locations()
    cur_game.create_bogg_butt_commands()
    cur_game.create_check_button_command()
    cur_game.board.root.resizable(width=False, height=False)
    cur_game.board.root.mainloop()

