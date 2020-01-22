import boggle_board_randomizer as random
import tkinter as tk
from button import Boggbutt

BOARD_HEIGHT = 500
BOARD_WIDTH = 500
BOGGLE_SIDE = 4


class Board:
    def __init__(self, letter_list):
        self.letter_list = letter_list
        self.root = tk.Tk()
        self.height = BOARD_HEIGHT
        self.width = BOARD_WIDTH
        self.boggle_buttons = self.create_boggle_buttons()
        self.cur_letters = self.create_letter_list_label()

    def create_boggle_buttons(self):
        boggle_frame = tk.Frame(self.root, height=200, width=200)
        boggle_frame.pack()
        boggle_frame.place(in_=self.root, anchor='c', relx=.5, rely=.5)
        list_of_butts = []
        counter = 1
        butt_row = 0
        for row in self.letter_list:
            butt_col = 0
            for letter in row:
                cur_button = tk.Button(boggle_frame, text=letter, font=('Forte', 20), height=1, width=2)
                cur_button = tk.Button(boggle_frame, text=letter, font=('Uppercut Angle', 20), height=1, width=2)
                cur_bogg_button = Boggbutt('button' + str(counter), letter, cur_button)
                list_of_butts.append(cur_bogg_button)
                cur_button.grid(row=butt_row, column=butt_col)
                counter += 1
                butt_col += 1
            butt_row += 1
        return list_of_butts

    def create_letter_list_label(self):
        cur_string_label = tk.Label(self.root, width=23, height=2, bg='white', relief='sunken', font=('Forte', 10))
        cur_string_label.place(in_=self.root, anchor='c', relx=.5, rely=.20)
        return cur_string_label





