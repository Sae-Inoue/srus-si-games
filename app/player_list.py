from player_node import PlayerNode
from player import Player

class PlayerList():
    '''
    Initializes an empty player list with head and tail pointers
    '''
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    @property
    def head(self) -> str:
        '''
        :return: head pointer
        '''
        return self._head

    @property
    def tail(self) -> str:
        '''
        :return: tail pointer
        '''
        return self._tail

    def is_empty(self):
        '''
        Checks if the player list is empty
        :return: True if the list is empty, otherwise False.
        '''
        return self._head is None and self._tail is None

    def insert_head(self, player: Player):
        '''
        Adds a player to the head of the player list
        :param player: The player to be added to the head of the list
        '''
        #creating a new node
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node

        else:
            new_node.next = self._head
            self._head.previous = new_node
            self._head = new_node

    def insert_tail(self, player: Player):
        '''
        Adds a player to the tail of the player list
        :param player: The player to be added to the tail of the list
        '''
        #creating a new node
        new_node = PlayerNode(player)

        if self.is_empty():
            self._head = new_node
            self._tail = new_node

        else:
            new_node.previous = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def delete_head(self):
        '''
        Deletes the node from the head of the player list
        '''
        if self._head == self._tail:
            self._head = None
            self._tail = None

        else:
            self._head = self._head.next
            self._head.previous = None

    def delete_tail(self):
        '''
          Deletes the node from the tail of the player list
        '''
        if self._head == self._tail:
            self._head = None
            self._tail = None

        else:
            self._tail = self._tail.previous
            self._tail.next = None

    def delete_item_by_key(self, id: str):
        '''
        Deletes the node from the player list that matches the provided id
        :param id: This is unique identifier for the player
        '''
        current = self._head

        while current is not None:
            if current.key == id:
                if current == self._head:
                    self.delete_head()
                    return

                elif current == self._tail:
                    self.delete_tail()
                    return

                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous

            current = current.next

    def display(self, forward=True):
        '''
        Displays the player list forward or backward
        :param forward:  If it's True, displays the list from head to tail. if it's False, from tail to head.
        '''

        if forward:
            current = self._head
            while current is not None:
                print(current)
                current = current.next
        else:
            current = self._tail
            while current is not None:
                print(current)
                current = current.previous



    def __str__(self)->str:
        '''
        Returns a string representation of the player list
        :return: Displays the players in list
        '''
        node = []
        current = self._head
        while current is not None:
            node.append(str(current.player.name))
            current = current.next
        return f"Player List: {', '.join(node)}"


def main():
    player = Player("1", "Sae",20)
    player2 = Player("2", "John",30)
    player3 = Player("3", "Josh",10)
    plnode = PlayerNode(player)
    plnode2 = PlayerNode(player2)
    plnode3 = PlayerNode(player3)

    pl1 = PlayerList()

    print(f'this is  {pl1._tail}')
    print(f'this is  {pl1._head}')
    pl1.insert_tail(player)
    print(f'This is tail {pl1._tail.player}')
    print(f'this is head {pl1._head.player}')
    pl1.insert_tail(player2)
    print(f'This is tail {pl1._tail.player}')
    print(f'this is head {pl1._head.player}')
    pl1.insert_tail(player3)
    print(f'This is tail {pl1._tail.player}')
    print(f'this is head {pl1._head.player}')
    print(str(pl1))

    print("This is forward of the list:")
    pl1.display(True)
    print("This is backward of the list:")
    pl1.display(False)

if __name__ == '__main__':
    main()