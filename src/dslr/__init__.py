# sample/__init__.py

from .read import read
from .str_data import str_data

from .stat import \
    get_count, get_mean, \
    get_min, get_max, \
    get_median, get_quartile_1, get_quartile_3

from .histogram import plt_hist
from .scatter_plot import plt_scatter
from .pair_plot import plt_matrix

__all__ = [

    'read',

    'str_data',

    'get_count', 'get_mean',
    'get_min', 'get_max',
    'get_median', 'get_quartile_1', 'get_quartile_3',

    'plt_hist', 'plt_scatter', 'plt_matrix'

]
