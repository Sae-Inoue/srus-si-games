from player import Player
class PlayerNode():
    def __init__(self, player: Player) -> None:
        self._player = player
        self._previous = None
        self._next = None


    @property
    def player(self) -> Player:
        return self._player

    # This sets the property and setter for previous
    @property
    def previous(self) -> Player:
        return self._previous

    # This sets the property and setter for next
    @property
    def next(self) -> Player:
        return self._next

    @previous.setter
    def previous(self, previous_node: Player):
        self._previous = previous_node

    @next.setter
    def next(self, next_node: Player):
        self._next = next_node

# Creating a new variable called key
    @property
    def key(self):
        return self._player.uid

    def __str__(self) -> str:
        return f"PlayerNode({self._player}, Previous={self._previous}, Next={self._next})"


# def main():
#     player = Player("1", "Sae")
#     plnode = PlayerNode(player)
#     print(str(player))
#     print(str(plnode))
#
#
# if __name__ == "__main__":
#     main()
