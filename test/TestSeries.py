import sys
# sys.path.append("..")
from mirana.pandas.Series import init_series

if __name__ == "__main__":
    series = init_series()
    desc = series.describe()
    print(desc)