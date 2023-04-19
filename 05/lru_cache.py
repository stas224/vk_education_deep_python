class LRUCache:
    class Node:  # pylint: disable=R0903
        def __init__(self, key, val):
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

    def get(self, key):
        if key in self.__cache:
            node = self.__cache[key]
            self.__replace_to_front(node)
            return node.val
        return None

    def set(self, key, value):
        if key in self.__cache:
            node = self.__cache[key]
            node.val = value
            self.__replace_to_front(node)
        else:
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

        del self.__cache[self.__tail.key]

        if self.__head == self.__tail:
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev
            del self.__tail.next
            self.__tail.next = None

    def __add_to_front(self, node):
        if self.__head is None:
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def __replace_to_front(self, node):
        if self.__head == node:
            return
        if self.__tail == node:
            self.__tail = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = None
        node.next = self.__head
        self.__head.prev = node
        self.__head = node
