import pandas
from . import formats
from . import tables

d1 = pandas.read_csv('D1.csv', **T.format.pandas_read_csv_args)


from functools import wraps

class ErrorListException(Exception):
    pass

def check_errors(fn):
    '''
    Function decorator for functions returning error information in the form of an iterable of
    error messages. If the decorated function returns an empty list or anything else that evaluates to False,
    no exception is raised. Otherwise, an exception is raised containing the concatenated error messages.
    '''
    @wraps(fn)
    def checker(*args, **kwargs):
        errors = fn(*args, **kwargs)
        if errors:
            raise ErrorListException(*errors)
    return checker
