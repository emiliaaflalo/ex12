import tkinter as tk
import game

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
                         text="Start Game!", font=('calibri light', 18, 'bold'))
        butt.place(in_=self.root, anchor='c', relx=.5, rely=.80)
        return butt

    def create_quit_butt(self):
        butt = tk.Button(self.root, width=8, height=1, bg="pink",
                         text="QUIT", font=('calibri light', 8, 'bold'))
        butt.place(in_=self.root, anchor='c', relx=.5, rely=.90)
        return butt



if __name__ == '__main__':
    page = StartPage()
    page.root.mainloop()