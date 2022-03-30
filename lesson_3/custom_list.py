"""Implements CustomList with per-elemental operations"""
import itertools
import functools
import operator


@functools.total_ordering
class MyCustomList:
    """
    Implemetation of CustomList

    Need to be cause total_ordering can't rewrite
    existing methods __lt__, __gt__, __le__, etc. in list
    """
    @staticmethod
    def __do_bin(func, left, right):
        return CustomList(
            [func(a, b) for a, b in itertools.zip_longest(left, right, fillvalue=0)]
        )

    def __sub__(self, deduct):
        return self.__do_bin(operator.sub, self, deduct)

    def __rsub__(self, reduced):
        return self.__do_bin(operator.sub, reduced, self)

    def __add__(self, addend):
        return self.__do_bin(operator.add, self, addend)

    def __radd__(self, addend):
        return self.__do_bin(operator.add, addend, self)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __str__(self):
        return f"{super().__str__()} sum={sum(self)}"


class CustomList(MyCustomList, list):
    """Wrapper for python list with per-elemaental operations"""
