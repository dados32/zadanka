def two_biggest_num(data):

    numbers = list(data)
    biggest = max(numbers)
    numbers.remove(biggest)
    second_biggest = max(numbers)
    return print(biggest, second_biggest)


if __name__ == '__main__':
    data = [2, 1, 4, 6, 88, 0, 5, 66, 4534, 999, 0, 2, -49]
    two_biggest_num(data)
    print(data)