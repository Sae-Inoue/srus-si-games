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
        self.assertEqual(self.playerlist, )

    def test_str(self):
        self.assertEqual(str(self.playerlist.__str__()), "Player id:1 , Player name:Sae")

if __name__ == '__main__':
    unittest.main()