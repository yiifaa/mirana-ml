import numpy as np
import pandas as pd


s = pd.Series([1, 3, 5])

if __name__ == "__main__":
    desc = s.describe()
    print(desc)