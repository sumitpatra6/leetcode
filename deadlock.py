counter = 0

def increase_counter():
    global counter
    counter += 1


def read_counter():
    return counter


def main():
    increase_counter()
    print(read_counter())


if __name__ == '__main__':
    main()
