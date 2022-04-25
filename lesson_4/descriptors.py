class Integer:
    __container: int

    def __init__(self, val: int = 0):
        self.__container = val

    def __get__(self, obj, objtype):
        return self.__container

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise ValueError(f"Can't assign {value} to Integer field")
        self.__container = value


class String:
    __container: str

    def __init__(self, val: str = ""):
        self.__container = val

    def __get__(self, obj, objtype):
        return self.__container

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise ValueError(f"Can't assign {value} to String field")
        self.__container = value


class PositiveInteger:
    __container: int

    def __init__(self, val: int = 1):
        self.__container = val

    def __get__(self, obj, objtype):
        return self.__container

    def __set__(self, obj, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"Can't assign {value} to PositiveInteger field")
        self.__container = value
