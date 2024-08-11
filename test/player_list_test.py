import unittest

from player import Player
from player_list import PlayerList

class TestPlayer(unittest.TestCase):
    def setUp(self):
        '''
        Sets up the test variables. Creates instances of PlayerList and Player objects to be used in the tests.
        '''
        # Create an instance of playerList class
        self.playerlist = PlayerList()
        self.player = Player(uid="1", name="Sae")
        self.player2 = Player(uid="2", name="John")
        self.player3 = Player(uid="3", name="Karen")

    def test_is_empty(self):
        '''
        Tests if the player list is empty
        '''
        self.assertTrue(self.playerlist.is_empty)

    def test_insert_head(self):
        '''
        Tests if insert_head function is working as expected. Checks if a player inserted at the head of the list
        '''
        self.playerlist.insert_head(self.player)
        self.playerlist.insert_head(self.player2)
        self.assertEqual(self.playerlist._head.player, self.player2)

    def test_insert_tail(self):
        '''
        Tests if insert_tail function is working as expected. Checks if a player is added at the tail of the list
        '''
        self.playerlist.insert_tail(self.player)
        self.playerlist.insert_tail(self.player2)
        self.assertEqual(self.playerlist._tail.player, self.player2)

    def test_delete_head(self):
        '''
        Tests if delete_head function is working as expected. Checks if a player removed 
        '''
        self.playerlist.insert_tail(self.player)
        self.playerlist.insert_tail(self.player2)
        self.playerlist.delete_head()
        self.assertEqual(self.playerlist._tail.player, self.player2)

    def test_delete_tail(self):
        '''
        Tests if delete_tail function is working as expected
        '''
        self.playerlist.insert_tail(self.player)
        self.playerlist.insert_tail(self.player2)
        self.playerlist.delete_tail()
        self.assertEqual(self.playerlist._tail.player, self.player)

    def test_delete_item_by_key(self):
        '''
        Tests if delete_item_by_key function is working as expected
        '''
        self.playerlist.insert_tail(self.player)
        self.playerlist.insert_tail(self.player2)
        self.playerlist.insert_tail(self.player3)
        self.playerlist.delete_item_by_key("2")
        self.assertEqual(str(self.playerlist), "Player List: Sae, Karen")

    def test_str(self):
        '''
        Tests if str function is working as expected
        '''
        self.playerlist.insert_head(self.player)
        self.playerlist.insert_head(self.player2)
        self.assertEqual(str(self.playerlist), "Player List: John, Sae")




if __name__ == '__main__':
    unittest.main()