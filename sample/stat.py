from pandas import Series
import statistics as stat


def get_count(col: Series) -> float:
    """
    Return the len of a collumn.
    """

    assert isinstance(col, Series), \
        f"get_count :WrongType: col = {type(col)}"

    return (len(col))


def get_mean(col: Series) -> float:
    """
    Return the mean of a collumn.
    """

    assert isinstance(col, Series), \
        f"get_mean :WrongType: col = {type(col)}"

    return (stat.mean(col))


def get_min(col: Series) -> float:
    """
    Return the min of a collumn.
    """

    assert isinstance(col, Series), \
        f"get_min :WrongType: col = {type(col)}"

    return (min(col))


def get_max(col: Series) -> float:
    """
    Return the max of a collumn.
    """

    assert isinstance(col, Series), \
        f"get_max :WrongType: col = {type(col)}"

    return (max(col))


def get_median(col: Series) -> float:
    """
    Return the median of a collumn.
    """

    assert isinstance(col, Series), \
        f"get_median :WrongType: col = {type(col)}"

    return (stat.median(col))


def get_quartile_1(col: Series) -> float:
    """
    Return the first quartile of a collumn.
    """

    assert isinstance(col, Series), \
        f"get_median :WrongType: col = {type(col)}"

    return (stat.quantiles(col)[0])


def get_quartile_3(col: Series) -> float:
    """
    Return the first quartile of a collumn.
    """

    assert isinstance(col, Series), \
        f"get_median :WrongType: col = {type(col)}"

    return (stat.quantiles(col)[2])
