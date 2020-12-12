import tkinter
from tkinter import ttk

class MainGUI:
    def __init__(self):
        self.m = tkinter.Tk() # where self.m is the name of the main window object
        self.m.title('Player Queue Bot')

        self.id_label = tkinter.Label(self.m, text="Room ID")
        self.id_label.grid(row=1)

        self.id_box = tkinter.Entry(self.m)
        self.id_box.grid(row=1, column=1)

        self.pass_label = tkinter.Label(self.m, text="Room Password")
        self.pass_label.grid(row=2)

        self.pass_box = tkinter.Entry(self.m)
        self.pass_box.grid(row=2, column=1)

        self.next_player_button = tkinter.Button(self.m, text='Next Player')
        self.next_player_button.grid(row=3, columnspan=2)

        self.top_players_button = tkinter.Button(self.m, text='Show Top Players')
        self.top_players_button.grid(row=4, columnspan=2)

        self.current_player_label = tkinter.Label(self.m, text="Current player:")
        self.current_player_label.config(text="Current player:")
        self.current_player_label.grid(row=5, columnspan=2)

        self.exit_button = tkinter.Button(self.m, text='Save and Exit')
        self.exit_button.grid(row=6, columnspan=2)