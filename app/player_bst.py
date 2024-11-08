from player import Player
from player_bnode import PlayerBNode
class PlayerBST():
    def __init__(self):
        '''
        Initialize the root of player BST
        '''
        self._root = None

    @property
    def root(self):
        '''
        Set the root of the player BST
        :return: Root of the search
        '''
        return self._root

    def insert(self, player: Player):
        '''
        Insert PlayerNode to BST by using name as keys
        :param player: Player to be inserted into the BST
        '''
        new_node = PlayerBNode(player)
        new_node.key = player.name
        new_node.value = player

        if self._root is None:
            print(f"This is root player: {new_node.key}")
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
        :param name: plyer name
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

    def traverse(self):
        '''
        Traverse the current node and return its children
        :return:
        '''
        nodes = []
        print("In-order traversal:")
        self.inorder_helper(self._root, nodes)
        return nodes

    def inorder_helper(self, node, nodes):
        '''
        Helper function to traverse the tree in order and return a list of PlayerBNodes
        :param node:
        :param nodes:
        :return:
        '''
        if node is not None:
            self.inorder_helper(node.left, nodes)
            nodes.append(node)
            print(str(node.player))
            self.inorder_helper(node.right, nodes)

    def balanced_tree(self, nodes, start, end):
        '''
        Balanced tree
        :param nodes: a list of PlayerBNodes
        :param start: at the start of the tree
        :param end: at the end of the tree
        :return:
        '''
        if start > end:
            return None

        mid = (start + end) // 2
        self._root = PlayerBNode(nodes[mid])

        self._root.left = self.balanced_tree(nodes, start, mid - 1)
        self._root.right = self.balanced_tree(nodes, mid + 1, end)
        return self._root

    def balance_bst(self):
        '''
        Balanced tree traversal using binary search tree
        :return: balanced tree function
        '''
        nodes = []
        self.inorder_helper(self._root, nodes)
        return self.balanced_tree(nodes, 0, len(nodes) - 1)




def main():
    tree = PlayerBST()

    player = Player("1", "Sae", 20)
    player2 = Player("2", "John", 15)
    player3 = Player("3", "Alice", 49)
    player4 = Player("4", "Levi", 34)
    player5 = Player("5", "Josh", 34)
    player6 = Player("6", "Karen", 34)
    player7 = Player("7", "Ben ", 34)


    tree.insert(player)
    tree.insert(player2)
    tree.insert(player3)
    tree.insert(player4)
    tree.insert(player5)
    tree.insert(player6)
    tree.insert(player7)

    tree.search("Alice")
    tree.search("Karen")

    tree.traverse()

    print("\n")
    print("This is balanced tree:")
    tree.balance_bst()



if __name__ == '__main__':
    main()

