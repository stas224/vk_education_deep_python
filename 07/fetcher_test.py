import asyncio
import unittest
from unittest import mock
import os

from aiounittest import AsyncTestCase

import fetcher


class TestFetcher(AsyncTestCase):
    async def test_process_url(self):
        async def text():
            return '<html><body><p>hello world</p></body></html>'

        response = mock.Mock()
        response.text = text
        response.url = 'http://example.com'
        await fetcher.process_url(response)

        filename = './count_words'
        with open(filename, 'r', encoding='UTF-8') as file:
            last_line = file.readlines()[-1]
            assert 'IN http://example.com 2 UNIQUE WORDS' in last_line

        if os.path.exists(filename):
            os.remove(filename)


class TestFetcher2(unittest.TestCase):
    def test_fetch_batch(self):
        filename = './urls.txt'
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write('https://en.wikipedia.org/wiki/1\n'
                       'https://en.wikipedia.org/wiki/2\n'
                       'https://en.wikipedia.org/wiki/3\n'
                       'https://en.wikipedia.org/wiki/4\n')

        with mock.patch('fetcher.fetch_url') as mock_file:
            asyncio.get_event_loop().run_until_complete(fetcher.fetch_batch((2, 'urls.txt')))

        self.assertEqual(mock_file.call_count, 4)

        if os.path.exists(filename):
            os.remove(filename)
