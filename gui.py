"""

"""
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from tkinter import ttk

m = tkinter.Tk() # where m is the name of the main window object
m.title('Player Queue Bot')

id_label = tkinter.Label(m, text="Room ID")
id_label.grid(row=1)

id_box = tkinter.Entry(m)
id_box.grid(row=1, column=1)

pass_label = tkinter.Label(m, text="Room Password")
pass_label.grid(row=2)

pass_box = tkinter.Entry(m)
pass_box.grid(row=2, column=1)

next_player_button = tkinter.Button(m, text='Next Player')
next_player_button.grid(row=3, columnspan=2)

top_players_button = tkinter.Button(m, text='Show Top Players')
top_players_button.grid(row=4, columnspan=2)

current_player_label = tkinter.Label(m, text="Current player:")
current_player_label.config(text="Current player:")
current_player_label.grid(row=5, columnspan=2)

exit_button = tkinter.Button(m, text='Exit', command=m.destroy)
exit_button.grid(row=6, columnspan=2)

m.mainloop()