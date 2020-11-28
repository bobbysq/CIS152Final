from player_queue import PlayerQueue
import json
from os import path
import configparser
import twitch

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

    if message.text.startswith('!next'):
        #message.chat.send('/w ' + message.sender + ' the code is: [CODE HERE]')
        if message.sender.lower() == CHANNEL.lower():
            message.chat.send('Hello, ' + q.get_next_player() + '. The code is: [CODE HERE]')

if __name__ == "__main__":
    if path.exists('players.json'):
        with open('players.json', 'r') as f:
            player_data = json.load(f)
    else:
        f = open('players.json', 'w') #create file if it doesn't exist
        f.close()
        player_data = {}

    q = PlayerQueue(player_data)
    chat = twitch.Chat(channel='#' + CHANNEL,
                       nickname='PlayerQueueBot',
                       oauth=OAUTH,
                       helix=twitch.Helix(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, use_cache=True))

    chat.subscribe(lambda message: handle_message(q, message))

    json_out = json.dumps(q.player_dict)

    with open('players.json', 'w') as f:
        json.dump(q.player_dict, f)

    print(json_out)