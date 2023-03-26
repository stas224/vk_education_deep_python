import unittest
from unittest import mock
from collections import defaultdict

from parser_json import parse_json, example_function


class TestParseJson(unittest.TestCase):

    def setUp(self):
        self.mock_func = mock.Mock(return_value=None)
        self.json_example = '{"width": "500", "height": "500", "data":' \
                            ' "Click Here", "size": "36", "style": "bold",' \
                            ' "name": "text1", "hOffset": "250",' \
                            ' "vOffset": "100", "alignment": "center"}'
        self.log = defaultdict(list)
        self.example_func = example_function(self.log)

    def test_parse_json_with_mock_function(self):
        res = parse_json(self.json_example,
                         ['width', 'height'], ['500', 'Click', 'center'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, True)

        res = parse_json(self.json_example,
                         keyword_callback=self.mock_func)
        self.assertEqual(res, False)

        res = parse_json(self.json_example,
                         ['width', 'height'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, False)

        res = parse_json(self.json_example,
                         keywords=['500', 'Click', 'center'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, False)

    def test_parse_json_with_example_function(self):
        res = parse_json(self.json_example,
                         ['width', 'height'], ['500', 'Click', 'center'],
                         keyword_callback=self.example_func)
        self.assertEqual(res, True)

        res = parse_json(self.json_example,
                         keyword_callback=self.example_func)
        self.assertEqual(res, False)

        res = parse_json(self.json_example,
                         ['width', 'height'],
                         keyword_callback=self.example_func)
        self.assertEqual(res, False)

        res = parse_json(self.json_example,
                         keywords=['500', 'Click', 'center'],
                         keyword_callback=self.example_func)
        self.assertEqual(res, False)

        self.assertEqual(self.log, {'width': ['500'], 'height': ['500']})


if __name__ == '__main__':
    unittest.main()
