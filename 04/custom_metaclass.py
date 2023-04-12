from typing import Any


class CustomMeta(type):

    def create_custom_setattr(cls, key: str, value: Any):
        object.__setattr__(cls, (f'custom_{key}', key)
                           [key.endswith('__') and key.startswith('__')],
                           value)

    @classmethod
    def create_custom_dict(mcs, class_dict: dict) -> dict:
        custom_dict = {
            (f'custom_{attr}', attr)
            [attr.endswith('__') and attr.startswith('__')]: value
            for attr, value in class_dict.items()
        }
        return custom_dict

    def __new__(mcs, name, bases, class_dict, **kwargs):
        custom_dict = mcs.create_custom_dict(class_dict)
        custom_dict["__setattr__"] = mcs.create_custom_setattr
        return super().__new__(mcs, name, bases, custom_dict, **kwargs)

    def __setattr__(cls, key, value):
        super().__setattr__((f'custom_{key}', key)
                            [key.endswith('__') and key.startswith('__')],
                            value)
