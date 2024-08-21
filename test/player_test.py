import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        '''
        Setup variables for player.Creates instances of Player objects to be used in the tests.
        '''
        # Create an instance of player class
        self.player = Player(uid="1", name="Sae")

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
        self.assertEqual(str(self.player),"id:1 ,name:Sae")

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


if __name__ == '__main__':
    unittest.main()