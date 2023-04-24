import unittest
from descriptors import BasketballPlayer


class TestDescriptor(unittest.TestCase):

    def test_set_with_correct_field(self):
        BasketballPlayer(12, 'PG', 190.9)
        BasketballPlayer(78, 'C', 212.9)
        BasketballPlayer(23, 'SF', 202.9)

    def test_set_with_incorrect_field(self):
        with self.assertRaises(TypeError):
            BasketballPlayer(12.4, 'PG', 190.9)

        with self.assertRaises(ValueError):
            BasketballPlayer(100, 'PG', 190.9)

        with self.assertRaises(ValueError):
            BasketballPlayer(-100, 'PG', 190.9)

        with self.assertRaises(TypeError):
            BasketballPlayer(12, 12, 190.9)

        with self.assertRaises(ValueError):
            BasketballPlayer(100, 'PGG', 190.9)

        with self.assertRaises(TypeError):
            BasketballPlayer(12.4, 'PG', 190)

        with self.assertRaises(ValueError):
            BasketballPlayer(100, 'PG', -190.9)

    def test_str(self):
        number, height, position = 12, 190.9, 'PG'
        player1 = BasketballPlayer(number, position, height)
        self.assertEqual(str(player1),
                         f'Игрок под номером {number} с ростом {height}'
                         f' играет на позиции {position}')

    def test_get_with_correct_field(self):
        player1 = BasketballPlayer(12, 'PG', 190.9)

        self.assertNotEqual(player1.number, 122)
        self.assertNotEqual(player1.position, 'PGG')
        self.assertNotEqual(player1.height, 190.99)

        self.assertEqual(player1.number, 12)
        self.assertEqual(player1.position, 'PG')
        self.assertEqual(player1.height, 190.9)

    def test_change_descriptor_fields(self):
        player = BasketballPlayer(12, 'PG', 190.9)

        player.number = 40
        self.assertEqual(player.number, 40)
        with self.assertRaises(expected_exception=TypeError):
            player.number = '40'
        with self.assertRaises(expected_exception=ValueError):
            player.number = 100
        self.assertEqual(player.number, 40)
        player.number = 67
        self.assertEqual(player.number, 67)

        player.position = 'C'
        self.assertEqual(player.position, 'C')
        with self.assertRaises(expected_exception=TypeError):
            player.position = 40
        with self.assertRaises(expected_exception=ValueError):
            player.position = 'CG'
        self.assertEqual(player.position, 'C')
        player.position = 'SF'
        self.assertEqual(player.position, 'SF')

        player.height = 194.2
        self.assertEqual(player.height, 194.2)
        with self.assertRaises(expected_exception=TypeError):
            player.height = 12
        with self.assertRaises(expected_exception=ValueError):
            player.height = -123.0

        self.assertEqual(player.height, 194.2)
        player.height = 194.8
        self.assertEqual(player.height, 194.8)


