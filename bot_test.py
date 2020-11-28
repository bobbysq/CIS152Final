import configparser
import twitch

config = configparser.ConfigParser()
config.read('config_real.ini')

CLIENT_ID = config['DEFAULT']['ClientID']
CLIENT_SECRET = config['DEFAULT']['ClientSecret']
OAUTH = config['DEFAULT']['OAuth']
CHANNEL = config['DEFAULT']['Channel']

def handle_message(message: twitch.chat.Message) -> None:
    print(message.sender + ': ' + message.text)

    if message.text.startswith('!hello'):
        message.chat.send('Hello world!')

    if message.text.startswith('!join'):
        #message.chat.send('/w ' + message.sender + ' the code is: [CODE HERE]')
        message.chat.send('Hello, ' + message.sender + '. The code is: [CODE HERE]')


def main():
    chat = twitch.Chat(channel='#bobbysq',
                       nickname='PlayerQueueBot',
                       oauth=OAUTH,
                       helix=twitch.Helix(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, use_cache=True))

    chat.subscribe(handle_message)


if __name__ == '__main__':
    main()