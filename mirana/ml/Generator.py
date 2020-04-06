def sum(n):
    value = 0
    while(n > 0):
        value = value + n
        n = n - 1
        yield value

def iter(n):
    step = 0
    start, value = 1, 1
    while(step < n):
        if(step < 2):
            yield value
        else:
            temp = value
            value = start + value
            start = temp
            yield value    
        step = step + 1


if __name__ == '__main__':
    for value in sum(5):
        print(value)

    result = []
    for value in iter(10):
        result.append(value)
    print(result)    