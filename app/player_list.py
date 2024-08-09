from player_node import PlayerNode
from player import Player

class PlayerList():
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    # Create a method that allows you to insert a new node at the head of the list.
    def is_empty(self):
        return self._head is None and self._tail is None

    def insert_head(self, player: Player):
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
        if self._head == self._tail:
            self._head = None
            self._tail = None

        else:
            self._head = self._head.next
            self._head.previous = None

    def delete_tail(self):
        if self._head == self._tail:
            self._head = None
            self._tail = None

        else:
            self._tail = self._tail.previous
            self._tail.next = None

    def delete_item_by_key(self, id: str):
        current = self._head

        while current is not None:
            if current.player.uid == id:
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
        current = self._head
        nodes = []

        while current is not None:
            nodes.append(current.player.name)
            current = current.next

        if forward == False:
            nodes.reverse()

        print(nodes)



    def __str__(self)->str:
        node = []
        current = self._head
        while current is not None:
            node.append(str(current.player.name))
            current = current.next
        return f"Player List: {', '.join(node)}"


