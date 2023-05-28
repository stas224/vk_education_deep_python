import asyncio
import unittest
from unittest import mock
import os

import aioresponses
import aiounittest

import fetcher


class TestFetcher(aiounittest.AsyncTestCase):
    async def test_process_url(self):  # no network calls here
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

    async def test_fetch_url(self):  # no network calls here
        with aioresponses.aioresponses() as mock_url:
            mock_url.get('http://example.com',
                         status=200,
                         body='<html><body><p>hello world</p></body></html>')
            await fetcher.fetch_url('http://example.com')

        filename = './count_words'
        with open(filename, 'r', encoding='UTF-8') as file:
            last_line = file.readlines()[-1]
            assert 'IN http://example.com 2 UNIQUE WORDS' in last_line

        if os.path.exists(filename):
            os.remove(filename)

    async def test_fetch_batch(self):  # no network calls here
        source, output = './urls.txt', './count_words'
        test_digits = ((8, 1), (8, 4), (8, 8), (8, 10),
                       (1, 1), (1, 4), (1, 8), (1, 10),
                       (100, 1), (100, 4), (100, 8), (100, 100))

        for count_url, count_worker in test_digits:
            open(output, 'w').close()
            set_url = set()
            with open(source, 'w', encoding='UTF-8') as file:
                for i in range(count_url):
                    file.write(f'http://example.com/{i}\n')
                    set_url.add(f'IN http://example.com/{i} 2 UNIQUE WORDS \n')

            with aioresponses.aioresponses() as mock_url:
                for i in range(count_url):
                    mock_url.get(f'http://example.com/{i}',
                                 status=200,
                                 body=f'<html><body><p>hello world</p></body></html>')
                await fetcher.fetch_batch((count_worker, source))

            with open(output, 'r', encoding='UTF-8') as file:
                for line in file:
                    self.assertIn(line, set_url)

        if os.path.exists(source):
            os.remove(source)

        if os.path.exists(output):
            os.remove(output)


class TestFetcher2(unittest.TestCase):
    def test_fetch_batch_with_mock_fetch_url(self):  # no network calls here
        filename = './urls.txt'
        with open(filename, 'w', encoding='UTF-8') as file:
            file.write('https://en.wikipedia.org/wiki/1\n'
                       'https://en.wikipedia.org/wiki/2\n'
                       'https://en.wikipedia.org/wiki/3\n'
                       'https://en.wikipedia.org/wiki/4\n')

        with mock.patch('fetcher.fetch_url') as mock_file:
            asyncio.get_event_loop().run_until_complete(fetcher.fetch_batch((4, 'urls.txt')))

        self.assertEqual(mock_file.call_count, 4)

        if os.path.exists(filename):
            os.remove(filename)


if __name__ == '__main__':
    aiounittest.main()
    unittest.main()
