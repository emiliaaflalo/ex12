import tkinter as tk
import board
import game
import boggle_board_randomizer as random

BOARD_HEIGHT = 500
BOARD_WIDTH = 500
BOGGLE_SIDE = 4
ICON = 'graphics/cat_icon.ico'
TITLE = 'BOGGLENOVELA'
BACKGROUND_IMAGE = 'graphics/imbackground.gif'
BUTTON_NOT_PRESSED = 'graphics/normal_button.gif'
BUTTON_PRESSED = 'graphics/button_pressed.gif'
WORD_LIST_IM = 'graphics/word_list.gif'


class StartPage:
    def __init__(self):
        self.root = tk.Tk()
        self.background_label = None
        self.create_root()
        self.start_butt = self.create_start_butt()
        self.quit_butt = self.create_quit_butt()
        self.exists = True

    def create_root(self):
        self.root.geometry('500x500')
        self.root.iconbitmap(ICON)
        self.root.title(TITLE)
        image = tk.PhotoImage(file=BACKGROUND_IMAGE)
        self.background_label = tk.Label(self.root, image=image)
        self.background_label.image = image
        self.background_label.pack()

    def create_start_butt(self):
        butt = tk.Button(self.root, width=10, height=1, bg="pink",
                         text="Start Game!", font=('calibri light', 18, 'bold'), command=self.start_butt_command)
        butt.place(in_=self.root, anchor='c', relx=.5, rely=.80)
        return butt

    def start_butt_command(self):
        self.exists = False
        self.root.destroy()

    def create_quit_butt(self):
        butt = tk.Button(self.root, width=8, height=1, bg="pink",
                         text="QUIT", font=('calibri light', 8, 'bold'))
        butt.place(in_=self.root, anchor='c', relx=.5, rely=.90)
        return butt


def create_word_list(filename):
    f = open(filename, "r")
    legal_words = [line.strip("\n") for line in f]
    return legal_words


def create_random_letters():
    random_letters = random.randomize_board()
    return random_letters


def run_game():
    start_page = StartPage()
    start_page.root.mainloop()
    if not start_page.exists:
        correct_words = create_word_list('boggle_dict.txt')
        cur_letters = create_random_letters()
        board_game = board.Board(cur_letters)
        my_timer = game.Timer(board_game.root)
        cur_game = game.Game(board_game, cur_letters, my_timer, correct_words)
        cur_game.create_butt_locations()
        cur_game.create_bogg_butt_commands()
        cur_game.create_check_button_command()
        cur_game.board.root.resizable(width=False, height=False)
        cur_game.board.root.mainloop()

if __name__ == '__main__':
    run_game()