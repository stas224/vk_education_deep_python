import unittest
from custom_metaclass import CustomMeta


class CustomClass(metaclass=CustomMeta):
    test_x = 50

    def __init__(self, val=99):
        self.val = val

    def test_func(self) -> str:
        return f'{self}100'

    def __str__(self):
        return 'Custom_by_metaclass'


class TestMetaClassCustom(unittest.TestCase):

    def test_general_fields(self):
        self.test_var = CustomClass(12)  # pylint: disable=W0201
        self.assertFalse(hasattr(self.test_var, 'test_func'))
        self.assertFalse(hasattr(self.test_var, 'val'))
        self.assertFalse(hasattr(self.test_var, 'test_x'))
        self.assertTrue(hasattr(self.test_var, 'custom_test_func'))
        self.assertTrue(hasattr(self.test_var, 'custom_val'))
        self.assertTrue(hasattr(self.test_var, 'custom_test_x'))
        self.assertEqual(self.test_var.custom_test_x, 50)  # pylint: disable=E1101
        self.assertEqual(self.test_var.custom_val, 12)  # pylint: disable=E1101
        self.assertEqual(self.test_var.custom_test_func(),  # pylint: disable=E1101
                         f'{self.test_var}100')
        self.assertFalse(hasattr(self.test_var, 'custom___str__'))
        self.assertTrue(hasattr(self.test_var, '__str__'))
        self.assertEqual(str(self.test_var), 'Custom_by_metaclass')

    def test_additional_field(self):
        self.test_var = CustomClass()  # pylint: disable=W0201
        self.assertEqual(self.test_var.custom_val, 99)  # pylint: disable=E1101
        self.test_var.k = 12  # pylint: disable=W0201
        self.assertFalse(hasattr(self.test_var, 'k'))
        self.assertTrue(hasattr(self.test_var, 'custom_k'))
        self.assertEqual(self.test_var.custom_k, 12)  # pylint: disable=E1101
        CustomClass.boom = 'boom'
        self.assertFalse(hasattr(CustomClass, 'boom'))
        self.assertTrue(hasattr(CustomClass, 'custom_boom'))
        self.assertEqual(self.test_var.custom_boom, 'boom')  # pylint: disable=E1101


if __name__ == '__main__':
    unittest.main()
