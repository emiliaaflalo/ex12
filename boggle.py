import boggle_board_randomizer as random
import tkinter as tk
import time
BOARD_HEIGHT = 500
BOARD_WIDTH = 500
BOGGLE_SIDE = 4


def create_word_list(filename):
    f = open(filename, "r")
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


def create_placements():
    list_of_place =[]
    start_x = 150
    start_y = 150
    for i in range(BOGGLE_SIDE):
        for j in range(BOGGLE_SIDE):
            list_of_place.append((start_x, start_y))
            start_x += 2
        start_x = 150
        start_y += 2
    return list_of_place



class Board:
    def __init__(self, letter_list):
        self.letter_list = letter_list
        self.timer = 3
        self.score = 0
        self.right_words = []
        self.root = tk.Tk()
        self.height = BOARD_HEIGHT
        self.width = BOARD_WIDTH

    def create_boggle_buttons(self):
        boggle_frame = tk.Frame(self.root, height=200, width=200)
        boggle_frame.pack()
        boggle_frame.place(in_=self.root, anchor='c', relx=.5, rely=.5)
        dic_of_butts = {}
        counter = 1
        butt_row = 0
        for row in self.letter_list:
            butt_col = 0
            for letter in row:
                cur_button = tk.Button(boggle_frame, text=letter, font=('Helvetica', 20))
                dic_of_butts['button'+str(counter)] = cur_button
                cur_button.grid(row=butt_row, column=butt_col)
                counter += 1
                butt_col += 1
            butt_row += 1




if __name__ == '__main__':
    board_game = Board(create_board())
    board_game.root.geometry('500x500')
    board_game.create_boggle_buttons()
    board_game.root.resizable(width=False, height=False)
    board_game.root.mainloop()
