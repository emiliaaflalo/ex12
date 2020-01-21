import boggle_board_randomizer as random
import tkinter as tk
from button import Boggbutt

BOARD_HEIGHT = 500
BOARD_WIDTH = 500
BOGGLE_SIDE = 4





#def is_legal_word(word, word_list):
 #   if word in word_list:
  #      return True
  #  else:
   #     return False








class Board:
    def __init__(self, letter_list):
        self.letter_list = letter_list
        self.root = tk.Tk()
        self.height = BOARD_HEIGHT
        self.width = BOARD_WIDTH
        self.boggle_buttons = self.create_boggle_buttons()

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
                cur_button = tk.Button(boggle_frame, text=letter, font=('Helvetica', 20), height=1, width=2)
                cur_bogg_button = Boggbutt('button' + str(counter), letter, cur_button)
                list_of_butts.append(cur_bogg_button)
                cur_button.grid(row=butt_row, column=butt_col)
                counter += 1
                butt_col += 1
            butt_row += 1
        return list_of_butts






if __name__ == '__main__':
    board_game = Board(create_board())
    board_game.root.geometry('500x500')
    board_game.create_boggle_buttons()
    board_game.root.resizable(width=False, height=False)
    board_game.root.mainloop()
