from math import isclose


class CustomList(list):

    def __str__(self):
        return f'{super().__str__()} sum : {round(sum(self), 10)}'

    def __create_op_list(self, other):
        new_list = CustomList(self)
        if len(self) < len(other):
            new_list.extend([0 for i in range(len(other) - len(self))])
        return new_list

    def __add__(self, other):
        op_list = self.__create_op_list(other)
        for i, elem in enumerate(other):
            op_list[i] += elem
        return op_list

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        op_list = self.__create_op_list(other)
        for i, elem in enumerate(other):
            op_list[i] -= elem
        return op_list

    def __rsub__(self, other):
        op_list = CustomList(other)
        if len(self) > len(other):
            op_list.extend([0 for i in range(len(self) - len(other))])
        for i, elem in enumerate(self):
            op_list[i] -= elem
        return op_list

    def __isub__(self, other):
        return self.__sub__(other)

    def __eq__(self, other):
        return isclose(sum(self), sum(other))

    def __ne__(self, other):
        return not isclose(sum(self), sum(other))

    def __lt__(self, other):
        return not isclose(sum(self), sum(other)) and sum(self) < sum(other)

    def __gt__(self, other):
        return not isclose(sum(self), sum(other)) and sum(self) > sum(other)

    def __le__(self, other):
        return isclose(sum(self), sum(other)) or sum(self) < sum(other)

    def __ge__(self, other):
        return isclose(sum(self), sum(other)) or sum(self) > sum(other)
