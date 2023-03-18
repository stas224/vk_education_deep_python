def read_filter_generator(filename: str = None, wordlist: list = None) -> str:

    def checking_line(line_to_check: str):
        return any(word.lower() in line_to_check.lower() for word in wordlist)

    if all((filename, wordlist)):
        with open(filename, 'r', encoding='utf-8') as file_to_check:
            for line in file_to_check:
                if checking_line(line):
                    yield line.strip()
