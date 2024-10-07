from player import Player
from player_bnode import PlayerBNode
class PlayerBST():
    def __init__(self):
        self._root = None

    @property
    def root(self):
        '''
        :return: Root of the search
        '''
        return self._root

    def insert(self, player: Player):
        new_node = PlayerBNode(player)
        new_node.key = player.name
        new_node.value = player

        if self._root is None:
            self._root = new_node

        else:
            current_node = self._root
            while True:
                parent = current_node
                if player.name < current_node.player.name:
                    current_node = current_node.left
                    if current_node is None:
                        parent.left = new_node
                        return
                elif player.name > current_node.player.name:
                    current_node = current_node.right
                    if current_node is None:
                        parent.right = new_node
                        return

def main():
    tree = PlayerBST()

    player = Player("1", "Sae", 20)
    player2 = Player("2", "John", 15)
    player3 = Player("3", "Alice", 49)
    player4 = Player("4", "Levi", 34)


    tree.insert(player)
    tree.insert(player2)
    tree.insert(player3)
    tree.insert(player4)



if __name__ == '__main__':
    main()

