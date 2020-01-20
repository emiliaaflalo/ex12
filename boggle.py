import boggle_board_randomizer as random
import tkinter as tk
import time
BOARD_HEIGHT = 100
BOARD_WIDTH = 100

def create_word_list(filename):
    f = open("boggle_dict.txt", "r")
    legal_words = [line.strip("\n") for line in f]
    return legal_words


def is_legal_word(word, word_list):
    if word in word_list:
        return True
    else:
        return False


def create_board():
    board_list = random.randomize_board()
    return board_list


class Board:
    def __init__(self, letter_list):
        self.letter_list = letter_list
        self.timer = timer
        self.score = score
        self.right_words = []
        self.root = tk.Tk()
        self.height = BOARD_HEIGHT
        self.width = BOARD_WIDTH


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(width=False, height=False)

    root.mainloop()
