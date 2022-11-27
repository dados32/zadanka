def string_splitter(text: str, key: str, split_num=float('inf')):
    index = text.find(key)
    new_list = []
    while index > -1 and split_num > 0:
        split_num -= 1
        new_list.append(text[0:index])
        text = text[index + len(key):]
        index = text.find(key)
    new_list.append(text)
    return print(new_list)


if __name__ == "__main__":
    tessk = "he Python return keyword exits a function and instructs Python to continue executing the main program. The return keyword can send a value back to the main program. A value could be a string, a tuple, or any other object. This is useful because it allows us to process data within a function."

    string_splitter(tessk, "i")

    print(f"tu dla porównania:\n {tessk.split('i')}")
