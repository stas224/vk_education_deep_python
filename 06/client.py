import socket
import concurrent.futures
import sys


def send_request(url):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.connect(('localhost', 8000))
    server_sock.send(url.encode())
    response = server_sock.recv(1024).decode()
    server_sock.close()
    print(f'{str(url)} :{response}')


def start_client(args):
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(args[0])) as executor:
        for url in open(args[1], "r", encoding='UTF-8'):
            executor.submit(send_request, url)


if __name__ == '__main__':
    console_args = sys.argv[1:]
    start_client(console_args)
