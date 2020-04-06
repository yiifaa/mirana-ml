import pandas as pd
import os

def load_data():
    cwd = os.getcwd()
    data_path = os.path.join(cwd, "data\housing.csv")
    return pd.read_csv(data_path)

if __name__ == "__main__":
    housing = load_data()
    heads = housing.head(5)
    print(type(heads['longitude']))
    for row in heads['longitude']:
        print(row)
    print(type(housing.head(5))) 