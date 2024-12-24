import attr
from typing import List
from . import formats

@attr.s(slots=True, frozen=True)
class Table:
    name: str = attr.ib()
    format: formats.TableFormat = attr.ib()
    filename: str = attr.ib()
    run_types: List[str] = attr.ib(attr.Factory(list))
    filtered_filename: str = attr.ib(init=False)

    def __attrs_post_init__(self):
        object.__setattr__(self, 'filtered_filename', f'{self.filename[:-4]}_filtered.csv' if self.run_types else self.filename)

TABLES = [
    Table('d1_price', formats.PRICE, 'D1.csv', ['D1', 'D2']),
    Table('d2_price', formats.PRICE, 'D2.csv', ['D2'])
]