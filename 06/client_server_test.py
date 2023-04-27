import argparse
from unittest import TestCase
import threading

from servers import start_server, get_common_words
from client import start_client


class TestClientServer(TestCase):
    def test_many_urls(self):
        args = argparse.Namespace(k=7, w=10)
        server_thread = threading.Thread(target=start_server, args=(args,))
        server_thread.start()
        start_client(["1", "urls.txt"])
        server_thread.join()
        url = "https://en.wikipedia.org/wiki/1"
        most_common_words = get_common_words(args, url)
        assert most_common_words == {{"the": 173, "1": 108, "of": 101, "is": 89, "a": 81, "to": 59, "and": 45}}
