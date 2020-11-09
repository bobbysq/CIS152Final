from queue import PriorityQueue

class PlayerQueue:
    def __init__(self, player_dict = {}):
        self._q = PriorityQueue()
        self._player_dict = player_dict

    def add_player(self, username):
        if username in self._player_dict:
            times_played = self._player_dict[username]
            self._q.put(username, times_played)
        else:
            self._q.put(username, 0)
            self._player_dict[username] = 0

    def get_next_player(self):
        pass