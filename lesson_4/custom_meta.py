class CustomMeta(type):
    def __setattr__(cls, name, value):  # pylint: disable=function-redefined
        name = "custom_" + name if not CustomMeta.__is_magic(name) else name
        super().__setattr__(name, value)

    @staticmethod
    def __is_magic(name):
        return name.startswith("__") and name.endswith("__")

    def __init__(cls, name, bases, classdict):
        super().__init__(name, bases, classdict)

        def wrap(self, name, value):
            name = "custom_" + name if not CustomMeta.__is_magic(name) else name
            object.__setattr__(self, name, value)

        cls.__setattr__ = wrap
        for cname in classdict:
            if not CustomMeta.__is_magic(cname):
                setattr(cls, cname, getattr(cls, cname))
                delattr(cls, cname)
