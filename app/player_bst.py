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
        '''
        Insert PlayerNode to BST by using name as keys
        '''
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

    def search(self, name):
        '''
        Search player by name
        :param name plyer name
        :return current: searching node
        '''
        return self.prepare_search(self._root, name)

    def prepare_search(self, current, name):
        '''
        Prepare Search method to use search function
        :param: current: current node
                name: player name
        :return: if searching name matches current node player name return it
                 otherwise return none
        '''
        while current.player.name != name:
            if name < current.player.name:
                current = current.left
            elif name > current.player.name:
                current = current.right

            if current is None:
                print(f"{name} is not found!")
                return None

        print(f"{name} is found!!")
        return current.player


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


    tree.search("Alice")
    tree.search("Karen")



if __name__ == '__main__':
    main()

