from random import random


class SomeModel:

    def __init__(self):
        self.message = []

    def predict(self, message: str) -> float:
        self.message.append(message)
        return random()

    def pylint_more_public_methods(self):
        pass


def predict_message_mood(message: str = None, model: SomeModel = None,
                         bad_thresholds: float = 0.3,
                         good_thresholds: float = 0.8) -> str:
    if not (isinstance(message, str) and isinstance(model, SomeModel)):
        raise TypeError("missing 'message' and 'model'")
    res = model.predict(message)
    if res < bad_thresholds:
        return 'неуд'
    if res > good_thresholds:
        return 'отл'
    return 'норм'
