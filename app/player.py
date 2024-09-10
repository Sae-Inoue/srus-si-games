from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class Player:
    def __init__(self, uid: str, name: str) -> None:
        '''
        :param uid: Unique id of the player
        :param name: name of the player
        '''
        self._uid = uid
        self._name = name
        self.__hashed_password = None

    @property
    def uid(self) -> str:
        '''
        :return: Unique id of the player
        '''
        return self._uid

    @property
    def name(self) -> str:
        '''
        :return: name of the player
        '''
        return self._name

    def __str__(self):
        '''
        :return: String representation of the player
        '''
        return f"id:{self._uid} ,name:{self._name}"


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
        :param password: Plaintext password to be hashed
        :return: True if the provided password matches the hashed, otherwise False
        '''
        ph = PasswordHasher()
        try:
            return ph.verify(self.__hashed_password, password)
        except VerifyMismatchError:
            return False



def main():
    player = Player("1", "Sae")
    print(str(player))


if __name__ == "__main__":
    main()