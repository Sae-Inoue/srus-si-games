from player_node import PlayerNode
from player import Player

class PlayerList():
    def __init__(self) -> None:
        self._head = None

    # Create a method that allows you to insert a new node at the head of the list.
    def is_empty(self):
        return self._head is None

    def insert_head(self, player: Player):
        #creating a new node
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node

        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node


    def __str__(self)->str:
        node = []
        current = self._head
        while current is not None:
            node.append(str(current.player.name))
            current = current.next
        return f"Player List: {', '.join(node)}"



# def main():
#     player = Player("1", "Sae")
#     player2 = Player("2", "John")
#     player3 = Player("3", "Josh")
#     plnode = PlayerNode(player)
#     pl1 = PlayerList()
#     pl1.insert_head(player)
#     pl1.insert_head(player2)
#     pl1.insert_head(player3)
#
#
#     print(str(player))
#     print(str(plnode))
#     print(pl1)
#
# if __name__ == '__main__':
#     main()

