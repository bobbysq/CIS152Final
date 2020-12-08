from player_queue import PlayerQueue
import json
from os import path
import configparser
import twitch
import os

config = configparser.ConfigParser()
config.read('config_real.ini')

CLIENT_ID = config['DEFAULT']['ClientID']
CLIENT_SECRET = config['DEFAULT']['ClientSecret']
OAUTH = config['DEFAULT']['OAuth']
CHANNEL = config['DEFAULT']['Channel']


def handle_message(q, message: twitch.chat.Message) -> None:
    print(message.sender + ': ' + message.text)

    if message.text.startswith('!hello'):
        message.chat.send('Hello world!')

    if message.text.startswith('!join'):
        q.add_player(message.sender)
        message.chat.send(message.sender + ', you are now in the queue')

    # if message.text.startswith('!next'):
    #     #message.chat.send('/w ' + message.sender + ' the code is: [CODE HERE]')
    #     if message.sender.lower() == CHANNEL.lower():
    #         message.chat.send('Hello, ' + q.get_next_player() + '. The code is: [CODE HERE]')


def show_menu():
    choice = 0
    while choice < 1 or choice > 3:
        print('PlayerQueueBot menu:\n\
\n\
1. Go to next player\n\
2. Show top players\n\
3. Quit')
        choice = int(input('Please enter a selection: '))
        if choice < 1 or choice > 3:
            print('Invalid choice.')
    return choice


if __name__ == "__main__":
    if path.exists('players.json'):
        with open('players.json', 'r') as f:
            player_data = json.load(f)
    else:
        f = open('players.json', 'w')  # create file if it doesn't exist
        f.close()
        player_data = {}

    q = PlayerQueue(player_data)
    chat = twitch.Chat(channel='#' + CHANNEL,
                       nickname='PlayerQueueBot',
                       oauth=OAUTH,
                       helix=twitch.Helix(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, use_cache=True))

    handler = lambda message: handle_message(q, message)
    chat.subscribe(handler)

    choice = 0
    while choice != 3:
        choice = show_menu()
        if choice == 1:
            next_player = q.get_next_player()
            if next_player:
                pass
                chat.send('@' + next_player + ', The code is: [CODE HERE]')
            else:
                print('No one in queue!')

    with open('players.json', 'w') as f:
        json.dump(q.player_dict, f)

    chat.dispose()  # Unsubscribe the message handler
    del chat

    os._exit(0)