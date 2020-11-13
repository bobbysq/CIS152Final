from player_queue import PlayerQueue

if __name__ == "__main__":
    q = PlayerQueue()

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