import unittest
from unittest import mock

from reading_and_filtering_generator import read_filter_generator


class TestReadFilterGenerator(unittest.TestCase):

    def test_read_filter_generator_with_all_arguments(self):

        contents_test = ["First line\nSecond line\nThird line",
                         "Яблоко от яблони недалеко падает\nХорошо там, где нас нет\n"
                         "Раз на раз не приходится\nГусь свинье не товарищ",
                         'Молокомолочкамилкивэймультики']
        wordlist_test = [['second', 'third'],
                         ['гусь', 'раз', 'товариш'],
                         ['молоко']]
        results = [['Second line', 'Third line'],
                   ["Гусь свинье не товарищ", "Раз на раз не приходится"],
                   ['Молокомолочкамилкивэймультики']]

        for file_content, wordlist, res in zip(contents_test, wordlist_test, results):
            with mock.patch('builtins.open', mock.mock_open(read_data=file_content)) as mock_file:
                result = list(read_filter_generator('test_file.txt', wordlist))
                self.assertCountEqual(result, res)
            mock_file.assert_called_once_with('test_file.txt', 'r', encoding='utf-8')

    def test_read_filter_generator_with_only_content(self):

        contents_test = ["First line\nSecond line\nThird line",
                         "Яблоко от яблони недалеко падает\nХорошо там, где нас нет\n"
                         "Раз на раз не приходится\nГусь свинье не товарищ",
                         'Молокомолочкамилкивэймультики']

        for file_content in contents_test:
            with mock.patch('builtins.open', mock.mock_open(read_data=file_content)) as mock_file:
                result = list(read_filter_generator('test_file.txt'))
                self.assertCountEqual(result, [])
            self.assertEqual(mock_file.call_count, 0)

    def test_read_filter_generator_with_only_wordlist(self):

        wordlist_test = [['second', 'third'],
                         ['гусь', 'раз', 'товариш'],
                         ['молоко']]

        for wordlist in wordlist_test:
            with mock.patch('builtins.open', mock.mock_open(read_data='test')) as mock_file:
                result = list(read_filter_generator(wordlist=wordlist))
                self.assertCountEqual(result, [])
            self.assertEqual(mock_file.call_count, 0)


if __name__ == '__main__':
    unittest.main()
