import tkinter as tk
import board
import game
import boggle_board_randomizer as random

BOGGLE_SIDE = 4
TITLE = 'BOGGLENOVELA'
START_IMAGE = 'opening_screen.gif'
ICON = 'cat_icon.ico'


class StartPage:
    """
    this class creates an object that is used as an opening page for the
     boggle game
    """
    def __init__(self):
        """
        creates a startpage object to be used as an starting page for the game
        using tkinter functions.
        """
        self.root = tk.Tk()
        self.background_label = None
        self.create_root()
        self.start_butt = self.create_start_butt()
        self.quit_butt = self.create_quit_butt()
        self.exists = True

    def create_root(self):
        """
        this function creates a root (parent) for the start page, using tkinter
        functions
        :return:
        """
        self.root.geometry('500x500')
        # self.root.iconbitmap(ICON)
        self.root.title(TITLE)
        image = tk.PhotoImage(file=START_IMAGE)
        self.background_label = tk.Label(self.root, image=image)
        self.background_label.image = image
        self.background_label.pack()

    def create_start_butt(self):
        """
        this function creates a button on teh start page that calls
         the start_butt function
        :return:
        """
        butt = tk.Button(self.root, width=10, height=1, bg="pink",
                         text="Start Game!",
                         font=('calibri light', 18, 'bold'),
                         command=self.start_butt_command)
        butt.place(in_=self.root, anchor='c', relx=.5, rely=.65)
        return butt

    def start_butt_command(self):
        """
        this function closes the current page (start page) so the main game
        page will open after
        :return:
        """
        self.exists = False
        self.root.destroy()

    def create_quit_butt(self):
        """
        this function creates a button that closes the page if clicked
        :return:
        """
        butt = tk.Button(self.root, width=8, height=1, bg="pink",
                         text="QUIT", font=('calibri light', 8, 'bold'),
                         command=self.root.destroy)
        butt.place(in_=self.root, anchor='c', relx=.5, rely=.75)
        return butt


def create_word_list(filename):
    """
    this function creates a list of legal words to use in the game
    :param filename: the name of the fil containing the words
    :return:
    """
    f = open(filename, "r")
    legal_words = [line.strip("\r\n") for line in f]
    return legal_words


def create_random_letters():
    """
    this function creates a 2d list containing random letters
    :return:
    """
    random_letters = random.randomize_board()
    return random_letters


def run_game():
    """
    this function is the main function for running the game. it calls in order
    the main functions and creates objects to be used in the game.
    in general: it opens the start page, when "start game" is clicked, closes
     the start page and creates the game page with all of its objects.
    :return:
    """
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
