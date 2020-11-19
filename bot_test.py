import configparser
import twitch

config = configparser.ConfigParser()
config.read('config.ini')

CLIENT_ID = config['DEFAULT']['ClientID']
CLIENT_SECRET = config['DEFAULT']['ClientSecret']
OAUTH = config['DEFAULT']['OAuth']

def handle_message(message: twitch.chat.Message) -> None:
    if message.text.startswith('!hello'):
        message.chat.send('Hello world!')


def main():
    chat = twitch.Chat(channel='#bobbysq',
                       nickname='PlayerQueueBot',
                       oauth=OAUTH,
                       helix=twitch.Helix(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, use_cache=True))

    chat.subscribe(handle_message)


if __name__ == '__main__':
    main()