class FlatIterator:
    def __init__(self, nested_list):
        self.data = self.flatten(nested_list)

    def flatten(self, nest_list):
        temp_list = list()
        for elem in nest_list:
            if type(elem) == list:
                temp_list += self.flatten(elem)
            else:
                temp_list.append(elem)
        return temp_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.data:
            return self.data.pop(0)
        else:
            raise StopIteration


def flat_generator(nest_list):
    for elem in nest_list:
        if type(elem) == list:
            for nest_elem in flat_generator(elem):
                yield nest_elem
        else:
            yield elem


def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    for item in flat_generator(nested_list):
        print(item)

    n_nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', ['h'], False],
        33,
        [1, [2, [3, 4, [5]]]],
        [1, 2, None],
    ]
    for item in FlatIterator(n_nested_list):
        print(item)
    for item in flat_generator(n_nested_list):
        print(item)


if __name__ == '__main__':
    main()
