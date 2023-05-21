import asyncio
import sys

import aiohttp
import aiofiles
from bs4 import BeautifulSoup


async def process_url(response):
    text = await response.text()
    soup = BeautifulSoup(text, 'html.parser')
    count_words = len(set(soup.get_text().split()))
    async with aiofiles.open('count_words', 'a', encoding='UTF-8') as file:
        await file.write(f'IN {response.url} {count_words} UNIQUE WORDS \n')


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            assert response.status == 200
            await process_url(response)


async def run_worker(queue):
    while True:
        url = await queue.get()
        try:
            await fetch_url(url)
        finally:
            queue.task_done()


async def fetch_batch(args):
    queue = asyncio.Queue()
    workers = [asyncio.create_task(run_worker(queue)) for _ in range(int(args[0]))]

    async with aiofiles.open(args[1], 'r', encoding='UTF-8') as file:
        async for url in file:
            url = url.strip()
            await queue.put(url)

    await queue.join()

    for worker in workers:
        worker.cancel()

    await asyncio.gather(*workers, return_exceptions=True)


def fetcher():
    console_args = sys.argv[1:]
    asyncio.get_event_loop().run_until_complete(fetch_batch(console_args))


if __name__ == "__main__":
    fetcher()
