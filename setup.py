from mirana.pandas.Series import init_series

def add(start, end):
    sum = 0
    for i in range(start, end):
        sum = i + sum
    return sum

if __name__ == "__main__":
    ser = init_series()
    desc = ser.describe()
    print(desc)
    print(add(1, 10))