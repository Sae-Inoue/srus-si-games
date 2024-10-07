import unittest

from player import Player
from player_bst import PlayerBST

class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        '''
        Sets up the test variables. Creates instances of PlayerList and Player objects to be used in the tests.
        '''
        # Create an instance of playerBST class
        self.bst = PlayerBST()
        self.player = Player(uid="1", name="Sae", score=12)
        self.player2 = Player(uid="2", name="John", score=24)
        self.player3 = Player(uid="3", name="Karen", score=4)
        self.player4 = Player(uid="4", name="Tom", score=50)

    def test_instantiation(self):
        '''Tests the insert method of the PlayerBST class
        :param self:
        :return:
        '''
        self.bst.insert(self.player)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)

        self.assertEqual(self.bst.root.player.name, "Sae")
        self.assertEqual(self.bst.root.left.player.name, "John")
        self.assertEqual(self.bst.root.right.player.name, "Tom")
        self.assertEqual(self.bst.root.left.right.player.name, "Karen")

if __name__ == "__main__":
    unittest.main()
