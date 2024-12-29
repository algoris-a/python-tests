import pandas
import formats
import tables
from pde import DFE
from pde import read_csv

# direct read

p1 = read_csv('D1.csv', parse_dates=['date'], index_col='Cusip')
p2 = read_csv('D2.csv', parse_dates=['date'], index_col='Cusip')      

p = p1 & p2

t = {}
for T in tables.TABLES:
    t[T.name] = pandas.read_csv(T.filename, **T.format.pandas_read_csv_args)

a = t['d1_price']
b = t['d2_price']
c = t['d1_price'] & t['d2_price']

print('done')

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
