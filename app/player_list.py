from player_node import PlayerNode
from player import Player

class PlayerList():
    def __init__(self) -> None:
        self._head = None

    # Create a method that allows you to insert a new node at the head of the list.
    def is_empty(self):
        return self._head is None

    def insert_head(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
        else:
            new_node.next = self._head
            new_node.previous = new_node
            self._head = new_node


