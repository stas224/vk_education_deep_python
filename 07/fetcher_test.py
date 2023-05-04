from unittest import mock
from unittest.mock import Mock
from aiounittest import AsyncTestCase
import aiofiles
import fetcher


class TestUrlsParser(AsyncTestCase):
    async def test_process_url(self):
        response = Mock()
        response.text = Mock(return_value='<html><body><p>hello world</p></body></html>')
        response.url = 'http://example.com'
        await fetcher.process_url(response)
        with open('count_words', 'r', encoding='UTF-8') as file:
            last_line = file.readlines()[-1]
            assert 'IN http://example.com 2 UNIQUE WORDS' in last_line

    async def test_fetch_batch(self):
        async with aiofiles.open('test_urls.txt', 'a', encoding='UTF-8') as file:
            await file.write(f'https://en.wikipedia.org/wiki/{1} \n')
            await file.write(f'https://en.wikipedia.org/wiki/{2} \n')
            await file.write(f'https://en.wikipedia.org/wiki/{3} ')

        await fetcher.fetch_batch((2, 'test_urls.txt'))


