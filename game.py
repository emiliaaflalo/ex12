from board import Board
import tkinter as tk
from tkinter import messagebox
import datetime
import boggle

BUTTON_LOCATIONS = {'button1': (0, 0), 'button2': (0, 1), 'button3': (0, 2),
                    'button4': (0, 3),
                    'button5': (1, 0), 'button6': (1, 1), 'button7': (1, 2),
                    'button8': (1, 3),
                    'button9': (2, 0), 'button10': (2, 1), 'button11': (2, 2),
                    'button12': (2, 3),
                    'button13': (3, 0), 'button14': (3, 1), 'button15': (3, 2),
                    'button16': (3, 3)}
BOGGLE_SIDE = 4
SECONDS = 180
WRONG_WORD_MESSAGE = "This word doesn't exist! try again"
DUPLICATE_WORD_MESSAGE = "You've used this word already! try again"


class Timer:
    def __init__(self, root):
        self.root = root
        self.secs = SECONDS
        self.label = tk.Label(self.root, bg="#f3dee1", fg='black',
                              text=str(datetime.timedelta(seconds=self.secs)),
                              width=16, height=2,
                              font=('calibri light', 10, 'bold'),
                              relief='sunken')
        self.label.place(in_=self.root, anchor="e", relx=.3, rely=.48)
        self.root.after(1000, self.refresh_timer)

    def flash(self):
        if self.secs > 0:
            if self.secs == 60:
                self.label.configure(background='#f3dee1', fg='#e93a57')
            bg = self.label.cget("background")
            fg = self.label.cget("foreground")
            self.label.configure(background=fg, foreground=bg)
            self.root.after(500, self.flash)

    def times_up(self):
        if self.secs <= 0:
            end_message = \
                messagebox.askquestion("Time's Up!", "Nice one! Mitzi Biton"
                                                     " will be proud! \n Do "
                                                     "you want to play "
                                                     "again?", icon=None)
            if end_message == "yes":
                self.root.destroy()
                boggle.run_game()
            else:
                self.root.destroy()
        else:
            return

    def refresh_timer(self):
        if self.secs == 60:
            self.flash()
        elif self.secs <= 0:
            self.times_up()
            return
        self.secs -= 1
        self.label.configure(text=str(datetime.timedelta(seconds=self.secs)))
        self.root.after(1000, self.refresh_timer)


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
        self.board.score_label.config(text=str(self.score))
        self.board.quit_butt.configure(command=self.exit_program)

    def create_butt_locations(self):
        for button in self.board.boggle_buttons:
            button.location = BUTTON_LOCATIONS[button.get_name()]

    def boggle_button_click(self, location, letter, bogg_butt):
        self.cur_letters.append(letter)
        current = ''
        self.cur_string.set(current.join(self.cur_letters))
        self.board.change_button_to_pressed(bogg_butt)
        for bogg_button in self.board.boggle_buttons:
            if not (location[0] - 1 <= bogg_button.location[0] <= location[
                0] + 1 and
                    location[1] - 1 <= bogg_button.location[1] <= location[
                        1] + 1) or bogg_button.is_pressed:
                bogg_button.button.config(state='disabled')
            else:
                bogg_button.button.config(state='normal')

    def create_bogg_butt_commands(self):
        for bogg_butt in self.board.boggle_buttons:
            bogg_butt.button.config(command=lambda location=bogg_butt.location,
                                                   letter=bogg_butt.letter,
                                                   button=bogg_butt:
            self.boggle_button_click(location, letter, button))

    def create_check_button_command(self):
        self.board.check_butt.config(command=self.check_word)

    def check_word(self):
        word = ""
        word = word.join(self.cur_letters)
        if word in self.legal_words:
            if word in self.correct_words:
                message = messagebox.showinfo('Nope', DUPLICATE_WORD_MESSAGE)
            else:
                self.correct_words.append(word)
                self.board.correct_words_box.insert(0, word)
                self.score += len(word) ** 2
                self.board.score_label.config(text=str(self.score))
        elif word not in self.legal_words:
            message = messagebox.showinfo('Undefined', WRONG_WORD_MESSAGE)
        self.cur_letters = []
        self.cur_string.set("")
        self.board.change_buttons_to_normal()

    def exit_program(self):
        exit_message = messagebox.askquestion('Quit Game',
                                              'Are you sure you want to quit?',
                                              icon='warning')
        if exit_message == 'yes':
            self.root.destroy()
        else:
            tk.messagebox.showinfo('Return', 'Yay! back to the game then')
