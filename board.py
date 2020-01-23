import boggle_board_randomizer as random
import tkinter as tk
from button import Boggbutt

BOARD_HEIGHT = 500
BOARD_WIDTH = 500
BOGGLE_SIDE = 4

ICON = 'graphics\cat_icon.ico'
TITLE = 'BOGGLENOVELA'
BACKGROUND_IMAGE = 'graphics/imbackground.gif'
BUTTON_NOT_PRESSED = 'graphics/normal_button.gif'
BUTTON_PRESSED = 'graphics/button_pressed.gif'
WORD_LIST_IM = 'graphics/word_list.gif'



class Board:
    def __init__(self, letter_list):
        self.letter_list = letter_list
        self.background_label = None
        self.root = tk.Tk()
        self.create_root()
        self.boggle_buttons = self.create_boggle_buttons()
        self.cur_letters = self.create_letter_list_label()
        self.correct_words_box = self.create_listbox()
        self.check_butt = self.create_check_butt()
        self.score_label = self.create_score_label()
        self.quit_butt = self.create_quit_butt()



    def create_boggle_buttons(self):
        boggle_frame = tk.Frame(self.root)
        boggle_frame.place(in_=self.root, anchor='c', relx=.5, rely=.60)
        pic = tk.PhotoImage(file=BUTTON_NOT_PRESSED)
        list_of_butts = []
        counter = 1
        butt_row = 0
        for row in self.letter_list:
            butt_col = 0
            for letter in row:
                cur_button = tk.Button(boggle_frame, image=pic, compound='center', text=letter,
                                       font=('calibri light', 17, 'bold'), background='#f5bdc6')
                cur_button.image = pic
                cur_bogg_button = Boggbutt('button' + str(counter), letter,
                                           cur_button)
                list_of_butts.append(cur_bogg_button)
                cur_button.grid(row=butt_row, column=butt_col, sticky='nesw')
                counter += 1
                butt_col += 1
            butt_row += 1
        return list_of_butts

    def change_buttons_to_normal(self):
        for butt in self.boggle_buttons:
            butt.is_pressed = False
            butt.button.config(state='normal')
            pic = tk.PhotoImage(file=BUTTON_NOT_PRESSED)
            butt.button.config(image=pic)
            butt.button.image = pic

    def change_button_to_pressed(self, butt):
        butt.is_pressed = True
        pic = tk.PhotoImage(file=BUTTON_PRESSED)
        butt.button.config(image=pic)
        butt.button.image = pic

    def create_letter_list_label(self):
        cur_string_label = tk.Label(self.root, width=22, height=2, bg='#f3dee1',
                                    relief='sunken', font=('Calibri Light', 10, 'bold'))
        cur_string_label.place(in_=self.root, anchor='c', relx=.5, rely=.33)
        return cur_string_label

    def create_listbox(self):
        list_frame = tk.Frame(self.root, bd=2, background='#f3dee1')
        list_frame.place(in_=self.root, anchor='w', relx=.7, rely=.6)
        scroll_bar = tk.Scrollbar(list_frame)
        scroll_bar.pack(side='right', fill='y')
        correct_words = tk.Listbox(list_frame, bd=2.5,
                                   yscrollcommand=scroll_bar.set, width=20,
                                   height=9, relief='sunken', background='#f3dee1')
        correct_words.pack()
        scroll_bar.config(command=correct_words.yview)
        return correct_words

    def create_check_butt(self):
        check = tk.Button(self.root, width=10, height=2, bg="pink",
                          text="CHECK WORD", font=('calibri light', 8, 'bold'))
        check.place(in_=self.root, anchor='w', relx=.69, rely=.33)
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
        score = tk.Label(self.root, bg="#f3dee1", fg='black', relief='sunken', width=16,
                         height=2, font=('calibri light', 10, 'bold'))
        score.place(in_=self.root, anchor="e", relx=.3, rely=.65)
        return score

    def create_quit_butt(self):
        butt = tk.Button(self.root, width=8, height=1, bg="pink",
                         text="QUIT", font=('calibri light', 8, 'bold'))
        butt.place(in_=self.root, anchor='c', relx=.5, rely=.90)
        return butt


