from queue import PriorityQueue


class PlayerQueue:
    def __init__(self, player_dict={}):
        self._q = PriorityQueue()
        self._player_dict = player_dict

    def add_player(self, username):
        if username in self._player_dict:
            times_played = self._player_dict[username]
            #the queue class's internal list is public i guess
            if not (times_played, username) in self._q.queue:
                self._q.put((times_played, username))
            else:
                print('User already in queue!')
        else:
            self._q.put((0, username))
            self._player_dict[username] = 0

    def get_next_player(self):
        if not self._q.empty():
            next_player = self._q.get()[1]
            self._player_dict[next_player] += 1
            return next_player
        else:
            return None

    @property
    def player_dict(self):
        return self._player_dict