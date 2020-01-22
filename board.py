import boggle_board_randomizer as random
import tkinter as tk
from button import Boggbutt

BOARD_HEIGHT = 500
BOARD_WIDTH = 500
BOGGLE_SIDE = 4

ICON = 'graphics\cat_icon.ico'
TITLE = 'BOGGLENOVELA'
BACKGROUND_IMAGE = 'graphics/imbackground.gif'



class Board:
    def __init__(self, letter_list):
        self.letter_list = letter_list
        self.background_label = None
        self.root = tk.Tk()
        self.create_root()
        self.height = BOARD_HEIGHT
        self.width = BOARD_WIDTH
        self.boggle_buttons = self.create_boggle_buttons()
        self.cur_letters = self.create_letter_list_label()
        self.correct_words_box = self.create_listbox()
        self.check_butt = self.create_check_butt()
        self.score_label = self.create_score_label()
        self.quit_butt = self.create_quit_butt()

    def create_boggle_buttons(self):
        boggle_frame = tk.Frame(self.root)
        boggle_frame.place(in_=self.root, anchor='c', relx=.5, rely=.60)
        list_of_butts = []
        counter = 1
        butt_row = 0
        for row in self.letter_list:
            butt_col = 0
            for letter in row:
                cur_button = tk.Button(boggle_frame, text=letter,
                                       font=('constantia', 13), height=1,
                                       width=4,
                                       background='white', compound='center')
                cur_bogg_button = Boggbutt('button' + str(counter), letter,
                                           cur_button)
                list_of_butts.append(cur_bogg_button)
                cur_button.grid(row=butt_row, column=butt_col)
                counter += 1
                butt_col += 1
            butt_row += 1
        return list_of_butts

    def create_letter_list_label(self):
        cur_string_label = tk.Label(self.root, width=25, height=2, bg='white',
                                    relief='sunken', font=('Gill sans', 10))
        cur_string_label.place(in_=self.root, anchor='c', relx=.5, rely=.33)
        return cur_string_label

    def create_listbox(self):
        list_frame = tk.Frame(self.root)
        list_frame.place(in_=self.root, anchor='w', relx=.71, rely=.6)
        scroll_bar = tk.Scrollbar(list_frame)
        scroll_bar.pack(side='right', fill='y')
        correct_words = tk.Listbox(list_frame, bd=0,
                                   yscrollcommand=scroll_bar.set, width=20,
                                   height=10)
        correct_words.pack()
        scroll_bar.config(command=correct_words.yview)
        return correct_words

    def create_check_butt(self):
        check = tk.Button(self.root, width=13, height=2, bg="pink",
                          text="CHECK WORD", font=('Gabriola', 10))
        check.place(in_=self.root, anchor='w', relx=.71, rely=.33)
        return check

    def create_root(self):
        self.root.geometry('500x500')
        self.root.iconbitmap(ICON)
        self.root.title(TITLE)
        image = tk.PhotoImage(file=BACKGROUND_IMAGE)
        self.background_label = tk.Label(self.root, image=image)
        self.background_label.image = image
        self.background_label.pack()

    def create_score_label(self):
        score = tk.Label(self.root, bg="pink", width=16, height=2)
        score.place(in_=self.root, anchor="e", relx=.3, rely=.7)
        return score

    def create_quit_butt(self):
        butt = tk.Button(self.root, width=8, height=1, bg="pink",
                         text="QUIT", command=self.root.destroy)
        butt.place(in_=self.root, anchor='c', relx=.5, rely=.90)
        return butt
