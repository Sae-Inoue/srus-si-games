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
            print("This is empty")
        else:
            new_node.next = self._head
            new_node.previous = new_node
            self._head = new_node
            print("this is not empty")

    def __str__(self):
        node = []
        current = self._head
        node.append(str(current))


def main():
    player = Player("1", "Sae")
    #player2 = Player("2", "John")
    plnode = PlayerNode(player)
    pl1 = PlayerList()
    list = pl1.insert_head(player)
    #list = list.insert_head(player2)

    print(str(player))
    print(str(plnode))
    print(list)
    #print(list2)


if __name__ == '__main__':
    main()

