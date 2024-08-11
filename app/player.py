class Player:
    def __init__(self, uid: str, name: str) -> None:
        '''
        :param uid: Unique id of the player
        :param name: name of the player
        '''
        self.__uid = uid
        self.__name = name

    @property
    def uid(self) -> str:
        '''
        :return: Unique id of the player
        '''
        return self.__uid

    @property
    def name(self) -> str:
        '''
        :return: name of the player
        '''
        return self.__name

    def __str__(self):
        '''
        :return: String representation of the player
        '''
        return f"id:{self.__uid} ,name:{self.__name}"

