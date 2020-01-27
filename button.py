import tkinter as tk


class Boggbutt:
    """
    this class creates object to be used as buttons with the tkinter functions,
    with attributes useful to follow which buttons were pressed and
     their name etc.
    """

    def __init__(self, name, letter, button, pressed=False, location=None):
        """
        creates a boggbutt object
        :param name: the name of the button
        :param letter: what letter is on the button
        :param button: a tkinter button connected to this object
        :param pressed: bool, if the button was pressed
        :param location: the button coordinate
        """
        self.__name = name
        self.letter = letter
        self.location = location
        self.button = button
        self.is_pressed = pressed

    def get_name(self):
        """
        returns the name of a boggbutt object
        :return:
        """
        return self.__name
