class PlayerBNode():
    def __init__(self, player):
        '''
        Initialise the player object
        :param player:
        '''
        self._player = player
        self._left = None
        self._right = None


    @property
    def player(self):
        '''
        :return: player
        '''
        return self._player

    @player.setter
    def player(self, value):
        '''
        Set the player object
        :param value:
        :return:
        '''
        self._player = value

    @property
    def left(self):
        '''
        Get the left of the BST node
        :return: left
        '''
        return self._left

    @left.setter
    def left(self, value):
        '''
        Set the left of the BST node
        :param value:
        :return:
        '''
        self._left = value

    @property
    def right(self):
        '''
        Get the right of the BST node
        :return:
        '''
        return self._right

    @right.setter
    def right(self, value):
        '''
        Set the right of the BST node
        :param value:
        :return:
        '''
        self._right = value
