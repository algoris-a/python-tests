# pde.py

import pandas

class DFE(pandas.DataFrame):
    def __and__(self, other):
        return super().__and__(other)

def read_csv(*args, **kwargs):
    return DFE(pandas.read_csv(*args, **kwargs))