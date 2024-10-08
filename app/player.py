from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class Player:
    def __init__(self, uid: str, name: str, score: int) -> None:
        '''
        :param uid: Unique id of the player
        :param name: name of the player
        '''
        self._uid = uid
        self._name = name
        self._hashed_password = None
        self._score = score

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

    @property
    def score(self) -> int:
        '''
        Get the score of the player
        :return: score of the player
        '''
        return self._score

    @score.setter
    def score(self, new_score):
        '''
        Set the score of the player
        :param new_score:
        :return:
        '''
        self._score = new_score

    def __str__(self):
        '''
        :return: String representation of the player
        '''
        return f"id:{self._uid} ,name:{self._name}, score:{self._score}"


    def add_password(self, password:str):
        '''
        Hashed password of the player and store it in a private instance variable
        :param password: Plaintext password to be hashed
        '''
        ph = PasswordHasher()
        self._hashed_password = ph.hash(password)

    def verify_password(self, password:str):
        '''
        Checks if the provided password matches the hashed password
        :param password: Plaintext password to be hashed
        :return: True if the provided password matches the hashed, otherwise False
        '''
        ph = PasswordHasher()
        try:
            return ph.verify(self._hashed_password, password)
        except VerifyMismatchError:
            return False

    def __eq__(self, other):
        '''
        Return true if the score is equal to the other score
        '''
        return self._score == other.score


    def __ge__(self, other):
        '''
        Return true if the score is grater than or equal to the other score
        '''
        return self._score >= other.score

    def __gt__(self, other):
        '''
        Return true if the score is grater than the other score
        :param other:
        :return:
        '''
        return self._score > other.score

    def __le__(self, other):
        '''
        Return true if the score is less than or equal to the other score
        :param other:
        :return:
        '''
        return self._score <= other.score

    def __lt__(self, other):
        '''
        Return true if the score is less than the other score
        :param other:
        :return:
        '''
        return self._score < other.score

    def sort_descending(self, scores):
        '''
        Sort the players by their score in descending order
        :param scores:
        :return: scores
        '''
        n = len(scores)
        for i in range(n):
            sort_list = scores[i]
            j = i-1
            while j >= 0 and scores[j] < sort_list:
                scores[j+1] = scores[j]
                j = j-1
            scores[j+1] = sort_list
        return scores


def main():
    player = Player("1", "Sae", 20)
    player2 = Player("2", "John", 15)
    player3 = Player("3", "Alice", 49)
    player4 = Player("4", "Levi", 34)
    print(str(player))

    scores = [player.score, player2.score, player3.score, player4.score]
    print(f'Unsorted list : {scores}')
    sorted_list = Player.sort_descending(player, scores)
    print(f'Sorted list : {sorted_list}')


if __name__ == "__main__":
    main()