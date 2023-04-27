import argparse
import socket
import concurrent.futures
import threading
from collections import Counter
import json
import requests
from bs4 import BeautifulSoup

mutex = threading.Lock()
PROCESSED_URLS = 0


def get_common_words(args, url):
    top_words = args.k
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.get_text().split()
    most_common_words = dict(Counter(words).most_common(top_words))

    return most_common_words


def send_request(args, url, client_socket):
    global PROCESSED_URLS
    most_common_words = get_common_words(args, url)
    with mutex:
        PROCESSED_URLS += 1

    client_socket.send(json.dumps(most_common_words, ensure_ascii=False).encode())
    print(f"{PROCESSED_URLS=}")


def start_server(args):
    workers = args.w
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 8000))
        sock.listen(workers)
        while True:
            client_socket, _ = sock.accept()
            data = client_socket.recv(1024)
            url = data.decode().strip()
            executor.submit(send_request, args, url, client_socket)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", type=int, default=5, help="workers count")
    parser.add_argument("-k", type=int, default=5, help="most common words count")
    console_args = parser.parse_args()
    start_server(console_args)
