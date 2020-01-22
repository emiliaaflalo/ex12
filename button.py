import tkinter as tk


class Boggbutt:

    def __init__(self, name, letter, button, pressed=False, location=None):
        self.__name = name
        self.letter = letter
        self.location = location
        self.button = button
        self.is_pressed = pressed

    def get_name(self):
        return self.__name
