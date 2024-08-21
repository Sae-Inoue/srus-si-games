from argon2 import PasswordHasher

class Player:
    def __init__(self, uid: str, name: str) -> None:
        '''
        :param uid: Unique id of the player
        :param name: name of the player
        '''
        self.__uid = uid
        self.__name = name
        self.__hashed_password = None

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


    def add_password(self, password:str):
        '''
        Hashed password of the player and store it in a private instance variable
        :param password: Plaintext password to be hashed
        '''
        ph = PasswordHasher()
        self.__hashed_password = ph.hash(password)

    def verify_password(self, password:str):
        '''
        Checks if the provided password matches the hashed password
        :param password:
        :return:
        '''
        ph = PasswordHasher()
        if(ph.verify(self.__hashed_password, password)):
            return True
        return False




