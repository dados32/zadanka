def two_biggest_num(data):
    biggest = max(data)
    data.remove(biggest)
    second_biggest = max(data)
    return biggest, second_biggest


if __name__ == '__main__':
    numbers = [2, 1, 4, 6, 88, 0, 5, 66, 4534, 999, 0, 2, -49]
    two_biggest_num(numbers)
