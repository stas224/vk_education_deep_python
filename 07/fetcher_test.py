import unittest
from unittest.mock import Mock
from aiounittest import AsyncTestCase
import aiofiles
import asyncio
import fetcher


class TestFetcher(AsyncTestCase):
    async def test_process_url(self):
        response = Mock()
        response.text = Mock(return_value='<html><body><p>hello world</p></body></html>')
        response.url = 'http://example.com'
        await fetcher.process_url(response)
        with open('count_words', 'r', encoding='UTF-8') as file:
            last_line = file.readlines()[-1]
            assert 'IN http://example.com 2 UNIQUE WORDS' in last_line


class TestFetcher2(unittest.TestCase):
    def test_fetch_batch(self):
        # with open('test_urls.txt', 'a', encoding='UTF-8') as file:
        #     file.write(f'https://en.wikipedia.org/wiki/{1} \n')
        #     file.write(f'https://en.wikipedia.org/wiki/{2} \n')
        #     file.write(f'https://en.wikipedia.org/wiki/{3} ')

        asyncio.get_event_loop().run_until_complete(fetcher.fetch_batch((2, 'test_urls.txt')))
