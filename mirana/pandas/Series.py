import numpy as np
import pandas as pd

def init_series():
    return pd.Series([1, 3, 5])




if __name__ == "__main__":
    s = init_series()
    desc = s.describe()
    print(desc)