from player import Player
class PlayerNode():
    def __init__(self, player: Player) -> None:
        '''
        :param player: Player object that represents the player who played the game
        '''
        self._player = player
        self._previous = None
        self._next = None


    @property
    def player(self) -> Player:
        '''
        :return: Player object that represents the player who played the game
        '''
        return self._player

    # This sets the property and setter for previous
    @property
    def previous(self) -> Player:
        '''
        :return: The previous PlayerNode in the list
        '''
        return self._previous

    # This sets the property and setter for next
    @property
    def next(self) -> Player:
        '''
        :return: The next PlayerNode in the list
        '''
        return self._next

    @previous.setter
    def previous(self, previous_node: Player):
        '''
        :param previous_node: The PlayerNode to be set as the previous node
        '''
        self._previous = previous_node

    @next.setter
    def next(self, next_node: Player):
        '''
        :param next_node: The PlayerNode to be set as the next node
        '''
        self._next = next_node

# Creating a new variable called key
    @property
    def key(self):
        '''
        Get the uid of the player
        :return: The id of the player
        '''
        return self._player.uid

    def __str__(self) -> str:
        '''
        :return: String representation of the player
        '''
        return f"PlayerNode({self._player}, Previous={self._previous}, Next={self._next})"

