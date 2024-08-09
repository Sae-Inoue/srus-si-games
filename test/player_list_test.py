import unittest

from player import Player
from player_list import PlayerList

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Create an instance of playerList class
        self.playerlist = PlayerList()
        self.player = Player(uid="1", name="Sae")
        self.player2 = Player(uid="2", name="John")

    def test_is_empty(self):
        self.assertTrue(self.playerlist.is_empty)

    def test_insert_head(self):
        self.playerlist.insert_head(self.player)
        self.playerlist.insert_head(self.player2)
        self.assertEqual(self.playerlist._head.player, self.player2)

    def test_insert_tail(self):
        self.playerlist.insert_tail(self.player)
        self.playerlist.insert_tail(self.player2)
        self.assertEqual(self.playerlist._tail.player, self.player2)

    def test_delete_head(self):
        self.playerlist.insert_tail(self.player)
        self.playerlist.insert_tail(self.player2)
        self.playerlist.delete_head()
        self.assertEqual(self.playerlist._tail.player, self.player2)

    def test_delete_tail(self):
        self.playerlist.insert_tail(self.player)
        self.playerlist.insert_tail(self.player2)
        self.playerlist.delete_tail()
        self.assertEqual(self.playerlist._tail.player, self.player)

    def test_str(self):
        self.playerlist.insert_head(self.player)
        self.playerlist.insert_head(self.player2)
        self.assertEqual(str(self.playerlist), "Player List: John, Sae")




if __name__ == '__main__':
    unittest.main()