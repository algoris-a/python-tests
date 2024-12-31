# pde.py

import pandas
import numpy as np

class Index:
    def __init__(self, index):
        self.index = index

    def __and__(self, other):
        a = set(self.index.values)
        b = set(other.index.values)
        ret_val = a & b
        return(ret_val)
        # What should it return? A new Index object? List of index values? 

class DFE(pandas.DataFrame):
    def __and__(self, other):
        return super().__and__(other)

def read_csv(*args, **kwargs):
    return DFE(pandas.read_csv(*args, **kwargs))