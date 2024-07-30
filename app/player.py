class Player:
    def __init__(self, uid: str, name: str) -> None:
        self.__uid = uid
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @property
    def name(self) -> str:
        return self.__name

    def __str__(self):
        return f"Player id:{self.__uid} , Player name:{self.__name}"

