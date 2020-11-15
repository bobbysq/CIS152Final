from player_queue import PlayerQueue
import json
from os import path

if __name__ == "__main__":
    if path.exists('players.json'):
        with open('players.json', 'r') as f:
            player_data = json.load(f)
    else:
        f = open('players.json', 'w') #create file if it doesn't exist
        f.close()
        player_data = {}

    q = PlayerQueue(player_data)

    q.add_player('test1')
    q.add_player('test1')
    q.add_player('test2')
    q.add_player('test3')

    print(q.get_next_player())
    print(q.get_next_player())
    print(q.get_next_player())

    q.add_player('test4')
    q.add_player('test2')
    q.add_player('test1')

    print(q.get_next_player())
    print(q.get_next_player())
    print(q.get_next_player())

    json_out = json.dumps(q.player_dict)

    with open('players.json', 'w') as f:
        json.dump(q.player_dict, f)

    print(json_out)