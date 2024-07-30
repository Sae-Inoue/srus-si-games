import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Create an instance of player class
        self.player = Player(uid="1", name="Sae")

    def test_initialization(self):
        self.assertEqual(self.player.uid, "1")
        self.assertEqual(self.player.name, "Sae")

    def test_property_uid(self):
        self.assertEqual(self.player.uid, "1")

    def test_property_name(self):
        self.assertEqual(self.player.name, "Sae")

    def test_str(self):
        self.assertEqual(str(self.player),"Player id:1 , Player name:Sae")


if __name__ == '__main__':
    unittest.main()