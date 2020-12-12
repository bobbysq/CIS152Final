from player_queue import PlayerQueue
import gui
import json
from os import path
import configparser
import twitch
import os
import tkinter
import tkinter.messagebox

config = configparser.ConfigParser()
config.read('config_real.ini')

CLIENT_ID = config['DEFAULT']['ClientID']
CLIENT_SECRET = config['DEFAULT']['ClientSecret']
OAUTH = config['DEFAULT']['OAuth']
CHANNEL = config['DEFAULT']['Channel']


def handle_message(q, message: twitch.chat.Message) -> None:
    #print(message.sender + ': ' + message.text)

    if message.text.startswith('!hello'):
        message.chat.send('Hello world!')

    if message.text.startswith('!join'):
        q.add_player(message.sender)
        message.chat.send(message.sender + ', you are now in the queue')


def exit_program(q, chat):
    with open('players.json', 'w') as f:
        json.dump(q.player_dict, f)

    chat.dispose()  # Unsubscribe the message handler
    del chat

    os._exit(0)


def next_player(q, chat, player_label, room_id, room_pass):
    next_player = q.get_next_player()
    if next_player:
        if room_pass == '':
            chat.send('@' + next_player + ', The room ID is: ' + room_id.get())
        else:
            chat.send('@' + next_player + ', The room ID is: ' +
                      room_id.get() + ' and the password is: ' + room_pass.get())
        player_label.config(text='Current player: ' + next_player)
    else:
        player_label.config(text='No one in queue!')


def show_top_players(player_arr):
    box_str = ''
    for player in player_arr:
        box_str = box_str + player[0] + ': ' + str(player[1]) + '\n'
    tkinter.messagebox.showinfo(title='Top Players', message=box_str)


if __name__ == "__main__":
    main_gui = gui.MainGUI()

    if path.exists('players.json'):
        with open('players.json', 'r') as f:
            player_data = json.load(f)
    else:
        f = open('players.json', 'w')  # create file if it doesn't exist
        f.close()
        player_data = {}

    room_id = tkinter.StringVar()
    room_pass = tkinter.StringVar()

    # room_id = input('Room ID: ')
    # room_pass = input('Password (optional): ')

    q = PlayerQueue(player_data)
    chat = twitch.Chat(channel='#' + CHANNEL,
                       nickname='PlayerQueueBot',
                       oauth=OAUTH,
                       helix=twitch.Helix(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, use_cache=True))

    def handler(message): return handle_message(q, message)
    chat.subscribe(handler)

    # Configure button commands
    main_gui.next_player_button.config(command=lambda: next_player(q, chat, main_gui.current_player_label, room_id, room_pass))
    main_gui.top_players_button.config(command=lambda: show_top_players(q.get_top_players()))
    main_gui.exit_button.config(command=lambda: exit_program(q, chat))
    main_gui.m.protocol('WM_DELETE_WINDOW', lambda: exit_program(q, chat))  # reconfigure 'X' button

    main_gui.id_box.config(textvariable=room_id)
    main_gui.pass_box.config(textvariable=room_pass)

    main_gui.m.mainloop()
