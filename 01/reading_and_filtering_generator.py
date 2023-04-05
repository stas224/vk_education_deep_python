from typing import TextIO


def read_filter_generator(filename: (str, TextIO) = None, wordlist: list = None) -> str:

    def checking_line(line_to_check: str):
        return any(word.lower() in line_to_check.lower().split() for word in wordlist)

    def searching_lines(file: TextIO):
        for line in file:
            if checking_line(line):
                yield line.strip()

    if all((filename, wordlist)):
        if isinstance(filename, str):
            with open(filename, 'r', encoding='utf-8') as file_to_check:
                for find_line in searching_lines(file_to_check):
                    yield find_line
        else:
            for find_line in searching_lines(filename):
                yield find_line
