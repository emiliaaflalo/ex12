import tkinter as tk

class Boggbutt:

    def __init__(self, name, letter, button, location=None):
        self.__name = name
        self.letter = letter
        self.location = location
        self.button = button

    def get_name(self):
        return self.__name