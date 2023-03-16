import functools

class calculate_attributeWhenReadFirstTime(object):
    ''' Meant to be used for lazy evaluation of an object attribute.
    Property should represent non-mutable data, as it replaces itself. '''

    def __init__(self, fget):
        self.fget = fget

        # Copy the getter function's docstring and other attributes
        functools.update_wrapper(self, fget)

    def __get__(self, obj, cls):
        if obj is None:
            return self

        # The function itself is replaced by the value it calculates.
        value = self.fget(obj)
        setattr(obj, self.fget.__name__, value)
        return value

