import argparse
from logger import get_logger, add_stream_handler, add_filter


log = get_logger()


class LRUCache:
    class Node:
        def __init__(self, key, val):
            log.debug("Creating new node, %s", self)
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, limit=42):
        self.__size = 0
        self.limit = limit
        self.__cache = {}
        self.__head = None
        self.__tail = None
        log.debug("Creating new cache %s with capacity %s", self, self.limit)

    def get(self, key):
        if key in self.__cache:
            log.info("Operation get:\t"
                     "key %s in cache", key)
            node = self.__cache[key]
            self.__replace_to_front(node)
            return node.val

        log.warning("Operation get:\t"
                    "key %s not in cache", key)
        return None

    def set(self, key, value):
        if key in self.__cache:
            log.info("Operation set:\t"
                     "changing value for existing key %s to %s", key, value)
            node = self.__cache[key]
            node.val = value
            self.__replace_to_front(node)
        else:
            log.info("Operation set:\t"
                     "new key %s, value %s", key, value)
            if self.__size == self.limit:
                self.__remove_last()
                self.__size -= 1
            self.__size += 1
            node = self.Node(key, value)
            self.__cache[key] = node
            self.__add_to_front(node)

    def __remove_last(self):
        if self.__tail is None:
            return
        log.info("Operation set:\t"
                 "overflow, remove last element %s (support)", self.__tail.key)
        del self.__cache[self.__tail.key]

        if self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev
            del self.__tail.next
            self.__tail.next = None

    def __add_to_front(self, node):
        log.debug("Add new node to front %s", node)
        if self.__head is None:
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def __replace_to_front(self, node):
        if self.__head == node:
            log.debug(f"Node %s is head, without move", node)
            return
        log.debug("Node %s isn't head, move to front", node)
        if self.__tail == node:
            self.__tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = None
        node.next = self.__head
        self.__head.prev = node
        self.__head = node


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", action="store_true")
    parser.add_argument("-f", action="store_true")
    return parser.parse_args()


def functional_test():
    cache = LRUCache(2)
    cache.set("k1", "1")
    cache.set("k2", "2")
    assert cache.get("k3") is None
    assert cache.get("k2") == "2"
    assert cache.get("k1") == "1"
    cache.set("k4", "3")
    cache.set("k4", "4")


if __name__ == "__main__":
    args = parse_args()

    if args.s:
        log = add_stream_handler(log)

    if args.f:
        log = add_filter(log)

    functional_test()

