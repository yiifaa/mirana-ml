def add(start, end):
    sum = 0
    for i in range(start, end):
        sum = i + sum
    return sum

if __name__ == "__main__":
    print(add(1, 10))