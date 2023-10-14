def foo():
    return x


def bar(x):
    return foo()


if __name__ == '__main__':
    x = 3
    y = x + bar(5)

    print(y)
