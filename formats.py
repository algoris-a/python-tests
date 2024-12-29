import attr
import numpy
import pandas
from typing import List, Set

DATE_FORMAT = "%m/%d/%Y"
NS_DATE_FORMAT = "%m%d%Y"


@attr.s(slots=True, frozen=True)
class ColumnFormat:
    name: str = attr.ib()
    importer = attr.ib()
    is_index: bool = attr.ib(default=False)
    is_required: bool = attr.ib(default=True)
    allow_empty: bool = attr.ib(default=False)

@attr.s(slots=True, frozen=True)
class TableFormat:
    columns: List[ColumnFormat] = attr.ib() 
    index_column_names: List[str] = attr.ib(init=False)
    required_column_names: Set[str] = attr.ib(init=False) 
    required_index_column_names: List[str] = attr.ib(init=False) 
    date_column_names: List[str] = attr.ib(init=False) 
    pandas_read_csv_args: dict = attr.ib(init=False)
    pandas_to_csv_args = attr.ib(init=False)


    def __attrs_post_init__(self):
        object.__setattr__(self, 'index_column_names', [c.name for c in self.columns if c.is_index])
        object.__setattr__(self, 'required_column_names', [c.name for c in self.columns if c.is_required])
        object.__setattr__(self, 'required_index_column_names', [c.name for c in self.columns if c.is_index and c.is_required])
        object.__setattr__(self, 'date_column_names', [c.name for c in self.columns if c.importer in (DT, NS_DT)])
        dtype = {}
        parse_dates = []
        DT_type = None            # this assumes that all date columns are of the same type
        for c in self.columns:
            if c.importer in (DT, NS_DT):
                parse_dates.append(c.name)
                if DT_type is None:
                    DT_type = c.importer
                elif DT_type is not c.importer:
                    raise RuntimeError("Every column within a table must have the same date type (DT or NS_DT)")
            else:
                dtype[c.name] = c.importer
                
        d = dict(
            index_col=self.index_column_names,
            dtype = dtype,
            parse_dates = parse_dates,
            date_parser = DT_type,
            float_precision = 'round_trip')
        object.__setattr__(self, 'pandas_read_csv_args', d)
        if DT_type is None:
            d = dict(encoding='utf-8')
        elif DT_type is DT:
            d = dict(encoding='utf-8', date_format=DATE_FORMAT)
        elif DT_type is NS_DT:
            d = dict(encoding='utf-8', date_format=NS_DATE_FORMAT)
        else:
            raise NotImplementedError()
        object.__setattr__(self, 'pandas_to_csv_args', d)


F64 = numpy.float64
U16 = numpy.uint16
DT = lambda v: pandas.to_datetime(v, format=DATE_FORMAT)
NS_DT = lambda v: pandas.to_datetime(v, format=NS_DATE_FORMAT)
TF = TableFormat
CF = ColumnFormat


PRICE = TF(
    [
        CF('Cusip', str, is_index=True),
        CF('Inventory', str, is_index=True),
        CF('date', DT),
        CF('price', F64)
    ]
)