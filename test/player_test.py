import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        '''
        Setup variables for player.Creates instances of Player objects to be used in the tests.
        '''
        # Create an instance of player class
        self.player = Player(uid="1", name="Sae", score=20)
        self.player2 = Player(uid="2", name="John", score=25)
        self.player3 = Player(uid="3", name="Alice", score=20)

    def test_initialization(self):
        '''
        Tests whether the player object is initialized
        '''
        self.assertEqual(self.player.uid, "1")
        self.assertEqual(self.player.name, "Sae")

    def test_property_uid(self):
        '''
        Tests whether the player object is initialized properly and its uid is correct
        '''
        self.assertEqual(self.player.uid, "1")

    def test_property_name(self):
        '''
        Tests whether the player object is initialized properly and its name is correct
        '''
        self.assertEqual(self.player.name, "Sae")

    def test_str(self):
        '''
        Tests whether the player object is printed properly and its uid is correct
        :return:
        '''
        self.assertEqual(str(self.player),"id:1 ,name:Sae, score:20")

    def test_add_and_verify_password(self):
        '''
        Tests whether the password object is added to the player object
        '''
        self.player.add_password("password1")
        self.assertTrue(self.player.verify_password("password1"))

    def test_add_and_verify_wrong_password(self):
        '''
        Tests whether the passsword object is verified correctly
        :return:
        '''
        self.player.add_password("password1")
        self.assertFalse(self.player.verify_password("password2"))

    def test_eq(self):
        '''
        Tests whether the player score is equal to the player score
        :return:
        '''
        self.assertTrue(self.player == self.player3)
        self.assertFalse(self.player == self.player2)

    def test_lt(self):
        '''
        Tests whether the player score is less than the player score
        :return:
        '''
        self.assertTrue(self.player < self.player2)
        self.assertFalse(self.player2 < self.player)

    def test_le(self):
        '''
        Tests whether the player score is less than or equal to the player score
        :return:
        '''
        self.assertTrue(self.player <= self.player3)
        self.assertTrue(self.player <= self.player2)
        self.assertFalse(self.player2 <= self.player)

    def test_gt(self):
        '''
        Tests whether the player score is greater than the player score
        :return:
        '''
        self.assertTrue(self.player2 > self.player)
        self.assertFalse(self.player > self.player2)

    def test_ge(self):
        '''
        Tests whether the player score is greater than or equal to the players score
        :return:
        '''
        self.assertTrue(self.player >= self.player3)
        self.assertTrue(self.player2 >= self.player)
        self.assertFalse(self.player >= self.player2)

    def test_sort_descending(self):
        scores = [self.player.score, self.player2.score, self.player3.score]
        sorted_players = Player.sort_descending(Player, scores)
        self.assertEqual(sorted_players[0], self.player2.score)  # Highest score first
        self.assertEqual(sorted_players[1], self.player.score)
        self.assertEqual(sorted_players[2], self.player3.score)


if __name__ == '__main__':
    unittest.main()