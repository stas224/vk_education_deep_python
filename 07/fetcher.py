import asyncio
import argparse

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
        except Exception as e:
            print(f'With {url=}: error {e=}')
        finally:
            queue.task_done()


async def fetch_batch(args):
    queue = asyncio.Queue(maxsize=int(args[0]))
    workers = [asyncio.create_task(run_worker(queue)) for _ in range(int(args[0]))]

    async with aiofiles.open(args[1], 'r', encoding='UTF-8') as file:
        async for url in file:
            url = url.strip()
            await queue.put(url)

    await queue.join()

    for worker in workers:
        worker.cancel()

    await asyncio.gather(*workers, return_exceptions=True)


def get_args() -> tuple[int, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", type=int, default=10, help="workers count")
    parser.add_argument("file", nargs=1)
    console_args = parser.parse_args()
    return console_args.c, console_args.file[0]


def fetcher():
    args = get_args()
    asyncio.get_event_loop().run_until_complete(fetch_batch(args))


if __name__ == "__main__":
    fetcher()
