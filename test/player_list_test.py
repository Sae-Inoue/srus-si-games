import unittest

from player import Player
from player_list import PlayerList

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Create an instance of playerList class
        self.playerlist = PlayerList()
        self.player = Player(uid="1", name="Sae")

    def test_is_empty(self):
        self.assertTrue(self.playerlist.is_empty)

    #def test_insert_head(self):
        #self.assertEqual(self.playerlist.insert_head(self.player), )

if __name__ == '__main__':
    unittest.main()