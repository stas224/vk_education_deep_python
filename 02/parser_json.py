from typing import Callable
from json import loads


def example_function(log: dict):
    def inner(json_key: str, json_value: str):
        log[json_key].append(json_value)

    return inner


def parse_json(json_str: str,
               required_fields: list[str] = None,
               keywords: list[str] = None, *,
               keyword_callback: Callable = None) -> bool:
    if not all((json_str, required_fields, keywords, keyword_callback)):
        return False

    json_doc = loads(json_str)

    for field in required_fields:
        if field in json_doc:
            for keyword in keywords:
                for word in json_doc[field].split():
                    if word == keyword:
                        keyword_callback(field, keyword)
    return True
