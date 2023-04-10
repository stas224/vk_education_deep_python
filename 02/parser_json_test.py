import unittest
from unittest import mock
from collections import defaultdict

from parser_json import parse_json, example_function


class TestParseJson(unittest.TestCase):

    def setUp(self):
        self.mock_func = mock.Mock(return_value=None)
        self.json_example = '{"width": "500 500", "height": "500", "data":' \
                            ' "Click Here", "style": "bold rush",' \
                            ' "name": "text1", "hOffset": "250",' \
                            ' "vOffset": "100", "alignment": "center",' \
                            ' "size" : "36 39"}'
        self.log = defaultdict(list)
        self.example_func = example_function(self.log)

    def test_parse_json_with_mock_function(self):
        res = parse_json(self.json_example,
                         keyword_callback=self.mock_func)
        self.assertEqual(res, False)
        self.assertEqual([], self.mock_func.mock_calls)

        res = parse_json(self.json_example,
                         ['width', 'height'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, False)
        self.assertEqual([], self.mock_func.mock_calls)

        res = parse_json(self.json_example,
                         keywords=['500', 'Click', 'center'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, False)
        self.assertEqual([], self.mock_func.mock_calls)

        res = parse_json(self.json_example,
                         ['width', 'height'],
                         ['500', 'Click', 'center'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, True)

        expected_calls = [mock.call('width', '500'),
                          mock.call('width', '500'),
                          mock.call('height', '500')]

        self.assertEqual(expected_calls, self.mock_func.mock_calls)

    def test_parse_json_with_example_function(self):
        res = parse_json(self.json_example,
                         keyword_callback=self.example_func)
        self.assertEqual(res, False)
        self.assertEqual(self.log, {})

        res = parse_json(self.json_example,
                         ['width', 'height'],
                         keyword_callback=self.example_func)
        self.assertEqual(res, False)
        self.assertEqual(self.log, {})

        res = parse_json(self.json_example,
                         keywords=['500', 'Click', 'center'],
                         keyword_callback=self.example_func)
        self.assertEqual(res, False)
        self.assertEqual(self.log, {})

        res = parse_json(self.json_example,
                         ['width', 'height'],
                         ['500', 'Click', 'center'])
        self.assertEqual(res, False)
        self.assertEqual(self.log, {})

        res = parse_json(self.json_example,
                         ['width', 'height'],
                         ['500', 'Click', 'center'],
                         keyword_callback=self.example_func)
        self.assertEqual(res, True)

        self.assertEqual(self.log, {'width': ['500', '500'],
                                    'height': ['500']})

    def test_parse_json_with_not_found_keywords(self):
        res = parse_json(self.json_example,
                         ['width', 'height'],
                         ['50000', 'Clicker',
                          'center_ls', '50'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, True)
        self.assertEqual([], self.mock_func.mock_calls)

        res = parse_json(self.json_example,
                         ['width', 'height'],
                         ['50', 'Cli', 'cent', '5'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, True)
        self.assertEqual([], self.mock_func.mock_calls)

        res = parse_json(self.json_example,
                         ['size', 'style'],
                         ['50000', 'Clicker', 'center_ls'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, True)
        self.assertEqual([], self.mock_func.mock_calls)

    def test_parse_json_with_multi_req_field(self):
        res = parse_json(self.json_example,
                         ['size', 'style'],
                         ['rush', 'bold', '36', '39'],
                         keyword_callback=self.mock_func)
        self.assertEqual(res, True)

        expected_calls = [mock.call('size', '36'),
                          mock.call('size', '39'),
                          mock.call('style', 'rush'),
                          mock.call('style', 'bold')]

        self.assertEqual(expected_calls, self.mock_func.mock_calls)


if __name__ == '__main__':
    unittest.main()
